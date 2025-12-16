import streamlit as st
import pandas as pd
from google.oauth2.service_account import Credentials
import gspread
import json

# Initialize Streamlit page config
st.set_page_config(
    page_title="FINMEN Rating Intelligence Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏦 FINMEN Rating Intelligence Engine")
st.markdown("Automate your initial assessment process by inputting rating rationales")

# Check if we're in demo mode or production mode
DEMO_MODE = True
worksheet = None

if 'google_sheets_key' in st.secrets and 'google_sheet_id' in st.secrets:
    try:
        creds_dict = st.secrets['google_sheets_key']
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
        gc = gspread.authorize(creds)
        sheet_id = st.secrets.get('google_sheet_id')
        worksheet = gc.open_by_key(sheet_id)
        DEMO_MODE = False
    except Exception as e:
        st.warning(f"Could not connect to Google Sheets: {str(e)}")
        st.info("Running in DEMO MODE - Data will be stored in session only")
else:
    st.warning("Google Sheets credentials not configured")
    st.info("Running in DEMO MODE - To enable production mode, add Google credentials to Streamlit Secrets")

# Initialize demo data in session state
if 'demo_data' not in st.session_state:
    st.session_state.demo_data = pd.DataFrame(columns=[
        'Company Name', 'Rating Agency', 'Instrument Type', 
        'Rating', 'Outlook', 'Rating Action', 'Rationale'
    ])

# Create tabs
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
            if DEMO_MODE:
                new_row = pd.DataFrame({
                    'Company Name': [company_name],
                    'Rating Agency': [agency],
                    'Instrument Type': [instrument_type],
                    'Rating': [rating],
                    'Outlook': [outlook],
                    'Rating Action': [rating_action],
                    'Rationale': [rationale]
                })
                st.session_state.demo_data = pd.concat([st.session_state.demo_data, new_row], ignore_index=True)
                st.success(f"✅ Rationale for {company_name} saved to session (Demo Mode)")
            else:
                try:
                    rationales_sheet = worksheet.worksheet("Raw_Rationales_DB")
                    rationales_sheet.append_row([company_name, agency, instrument_type, rating, outlook, rating_action, rationale])
                    st.success(f"✅ Rationale for {company_name} submitted successfully!")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill in all required fields")

with tab2:
    st.header("📊 View Data")
    
    if DEMO_MODE:
        st.info("📌 Demo Mode - Showing session data")
        if len(st.session_state.demo_data) > 0:
            st.dataframe(st.session_state.demo_data, use_container_width=True)
        else:
            st.info("No data yet. Submit a rationale to see it here.")
    else:
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
            st.error(f"Error: {str(e)}")

with tab3:
    st.header("🔍 Analysis & Insights")
    st.info("📌 Analysis features coming soon...")
    st.markdown("""
    - Peer comparison analysis
    - Rating trends
    - Upgrade/Downgrade signals
    - Agency recommendations
    """)

st.sidebar.markdown("---")
if DEMO_MODE:
    st.sidebar.warning("🔴 DEMO MODE ACTIVE")
    st.sidebar.info("Data stored in session only. Configure Google Sheets credentials to enable production mode.")
else:
    st.sidebar.success("🟢 PRODUCTION MODE")
    st.sidebar.info("Connected to Google Sheets")

st.sidebar.markdown("---")
st.sidebar.info("💡 **FINMEN Rating Intelligence Engine**\n\nAutomates the initial assessment process by analyzing rating rationales and providing peer comparisons and agency recommendations.")
