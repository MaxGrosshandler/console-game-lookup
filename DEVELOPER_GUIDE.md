# Console Game Search - Developer Guide

This guide provides information for developers who want to understand, modify, or extend the Console Game Search application.

## Table of Contents

1. [Setting Up Development Environment](#setting-up-development-environment)
2. [Project Structure](#project-structure)
3. [Code Overview](#code-overview)
4. [Understanding the Code](#understanding-the-code)
5. [Making Changes](#making-changes)
6. [Testing](#testing)
7. [Common Tasks](#common-tasks)
8. [Contributing Guidelines](#contributing-guidelines)
9. [Troubleshooting](#troubleshooting)

## Setting Up Development Environment

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Git (for version control)
- A text editor or IDE (VS Code, PyCharm, etc.)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ConsoleGameSales
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python console_game_search.py
   ```

### Optional Development Tools

```bash
# For testing
pip install pytest pytest-cov

# For code quality
pip install pylint flake8 black

# For type checking
pip install mypy

# For mocking HTTP requests in tests
pip install requests-mock
```

## Project Structure

```
ConsoleGameSales/
├── console_game_search.py    # Main application file (104 lines)
├── requirements.txt          # Python dependencies
├── README.md                 # User-facing documentation
├── ARCHITECTURE.md           # Architecture and design documentation
├── API_REFERENCE.md          # Function reference documentation
├── DEVELOPER_GUIDE.md        # This file
├── .git/                     # Git repository
└── .gitignore               # Git ignore rules (if present)
```

### File Descriptions

| File | Purpose | Lines |
|------|---------|-------|
| `console_game_search.py` | Main application containing all logic | 104 |
| `requirements.txt` | Package dependencies for installation | 2 |
| `README.md` | User installation and usage guide | 51 |
| `ARCHITECTURE.md` | System design and architecture | Comprehensive |
| `API_REFERENCE.md` | Function signatures and documentation | Comprehensive |
| `DEVELOPER_GUIDE.md` | Development and contribution guide | This file |

## Code Overview

### Main Components

**File:** `console_game_search.py`

#### Imports Section (Lines 1-3)
```python
import requests                 # HTTP requests library
from bs4 import BeautifulSoup   # HTML parsing library
import urllib.parse             # URL encoding utility
```

#### Function 1: `search_popular_game()` (Lines 5-68)
- **Purpose:** Core search functionality
- **Input:** Console name (string)
- **Output:** Formatted search results (string)
- **Key Operations:**
  - Query construction
  - HTTP request to Google
  - HTML parsing
  - Result extraction
  - Error handling

#### Function 2: `main()` (Lines 71-99)
- **Purpose:** Interactive command-line interface
- **Input:** User console names from stdin
- **Output:** Formatted results to stdout
- **Key Operations:**
  - Welcome banner display
  - Input validation
  - Search coordination
  - Output formatting
  - Exit handling

#### Entry Point (Lines 102-103)
```python
if __name__ == "__main__":
    main()
```

## Understanding the Code

### Key Concepts

#### 1. URL Encoding
The application uses `urllib.parse.quote()` to properly encode search queries into URLs:
```python
query = f"most popular video game for {console}"
encoded_query = urllib.parse.quote(query)
url = f"https://www.google.com/search?q={encoded_query}"
```

#### 2. Browser Spoofing
A realistic User-Agent header is sent to prevent Google from blocking the request:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...'
}
```

#### 3. HTML Parsing
BeautifulSoup is used to find specific CSS classes in the HTML:
```python
featured_snippet = soup.find('div', class_='hgKElc')  # Find by CSS class
results = soup.find_all('div', class_='g')             # Find all matches
```

#### 4. Error Handling
All errors are caught and converted to user-friendly messages:
```python
try:
    response = requests.get(url, headers=headers, timeout=10)
    # ... parsing ...
except requests.RequestException as e:
    return f"Error making request: {e}"
except Exception as e:
    return f"Error parsing results: {e}"
```

### Data Flow

```
User enters "PlayStation 5"
         ↓
main() processes input
         ↓
search_popular_game("PlayStation 5") called
         ↓
Query constructed: "most popular video game for PlayStation 5"
         ↓
URL encoded and sent to Google
         ↓
HTML response received
         ↓
BeautifulSoup parses HTML
         ↓
Results extracted using CSS selectors
         ↓
Results formatted as string
         ↓
Results returned to main()
         ↓
Results displayed to user
```

## Making Changes

### Modifying Search Query Format

**Location:** `console_game_search.py`, line 16

**Current:**
```python
query = f"most popular video game for {console}"
```

**Example - Search for best games:**
```python
query = f"best video games for {console}"
```

### Changing Results Limit

**Location:** `console_game_search.py`, line 50

**Current:**
```python
for i, result in enumerate(search_results[:3], 1):
```

**Example - Get top 5 results:**
```python
for i, result in enumerate(search_results[:5], 1):
```

### Updating CSS Selectors

If Google changes their HTML structure, update these selectors:

**Featured Snippet:** Line 37
```python
featured_snippet = soup.find('div', class_='hgKElc')
```

**Answer Box:** Line 42
```python
answer_box = soup.find('div', class_='IZ6rdc')
```

**Search Results:** Line 47
```python
search_results = soup.find_all('div', class_='g')
```

**Result Title:** Line 51
```python
title = result.find('h3')
```

**Result Snippet:** Line 52
```python
snippet = result.find('div', class_='VwiC3b')
```

### Adjusting Request Timeout

**Location:** `console_game_search.py`, line 27

**Current (10 seconds):**
```python
response = requests.get(url, headers=headers, timeout=10)
```

**For slower connections (30 seconds):**
```python
response = requests.get(url, headers=headers, timeout=30)
```

### Adding Logging

**Example - Log search queries and results:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search_popular_game(console):
    logger.info(f"Searching for console: {console}")
    # ... rest of function ...
    logger.info(f"Found {len(results)} results")
    return "\n".join(results)
```

## Testing

### Manual Testing

**Test 1: Basic Search**
```bash
python console_game_search.py
# Enter: Nintendo Switch
# Expected: Results about Nintendo Switch games
```

**Test 2: Multiple Searches**
```bash
python console_game_search.py
# Enter: PlayStation 5
# Enter: Xbox Series X
# Enter: quit
```

**Test 3: Edge Cases**
```bash
python console_game_search.py
# Enter: (empty - should show error)
# Enter: A very obscure console name
# Enter: quit
```

### Automated Testing Example

**File:** `test_console_game_search.py`
```python
import pytest
import requests_mock
from console_game_search import search_popular_game

def test_search_popular_game_success():
    """Test successful search"""
    with requests_mock.Mocker() as m:
        html = '''
        <html>
            <div class="g">
                <h3>Test Game 1</h3>
                <div class="VwiC3b">Great game for console</div>
            </div>
        </html>
        '''
        m.get('https://www.google.com/search?q=most+popular+video+game+for+test', text=html)

        result = search_popular_game("test")
        assert "Test Game 1" in result
        assert "Great game for console" in result

def test_search_popular_game_network_error():
    """Test network error handling"""
    with requests_mock.Mocker() as m:
        m.get('https://www.google.com/search?q=most+popular+video+game+for+test',
              exc=requests.RequestException)

        result = search_popular_game("test")
        assert "Error making request" in result

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

**Run tests:**
```bash
pytest test_console_game_search.py -v
```

## Common Tasks

### Task 1: Add Rate Limiting

```python
import time
from functools import wraps

last_request_time = 0

def rate_limited(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global last_request_time
        elapsed = time.time() - last_request_time
        if elapsed < 2:  # Minimum 2 seconds between requests
            time.sleep(2 - elapsed)
        last_request_time = time.time()
        return func(*args, **kwargs)
    return wrapper

@rate_limited
def search_popular_game(console):
    # ... existing code ...
```

### Task 2: Add Result Caching

```python
cache = {}

def search_popular_game(console):
    # Check cache first
    if console in cache:
        return cache[console]

    # ... existing search code ...

    # Store in cache
    cache[console] = "\n".join(results)
    return cache[console]
```

### Task 3: Add Retry Logic

```python
def search_popular_game(console, max_retries=3):
    for attempt in range(max_retries):
        try:
            # ... existing request code ...
            return "\n".join(results)
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                return f"Error making request: {e}"
```

### Task 4: Add Output to File

```python
def main():
    log_file = open("search_log.txt", "a")

    while True:
        console = input("Enter a game console name (or 'quit' to exit): ").strip()

        if console.lower() == 'quit':
            break

        results = search_popular_game(console)
        print(results)

        # Log to file
        log_file.write(f"Console: {console}\n")
        log_file.write(f"{results}\n")
        log_file.write("-" * 60 + "\n")

    log_file.close()
```

## Contributing Guidelines

### Code Style

- Follow PEP 8 Python style guide
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and single-purpose

### Commit Messages

```
Format: [Type] Brief description

Types:
- [Feature] New functionality
- [Fix] Bug fixes
- [Refactor] Code improvements
- [Docs] Documentation changes
- [Test] Test additions

Example:
[Feature] Add caching for search results
[Fix] Handle Google HTML structure changes
[Docs] Update API reference
```

### Pull Request Process

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make changes and test them
3. Commit with meaningful messages
4. Push to your fork: `git push origin feature/my-feature`
5. Create a pull request with description
6. Address review comments
7. Wait for approval and merge

## Troubleshooting

### Problem: "No results found. Google's HTML structure may have changed..."

**Cause:** Google updated their page structure

**Solution:**
1. Open Google in browser and inspect the HTML
2. Find new CSS class names for results
3. Update selectors in `console_game_search.py`

### Problem: "Connection timeout" or "Error making request"

**Cause:** Network issue or Google blocking requests

**Solution:**
1. Check internet connection
2. Wait a few minutes before trying again
3. Try from a different network
4. Implement retry logic with delays

### Problem: Empty results

**Cause:** No results for the search query

**Solution:**
1. Try a different console name
2. Check if spelling is correct
3. Try a more specific query

### Problem: Import error for requests or BeautifulSoup

**Cause:** Dependencies not installed

**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: Script runs but doesn't respond to input

**Cause:** Hanging on network request

**Solution:**
1. Press Ctrl+C to cancel
2. Check internet connection
3. Increase timeout value in code
4. Check if Google is blocking requests

## Performance Optimization

### Reduce Memory Usage
- Implement generator patterns for large result sets
- Use streaming for large HTTP responses

### Improve Response Time
- Add caching to avoid duplicate requests
- Implement concurrent requests for multiple searches
- Use connection pooling

### Reduce Network Load
- Implement rate limiting between requests
- Add request result compression
- Use regional Google servers

## Security Considerations

### Current Implementation
- No sensitive data handling
- No user authentication required
- Limited to read-only Google searches
- No credentials stored

### Best Practices
- Don't store search history with personal data
- Respect Google's Terms of Service
- Implement rate limiting to avoid abuse
- Don't use for bulk data scraping

## Further Reading

- [Python Requests Library](https://requests.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Google's Web Scraping Guidelines](https://support.google.com/webmasters)
