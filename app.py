import streamlit as st
import pandas as pd
from google.oauth2.service_account import Credentials
import gspread
import json
import io
from datetime import datetime

# Initialize Streamlit page config
st.set_page_config(
    page_title="FINMEN Rating Intelligence Engine v2",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏦 FINMEN Rating Intelligence Engine v2")
st.markdown("**Enhanced AI-powered rating rationale analysis with peer comparison engine**")

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
        'Rationale_ID', 'Company Name', 'Rating Agency', 'Instrument Type', 
        'Rating', 'Outlook', 'Rating Action', 'Rationale', 'Uploaded Files', 'Timestamp'
    ])

if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = {}

# Create tabs
tab1, tab2, tab3 = st.tabs(["📝 Input Rationale", "📊 View Data", "🔍 Analysis & Insights"])

with tab1:
    st.header("📝 Submit Rating Rationale")
    
    col1, col2 = st.columns(2)
    
    with col1:
        company_name = st.text_input("Company Name", placeholder="Enter company name")
        agency = st.text_input("Rating Agency", placeholder="e.g., CRISIL, ICRA, Fitch")
        instrument_type = st.selectbox("Instrument Type", [
            "Bond", "Debenture", "Commercial Paper", "Bank Facilities", "Long-term Loan", "Short-term Loan"
        ])
    
    with col2:
        rating = st.selectbox("Rating", [
            "AAA", "AA+", "AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-", "BB+", "BB", "BB-", "B+", "B"
        ])
        outlook = st.selectbox("Outlook", ["Positive", "Stable", "Negative", "Developing"])
        rating_action = st.selectbox("Rating Action", ["Initial Rating", "Upgrade", "Downgrade", "Affirmed", "Withdrawn"])
    
    st.divider()
    st.subheader("Rationale & Supporting Documents")
    
    rationale = st.text_area("Rating Rationale", placeholder="Enter detailed rating rationale...\n\nInclude:\n- Financial metrics and trends\n- Industry dynamics\n- Management quality\n- Risk factors\n- Comparable peer analysis", height=200)
    
    st.markdown("**Upload Supporting Documents**")
    uploaded_files = st.file_uploader(
        "Upload PDF, Excel, or Word documents",
        type=["pdf", "xlsx", "xls", "docx", "txt"],
        accept_multiple_files=True,
        help="Support financial statements, credit analysis, market reports"
    )
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully")
        for file in uploaded_files:
            st.caption(f"📎 {file.name} ({file.size/1024:.1f} KB)")
    
    st.divider()
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("🚀 Submit Rationale", type="primary", use_container_width=True):
            if company_name and agency and rating and rationale:
                # Generate rationale ID
                rationale_id = f"RAT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
                
                # Store uploaded files
                file_names = ", ".join([f.name for f in uploaded_files]) if uploaded_files else "None"
                if uploaded_files:
                    st.session_state.uploaded_files[rationale_id] = uploaded_files
                
                if DEMO_MODE:
                    # Demo mode: store in session
                    new_row = pd.DataFrame({
                        'Rationale_ID': [rationale_id],
                        'Company Name': [company_name],
                        'Rating Agency': [agency],
                        'Instrument Type': [instrument_type],
                        'Rating': [rating],
                        'Outlook': [outlook],
                        'Rating Action': [rating_action],
                        'Rationale': [rationale],
                        'Uploaded Files': [file_names],
                        'Timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
                    })
                    st.session_state.demo_data = pd.concat([st.session_state.demo_data, new_row], ignore_index=True)
                    st.success(f"✅ Rationale {rationale_id} saved (Demo Mode)")
                else:
                    try:
                        # Production mode: save to Google Sheets
                        rationales_sheet = worksheet.worksheet("Raw_Rationales_DB")
                        rationales_sheet.append_row([
                            rationale_id, company_name, agency, instrument_type, rating, outlook, 
                            rating_action, rationale, file_names, datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        ])
                        st.success(f"✅ Rationale {rationale_id} submitted to Google Sheets!")
                    except Exception as e:
                        st.error(f"Error saving to Google Sheets: {str(e)}")
                
                # Clear form
                st.rerun()
            else:
                st.warning("⚠️ Please fill in all required fields (Company, Agency, Rating, Rationale)")
    
    with col2:
        st.write("")  # Spacing

