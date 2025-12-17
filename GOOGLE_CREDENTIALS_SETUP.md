# 🔐 Google Credentials Setup - Step-by-Step

## **What You Need**
Before deployment, you need:
1. Google Cloud Project with Sheets API enabled
2. Service Account with proper permissions
3. Google Sheet ID for data storage
4. JSON credentials file

---

## **STEP 1: Create Google Cloud Project** (5 min)

### 1.1 Go to Google Cloud Console
- Visit: https://console.cloud.google.com
- Sign in with your Google account

### 1.2 Create New Project
- Click **"Select a Project"** at top
- Click **"NEW PROJECT"**
- Name it: `finmen-rating-engine`
- Click **CREATE**
- Wait for creation to complete

### 1.3 Enable APIs
- In search bar, search for **"Google Sheets API"**
- Click on it
- Click **ENABLE**

- Search for **"Google Drive API"**
- Click on it  
- Click **ENABLE**

---

## **STEP 2: Create Service Account** (5 min)

### 2.1 Create Service Account
- In left sidebar, go to **"Service Accounts"**
- Click **"CREATE SERVICE ACCOUNT"**
- Service account name: `finmen-sa`
- Service account ID: (auto-filled)
- Click **CREATE AND CONTINUE**

### 2.2 Grant Permissions
- Select role: **Editor** (full access)
- Click **CONTINUE**
- Click **DONE**

---

## **STEP 3: Create & Download JSON Key** (3 min)

### 3.1 Generate JSON Key
- Click on the service account you just created
- Go to **KEYS** tab
- Click **ADD KEY** → **Create new key**
- Select **JSON**
- Click **CREATE**
- JSON file automatically downloads
- **Save this file securely!** ⚠️

### 3.2 What's in the JSON?
```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "...",
  "private_key": "...",
  "client_email": "finmen-sa@...",
  "client_id": "...",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "...",
  "client_x509_cert_url": "..."
}
```

---

## **STEP 4: Create Google Sheet** (3 min)

### 4.1 Create New Sheet
- Go to https://sheets.google.com
- Click **"+ NEW"**
- Create new spreadsheet
- Name it: `FINMEN_Rating_Analysis_DB`

### 4.2 Create Sheet Tabs
Rename the first sheet to `Raw_Rationales_DB`

Add 2 more sheets:
1. **Company_Profiles**
2. **Peer_Matches_Logic**

### 4.3 Get Sheet ID
- Copy the Sheet ID from URL:
```
https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit#gid=0
                                            ^
                                      Copy this part
```

### 4.4 Share with Service Account
- Click **SHARE**
- Paste the service account email (from JSON: `client_email`)
- Give **Editor** access
- Click **SHARE**

---

## **STEP 5: Configure Local .env File** (2 min)

### 5.1 Edit .env.example
```bash
cp .env.example .env
```

### 5.2 Update .env
```env
# Google Sheets
GOOGLE_SHEET_ID=your_sheet_id_here
GOOGLE_SHEETS_KEY={your_json_content}

# Optional: AI Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# App Config
DEBUG=False
DEMO_MODE=False
```

### 5.3 Add JSON Content
- Open the downloaded JSON file
- Copy **entire** content
- Paste into `GOOGLE_SHEETS_KEY=` value
- Make sure it's valid JSON

---

## **STEP 6: Test Configuration** (2 min)

### 6.1 Run Validation
```bash
python test_finmen.py
```

Look for:
- ✅ Google Auth - PASS
- ✅ Gspread - PASS
- ✅ File exists: .env - PASS

### 6.2 Manual Test
```python
import gspread
from google.oauth2.service_account import Credentials

# Load your JSON
creds = Credentials.from_service_account_file('finmen-sa.json')
gc = gspread.authorize(creds)
sh = gc.open_by_key('YOUR_SHEET_ID')
print("✅ Connected successfully!")
```

---

## **STEP 7: Deploy to Streamlit Cloud** (5 min)

### 7.1 Go to Streamlit Cloud
- Visit: https://share.streamlit.io
- Sign in with GitHub

### 7.2 Deploy App
- Click **"New app"**
- Select your GitHub repo
- Select branch: `main`
- Set main file path: `app.py`
- Click **DEPLOY**

### 7.3 Add Secrets
- Once deployed, click **Settings** (gear icon)
- Go to **"Secrets"** tab
- Add this:

```toml
[google_sheets_key]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-key-id"
private_key = "your-private-key"
client_email = "your-email@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"

google_sheet_id = "your-sheet-id"
```

### 7.4 Reboot App
- Click **"Reboot app"** button
- Wait for deployment
- Visit your live URL

---

## **Troubleshooting**

### "API Key not valid"
- Verify JSON is properly formatted
- Check service account has Editor role

### "Sheet not found"
- Verify Sheet ID is correct
- Verify service account email has access
- Try sharing sheet again with Editor role

### "Permission denied"
- Check service account `client_email` has Editor access
- Verify APIs are enabled in Cloud Console

---

## **Security Tips** 🔒

⚠️ **Never commit these to GitHub:**
- .env file
- JSON credentials file
- API keys

✅ **Do use:**
- .gitignore for sensitive files
- Streamlit Secrets for cloud deployment
- Environment variables locally

---

## **Final Checklist**

- [ ] Created Google Cloud Project
- [ ] Enabled Sheets & Drive APIs
- [ ] Created Service Account
- [ ] Downloaded JSON credentials
- [ ] Created Google Sheet with 3 tabs
- [ ] Got Sheet ID
- [ ] Shared sheet with service account
- [ ] Created and configured .env file
- [ ] Ran test_finmen.py successfully
- [ ] Deployed to Streamlit Cloud
- [ ] Added secrets to Streamlit dashboard
- [ ] App is working live ✨

---

**Stuck?** Check QUICK_START.md or DEPLOYMENT_READY.md for more help!
