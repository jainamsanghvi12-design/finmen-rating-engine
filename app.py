import streamlit as st
import pandas as pd
from google.oauth2.service_account import Credentials
import gspread
import json
import os

# Initialize Streamlit page config
st.set_page_config(
    page_title="FINMEN Rating Intelligence Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏦 FINMEN Rating Intelligence Engine")
st.markdown("Automate your initial assessment process by inputting rating rationales")

# Google Sheets credentials
if 'google_sheets_key' not in st.secrets:
    st.error("Google Sheets credentials not found in secrets")
    st.stop()

creds_dict = json.loads(st.secrets['google_sheets_key'])
scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
gc = gspread.authorize(creds)

# Open the FINMEN Google Sheet
sheet_id = st.secrets.get('google_sheet_id')
if not sheet_id:
    st.error("Google Sheet ID not found in secrets")
    st.stop()

worksheet = gc.open_by_key(sheet_id)

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["Input Rationale", "View Data", "Analysis"])

with tab1:
    st.header("📝 Input Rating Rationale")
    
    col1, col2 = st.columns(2)
    
    with col1:
        company_name = st.text_input("Company Name")
        agency = st.text_input("Rating Agency")
        instrument_type = st.selectbox("Instrument Type", ["Bond", "Debenture", "Commercial Paper"])
    
    with col2:
        rating = st.selectbox("Rating", ["AAA", "AA+", "AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-", "BB+", "BB", "BB-"])
        outlook = st.selectbox("Outlook", ["Positive", "Stable", "Negative"])
        rating_action = st.selectbox("Rating Action", ["Initial Rating", "Upgrade", "Downgrade", "Affirmed"])
    
    rationale = st.text_area("Rating Rationale", placeholder="Enter the detailed rating rationale here...")
    
    if st.button("Submit Rationale", type="primary"):
        if company_name and agency and rating and rationale:
            try:
                # Get the Raw_Rationales_DB sheet
                rationales_sheet = worksheet.worksheet("Raw_Rationales_DB")
                
                # Append the new rationale
                rationales_sheet.append_row([
                    company_name,
                    agency,
                    instrument_type,
                    rating,
                    outlook,
                    rating_action,
                    rationale
                ])
                
                st.success(f"✅ Rationale for {company_name} submitted successfully!")
            except Exception as e:
                st.error(f"Error submitting rationale: {str(e)}")
        else:
            st.warning("Please fill in all required fields")

with tab2:
    st.header("📊 View Data")
    
    sheet_selector = st.selectbox("Select Sheet", ["Raw_Rationales_DB", "Company_Profiles"])
    
    try:
        selected_sheet = worksheet.worksheet(sheet_selector)
        data = selected_sheet.get_all_records()
        
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No data in this sheet yet.")
    except Exception as e:
        st.error(f"Error reading sheet: {str(e)}")

with tab3:
    st.header("🔍 Analysis & Insights")
    
    st.info("📌 Analysis features coming soon...")
    st.markdown("""
    This section will include:
    - Peer comparison analysis
    - Rating trends
    - Upgrade/Downgrade signals
    - Agency recommendations
    """)

st.sidebar.markdown("---")
st.sidebar.info("💡 **About FINMEN Rating Intelligence Engine**\n\nThis tool automates the initial assessment process by analyzing rating rationales and providing peer comparisons and agency recommendations.")
