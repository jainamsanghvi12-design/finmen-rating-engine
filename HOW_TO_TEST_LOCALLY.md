# 💻 How to Test FINMEN on Your Laptop

## **FOR WINDOWS USERS**

### **Step 1: Open Terminal (Command Prompt)**

**Method 1 (Easiest):**
1. Press: `Windows Key + R` (hold down Windows button, press R)
2. Type: `cmd`
3. Press: `Enter`
4. ✅ Black terminal window opens

**Method 2 (Alternative):**
1. Click Windows button (bottom left)
2. Search for: `Command Prompt`
3. Click on it
4. ✅ Terminal opens

**Method 3 (PowerShell - Modern):**
1. Right-click on Desktop
2. Select: `Open PowerShell window here`
3. ✅ PowerShell opens

### **Step 2: Navigate to Project Folder**

```cmd
cd Downloads\finmen-rating-engine
```

Or if you saved it somewhere else:
```cmd
cd C:\Users\YourName\Documents\finmen-rating-engine
```

💡 **Tip:** Drag the folder into terminal and it shows the path!

### **Step 3: Check if Python is Installed**

```cmd
python --version
```

You should see: `Python 3.8.0` or higher ✅

If NOT installed, download from: https://www.python.org/downloads

### **Step 4: Install Dependencies**

```cmd
pip install -r requirements.txt
```

⏳ This takes 2-3 minutes...  
✅ When done, you see: `Successfully installed`

### **Step 5: Run Tests**

```cmd
python test_finmen.py
```

✅ You'll see colorful output with ✓ PASS or ✗ FAIL

### **Step 6: Start the App**

```cmd
streamlit run app.py
```

✅ Wait for: `Local URL: http://localhost:8501`  
✅ Browser opens automatically

If not, copy & paste: `http://localhost:8501` in browser

---

## **FOR MAC USERS**

### **Step 1: Open Terminal**

**Method 1 (Easiest):**
1. Press: `Cmd + Space` (Command + Spacebar)
2. Type: `terminal`
3. Press: `Enter`
4. ✅ Terminal opens

**Method 2 (Finder):**
1. Open Finder
2. Go to: Applications → Utilities
3. Double-click: Terminal
4. ✅ Terminal opens

### **Step 2: Navigate to Project**

```bash
cd ~/Downloads/finmen-rating-engine
```

Or drag folder into terminal:
```bash
cd " drag folder here "
```

### **Step 3: Check Python**

```bash
python3 --version
```

Should show: `Python 3.8.0` or higher ✅

### **Step 4: Install Dependencies**

```bash
pip3 install -r requirements.txt
```

⏳ Wait 2-3 minutes...  
✅ Done when you see: `Successfully installed`

### **Step 5: Run Tests**

```bash
python3 test_finmen.py
```

✅ See colorful output with ✓ or ✗

### **Step 6: Start App**

```bash
streamlit run app.py
```

✅ Browser opens at: `http://localhost:8501`

---

## **TROUBLESHOOTING**

### **"Command not found: python"**
- **Windows:** Use `python` (not `python3`)
- **Mac:** Use `python3` (with the 3)
- Or download Python: https://www.python.org/downloads

### **"pip not found"**
- **Windows:** Use `pip` or `python -m pip install -r requirements.txt`
- **Mac:** Use `pip3` or `python3 -m pip install -r requirements.txt`

### **"Module not found" errors**
- Run: `pip install -r requirements.txt` again
- Make sure you're in correct folder (has `app.py` file)

### **Port 8501 already in use**
- Run on different port:
  ```bash
  streamlit run app.py --server.port 8080
  ```

### **Browser doesn't open**
- Manually go to: `http://localhost:8501`
- Or copy link from terminal

---

## **WHAT TO EXPECT**

When app starts, you'll see:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
```

Then browser shows:
- 📝 **Input Tab** - Submit test rating
- 📊 **View Data Tab** - See submissions
- 🔍 **Analysis Tab** - View peer matches

---

## **TEST WORKFLOW**

1. **Go to Input Tab**
2. **Fill in test data:**
   - Company: "Test Company"
   - Agency: "CRISIL"
   - Industry: "Banking"
   - Rating: "AA"
   - Outlook: "Stable"
   - Action: "Initial Rating"
   - Rationale: "Test rationale text"
3. **Click: "Submit Rationale"**
4. **Go to View Data Tab**
   - ✅ See your submission in table
5. **Go to Analysis Tab**
   - ✅ See peer matches
   - ✅ See charts

---

## **STOP THE APP**

In terminal: Press `Ctrl + C` (hold Ctrl, press C)

```
KeyboardInterrupt
Exited with code 0
```

✅ App stops safely

---

## **RUN AGAIN**

Next time just open terminal and run:

```bash
streamlit run app.py
```

You don't need to reinstall dependencies!

---

## **QUICK CHEAT SHEET**

| Task | Windows | Mac |
|------|---------|-----|
| Open Terminal | `Win + R` → `cmd` | `Cmd + Space` → `terminal` |
| Navigate Folder | `cd path` | `cd path` |
| Check Python | `python --version` | `python3 --version` |
| Install Packages | `pip install -r requirements.txt` | `pip3 install -r requirements.txt` |
| Run Tests | `python test_finmen.py` | `python3 test_finmen.py` |
| Start App | `streamlit run app.py` | `streamlit run app.py` |
| Stop App | `Ctrl + C` | `Ctrl + C` |

---

## **STILL STUCK?**

Check these files for more help:
- `QUICK_START.md` - 5-minute overview
- `README.md` - Full documentation
- `test_finmen.py` - Validation script

---

**You got this! 🚀**
