# 🚀 FINMEN Rating Intelligence Engine v2 - Quick Start

## **Get Started in 5 Minutes!**

### **Step 1: Install Dependencies** (2 min)
```bash
pip install -r requirements.txt
```

### **Step 2: Validate Installation** (1 min)
```bash
python test_finmen.py
```
✅ If all tests pass, you're ready to go!

### **Step 3: Run Locally** (1 min)
```bash
streamlit run app.py
```
The app opens at `http://localhost:8501`

### **Step 4: Test the App** (1 min)
1. **Input Tab**: Submit a test rating
2. **View Data Tab**: See your submission
3. **Analysis Tab**: View peer matches and insights

---

## **What's Next?**

### **For Testing & Development**
- Edit `peer_matcher.py` to customize peer matching logic
- Modify `search_engine.py` to enhance search features
- Update `ai_analyzer.py` for better AI analysis

### **Before Production**
1. **Create Google Service Account**
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create service account with Sheets API access
   - Download JSON credentials

2. **Create Google Sheet** with 3 tabs:
   - `Raw_Rationales_DB` - Input rationales
   - `Company_Profiles` - Company data
   - `Peer_Matches_Logic` - Peer matching results

3. **Deploy to Streamlit Cloud**
   - Push code to GitHub
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your repo
   - Add secrets (Google credentials)
   - Deploy!

---

## **Key Features**

✅ **Peer Matching** - Intelligent company matching  
✅ **Full-Text Search** - Fast rationale search  
✅ **AI Analysis** - NLP-powered rating analysis  
✅ **Multi-Agency** - Support for 7+ rating agencies  
✅ **Data Export** - Download as CSV  
✅ **Real-Time Insights** - Live charts and stats  

---

## **Troubleshooting**

**Q: Tests failing?**  
A: Run `pip install --upgrade -r requirements.txt`

**Q: Streamlit not found?**  
A: Ensure you're in the correct directory and virtual environment activated

**Q: Google Sheets not connecting?**  
A: Check credentials in `.env` file or Streamlit secrets

---

## **Commands Cheat Sheet**

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python test_finmen.py

# Start app locally
streamlit run app.py

# Run with custom port
streamlit run app.py --server.port 8080

# Clear Streamlit cache
streamlit cache clear
```

---

## **Architecture**

```
📊 FINMEN Rating Intelligence Engine v2
├── 🎨 Frontend (Streamlit + HTML)
├── 🤖 AI Engines (Peer Matching + Search + Analysis)
├── 💾 Backend (Google Apps Script + Sheets)
└── ⚙️ Config (requirements.txt + .env)
```

---

## **Support**

For issues or questions, check:
- `README.md` - Full documentation
- `FINMEN_V3_SETUP.md` - Detailed setup guide  
- `test_finmen.py` - Validation script
- `DEPLOYMENT_READY.md` - Deployment guide

---

**Status**: ✅ Ready for deployment
**Version**: 2.0.0  
**Last Updated**: Dec 17, 2025