with tab2:
    st.header("📊 View Submitted Rationales")
    
    if DEMO_MODE:
        st.info("📌 Demo Mode - Showing rationales from current session")
    else:
        st.success("🟢 Connected to Google Sheets")
    
    if len(st.session_state.demo_data) > 0:
        # Display summary stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Rationales", len(st.session_state.demo_data))
        with col2:
            st.metric("Unique Companies", st.session_state.demo_data['Company Name'].nunique())
        with col3:
            st.metric("Rating Agencies", st.session_state.demo_data['Rating Agency'].nunique())
        with col4:
            st.metric("Instrument Types", st.session_state.demo_data['Instrument Type'].nunique())
        
        st.divider()
        
        # Display data table
        display_cols = ['Rationale_ID', 'Company Name', 'Rating Agency', 'Instrument Type', 'Rating', 'Outlook', 'Rating Action', 'Timestamp']
        st.dataframe(st.session_state.demo_data[display_cols], use_container_width=True, height=400)
        
        # Export option
        csv = st.session_state.demo_data.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name=f"rationales_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    else:
        st.info("No rationales submitted yet. Start by submitting a rationale in the Input tab.")

with tab3:
    st.header("🔍 Analysis & Peer Comparison Engine")
    
    if len(st.session_state.demo_data) > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            selected_company = st.selectbox(
                "Select Company for Analysis",
                st.session_state.demo_data['Company Name'].unique()
            )
        
        with col2:
            metric_type = st.selectbox(
                "Analysis Type",
                ["Rating Distribution", "Agency Comparison", "Instrument Trends", "Peer Benchmark"]
            )
        
        st.divider()
        
        # Get company data
        company_data = st.session_state.demo_data[st.session_state.demo_data['Company Name'] == selected_company]
        
        if not company_data.empty:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                latest_rating = company_data.iloc[0]['Rating']
                st.metric("Latest Rating", latest_rating)
            
            with col2:
                outlook = company_data.iloc[0]['Outlook']
                st.metric("Current Outlook", outlook)
            
            with col3:
                num_ratings = len(company_data)
                st.metric("Rating History", num_ratings)
            
            st.divider()
            st.subheader("Company Ratings by Agency")
            
            # Show all ratings for this company
            agency_ratings = company_data.groupby('Rating Agency').agg({
                'Rating': 'last',
                'Outlook': 'last',
                'Rationale_ID': 'count'
            }).rename(columns={'Rationale_ID': 'Updates'})
            
            st.dataframe(agency_ratings, use_container_width=True)
            
            st.divider()
            st.subheader("📝 Latest Rationale")
            st.text_area("Rationale Text", value=company_data.iloc[0]['Rationale'], disabled=True, height=200)
            
        else:
            st.warning("No data available for this company.")
        
        st.divider()
        st.subheader("📊 Market Analysis")
        
        # Rating distribution
        rating_dist = st.session_state.demo_data['Rating'].value_counts().sort_index()
        st.bar_chart(rating_dist, use_container_width=True)
        
        # Outlook distribution
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Outlook Distribution")
            outlook_dist = st.session_state.demo_data['Outlook'].value_counts()
            st.bar_chart(outlook_dist)
        
        with col2:
            st.subheader("Instrument Type Distribution")
            instrument_dist = st.session_state.demo_data['Instrument Type'].value_counts()
            st.bar_chart(instrument_dist)
        
    else:
        st.info("📌 No data available for analysis yet. Submit rationales to see insights.")
        st.markdown("""
        **What you'll see here:**
        - Peer company comparisons
        - Rating trends and changes
        - Upgrade/Downgrade signals
        - Agency recommendations
        - Market benchmarking
        """)

# Sidebar information
st.sidebar.markdown("---")
if DEMO_MODE:
    st.sidebar.warning("🔴 DEMO MODE ACTIVE")
    st.sidebar.info("Data stored in session only. Configure Google Sheets credentials to enable production mode.")
else:
    st.sidebar.success("🟢 PRODUCTION MODE")
    st.sidebar.info("Connected to Google Sheets")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Quick Stats")
st.sidebar.metric("Total Rationales", len(st.session_state.demo_data))
st.sidebar.metric("Companies Analyzed", st.session_state.demo_data['Company Name'].nunique())

st.sidebar.markdown("---")
st.sidebar.info("""
**FINMEN Rating Intelligence Engine v2**

Automates the initial assessment (IA) process by analyzing rating rationales and providing:
- Peer company comparisons
- Rating trend analysis
- Upgrade/Downgrade signals
- Agency recommendations
""")
