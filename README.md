# FINMEN Rating Intelligence Engine v2

## Overview

FINMEN Rating Intelligence Engine is a Streamlit-based application that automates the initial assessment (IA) process for credit rating analysis. By inputting rating rationales, the engine automatically generates peer ratings, agency recommendations, and opportunity flags.

## Features

- **Automated Analysis**: Input rating rationales and get instant peer comparisons
- **Multi-Agency Support**: Compare ratings across multiple rating agencies
- **Real-time Data**: Pull data from Google Sheets for seamless collaboration
- **Interactive Dashboard**: Three-tab interface for input, data viewing, and analysis
- **Rating Insights**: Identify upgrade/downgrade signals and opportunity flags

## Installation

### Prerequisites
- Python 3.8+
- Streamlit
- Google Cloud credentials with Sheets API access
- A Google Sheet set up with the following sheets:
  - Raw_Rationales_DB
  - Company_Profiles
  - Peer_Matches_Logic

### Setup

1. Clone the repository
```bash
git clone https://github.com/jainamsanghvi12-design/finmen-rating-engine.git
cd finmen-rating-engine
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure Streamlit secrets
Create a `.streamlit/secrets.toml` file:
```toml
google_sheets_key = "{
  \"type\": \"service_account\",
  \"project_id\": \"your-project-id\",
  \"private_key_id\": \"your-key-id\",
  \"private_key\": \"your-private-key\",
  \"client_email\": \"your-email@your-project.iam.gserviceaccount.com\",
  \"client_id\": \"your-client-id\",
  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",
  \"token_uri\": \"https://oauth2.googleapis.com/token\",
  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",
  \"client_x509_cert_url\": \"your-cert-url\"
}"

google_sheet_id = "your-sheet-id"
```

4. Run the application
```bash
streamlit run app.py
```

## Usage

### Tab 1: Input Rationale
- Enter company name, rating agency, and instrument type
- Select rating, outlook, and rating action
- Provide detailed rating rationale
- Click "Submit Rationale" to save to Google Sheets

### Tab 2: View Data
- Select which sheet to view (Raw_Rationales_DB or Company_Profiles)
- View all submitted data in a formatted table

### Tab 3: Analysis & Insights
- Coming soon: Peer comparison analysis, rating trends, and recommendations

## Architecture

### Data Flow
1. User inputs rating rationale via Streamlit UI
2. Data is saved to Raw_Rationales_DB sheet in Google Sheets
3. Engine processes data and identifies peer companies
4. Results are displayed in the Analysis tab

### Google Sheets Structure
- **Raw_Rationales_DB**: Stores all input rationales
- **Company_Profiles**: Contains company metadata and profiles
- **Peer_Matches_Logic**: Matching logic for peer identification

## Deployment

### Deploy to Streamlit Cloud
1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repository
4. Add secrets in the Streamlit dashboard
5. Deploy!
6. 
### Configuration

**Setting up Streamlit Secrets:**

To properly configure the app, you need to add your Google Sheets credentials to the Streamlit Cloud secrets:

1. Go to your app settings in Streamlit Cloud
2. Navigate to the "Secrets" tab
3. Paste your Google service account JSON credentials in the following format:

```toml
google_sheets_key = {
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key_id": "your-private-key-id",
    "private_key": "your-private-key",
    "client_email": "your-service-account@your-project.iam.gserviceaccount.com",
    "client_id": "your-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "your-cert-url"
}

google_sheet_id = "your-google-sheet-id"
```

**Note:** Make sure to replace the values with your actual Google service account credentials and Google Sheet ID.

## Contact

For questions or support, please reach out to the development team.
