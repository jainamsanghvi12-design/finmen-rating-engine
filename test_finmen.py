"""FINMEN Testing Suite - Validate all components before deployment
Run this script: python test_finmen.py
"""

import sys
import os
from datetime import datetime

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

test_results = {
    'passed': 0,
    'failed': 0,
    'warnings': 0
}

def print_header(text):
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}{text.center(60)}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")

def print_test(test_name, status, message=""):
    if status == "PASS":
        print(f"{GREEN}PASS{RESET}: {test_name}")
        test_results['passed'] += 1
    elif status == "FAIL":
        print(f"{RED}FAIL{RESET}: {test_name}")
        if message:
            print(f"  {RED}Error: {message}{RESET}")
        test_results['failed'] += 1
    elif status == "WARN":
        print(f"{YELLOW}WARN{RESET}: {test_name}")
        if message:
            print(f"  {YELLOW}Warning: {message}{RESET}")
        test_results['warnings'] += 1

def print_summary():
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}TEST SUMMARY{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{GREEN}Passed: {test_results['passed']}{RESET}")
    print(f"{RED}Failed: {test_results['failed']}{RESET}")
    print(f"{YELLOW}Warnings: {test_results['warnings']}{RESET}")
    total = test_results['passed'] + test_results['failed'] + test_results['warnings']
    print(f"{BOLD}Total Tests: {total}{RESET}\n")

# TEST 1: Python & Environment Setup
print_header("TEST 1: Environment Validation")
try:
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 8:
        print_test("Python Version Check", "PASS", f"Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print_test("Python Version Check", "FAIL", f"Requires Python 3.8+, found {python_version.major}.{python_version.minor}")
except Exception as e:
    print_test("Python Version Check", "FAIL", str(e))

# TEST 2: Check Required Files
print_header("TEST 2: Project Structure Validation")
required_files = [
    'app.py',
    'peer_matcher.py',
    'search_engine.py',
    'requirements.txt',
    'index.html'
]

for file in required_files:
    if os.path.exists(file):
        print_test(f"File Exists: {file}", "PASS")
    else:
        print_test(f"File Exists: {file}", "FAIL", f"{file} not found in project root")

# TEST 3: Check Dependencies
print_header("TEST 3: Dependency Check")
required_packages = ['streamlit', 'google']

for package in required_packages:
    try:
        __import__(package)
        print_test(f"Package Installed: {package}", "PASS")
    except ImportError:
        print_test(f"Package Installed: {package}", "FAIL", f"Run: pip install -r requirements.txt")

# TEST 4: Peer Matcher Module
print_header("TEST 4: Peer Matcher Module")
try:
    from peer_matcher import PeerMatcher
    matcher = PeerMatcher()
    print_test("PeerMatcher Import", "PASS")
    print_test("PeerMatcher Initialization", "PASS")
except Exception as e:
    print_test("PeerMatcher Module", "FAIL", str(e))

# TEST 5: Search Engine Module
print_header("TEST 5: Search Engine Module")
try:
    from search_engine import SearchEngine
    search = SearchEngine()
    print_test("SearchEngine Import", "PASS")
    print_test("SearchEngine Initialization", "PASS")
except Exception as e:
    print_test("SearchEngine Module", "FAIL", str(e))

# TEST 6: Streamlit App
print_header("TEST 6: Streamlit Application")
try:
    with open('app.py', 'r') as f:
        app_content = f.read()
        if 'streamlit' in app_content:
            print_test("App.py Contains Streamlit", "PASS")
        else:
            print_test("App.py Contains Streamlit", "FAIL")
except Exception as e:
    print_test("App.py Check", "FAIL", str(e))

# TEST 7: Configuration Files
print_header("TEST 7: Configuration Files")
config_files = ['.env.example', '.env.production', 'requirements.txt']
for config in config_files:
    if os.path.exists(config):
        print_test(f"Config File: {config}", "PASS")
    else:
        print_test(f"Config File: {config}", "WARN", f"Optional: {config} not found")

print_summary()

if test_results['failed'] > 0:
    print(f"{RED}TESTING FAILED - Fix errors and re-run{RESET}\n")
    sys.exit(1)
else:
    print(f"{GREEN}ALL TESTS PASSED - Ready for deployment!{RESET}\n")
    sys.exit(0)
