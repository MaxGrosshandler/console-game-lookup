# Console Game Search - API Reference

## Module: `console_game_search`

This module provides functions for searching Google to find the most popular video games for a given gaming console.

---

## Functions

### `search_popular_game(console)`

Searches Google for the most popular video game for a given gaming console.

#### Signature
```python
def search_popular_game(console: str) -> str
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `console` | `str` | Yes | The name of the gaming console (e.g., "PlayStation 5", "Nintendo Switch") |

#### Returns

**Type:** `str`

A formatted string containing search results. The format includes:
- Featured snippets (if available)
- Answer boxes (if available)
- Top 3 search results with titles and descriptions

**Return Examples:**

Success case:
```
Featured Answer: The most popular video game on PlayStation 5 is...
Answer: According to recent data...

Result 1:
  Title: The Last of Us Part II
  Info: An action-adventure game released in 2020...

Result 2:
  Title: Elden Ring
  Info: A role-playing video game developed by FromSoftware...

Result 3:
  Title: FIFA 23
  Info: A sports video game in the FIFA series...
```

Error cases:
```
Error making request: Connection timeout
```
```
Error parsing results: Failed to parse HTML response
```
```
No results found. Google's HTML structure may have changed or the request was blocked.
```

#### Raises

**Does not raise exceptions.** All errors are caught and returned as error messages within the return string.

#### Error Handling

| Error Type | Cause | Return Message |
|------------|-------|----------------|
| `requests.RequestException` | Network error, timeout, invalid URL | `Error making request: {exception}` |
| General `Exception` | HTML parsing failure | `Error parsing results: {exception}` |
| No data found | Google structure changed or blocked | `No results found. Google's HTML structure...` |

#### Implementation Details

**Algorithm:**
1. Construct query string: `"most popular video game for {console}"`
2. URL-encode the query using `urllib.parse.quote()`
3. Build Google search URL: `https://www.google.com/search?q={encoded_query}`
4. Send HTTP GET request with browser User-Agent header
5. Parse response HTML with BeautifulSoup
6. Extract results from three sources (in order):
   - Featured snippet (CSS class: `hgKElc`)
   - Answer box (CSS class: `IZ6rdc`)
   - Search results (CSS class: `g`), limited to top 3
7. Format and return results

**HTTP Request Details:**
- **Method:** GET
- **Timeout:** 10 seconds
- **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36`
- **URL Scheme:** HTTPS

**CSS Selectors Used:**
- Featured snippet: `div.hgKElc`
- Answer box: `div.IZ6rdc`
- Search result container: `div.g`
- Result title: `h3`
- Result snippet: `div.VwiC3b`

#### Limitations

1. **Rate Limiting:** Google may block requests after multiple queries in short time
2. **HTML Structure Dependency:** Changes to Google's HTML structure will break parsing
3. **Results Limit:** Hard-coded to return maximum 3 results
4. **No Caching:** Every call makes a new HTTP request
5. **No Retry Logic:** Failed requests are not retried

#### Example Usage

```python
from console_game_search import search_popular_game

# Search for PlayStation 5
results = search_popular_game("PlayStation 5")
print(results)

# Search for Nintendo Switch
results = search_popular_game("Nintendo Switch")
print(results)

# Search with typos (still works)
results = search_popular_game("xbox")
print(results)
```

#### Performance

| Metric | Value |
|--------|-------|
| Average Response Time | 1-3 seconds |
| Network Calls | 1 per invocation |
| Memory Overhead | ~50-100 MB |

---

### `main()`

The main entry point of the application. Runs an interactive command-line loop for searching games.

#### Signature
```python
def main() -> None
```

#### Parameters

None

#### Returns

**Type:** `None`

This function doesn't return a value; it runs until the user exits.

#### Implementation Details

**Interactive Loop:**
1. Display welcome banner
2. Enter continuous loop:
   - Prompt user for console name with input message: `"Enter a game console name (or 'quit' to exit): "`
   - Strip whitespace from input
   - Check for exit condition: `quit` (case-insensitive)
   - Validate input (must not be empty)
   - Call `search_popular_game()` with console name
   - Display results with formatted separators
   - Display separator line (`-` × 60)
   - Continue to next iteration
3. On exit:
   - Display exit message: `"Thank you for using the Console Game Search!"`
   - Break loop and end program

**Output Format:**

```
============================================================
   CONSOLE GAME POPULARITY SEARCH
============================================================

Enter a game console name (or 'quit' to exit): [USER INPUT]

Searching for the most popular game on [CONSOLE NAME]...
------------------------------------------------------------
[SEARCH RESULTS]
------------------------------------------------------------

Enter a game console name (or 'quit' to exit): [USER INPUT]
...
```

#### Exit Behavior

The function exits when:
- User enters `quit` (case-insensitive)
- User presses Ctrl+C (keyboard interrupt)
- An unhandled exception occurs

#### Example Usage

```python
from console_game_search import main

# Run the interactive application
main()
```

**Interactive Session Example:**
```
$ python console_game_search.py
============================================================
   CONSOLE GAME POPULARITY SEARCH
============================================================

Enter a game console name (or 'quit' to exit): Nintendo Switch
Searching for the most popular game on Nintendo Switch...
------------------------------------------------------------
Result 1:
  Title: The Legend of Zelda: Breath of the Wild
  Info: A legend of the past...
------------------------------------------------------------

Enter a game console name (or 'quit' to exit): quit
Thank you for using the Console Game Search!
```

---

## Data Flow Diagram

```
User Input (Console Name)
        ↓
    main()
        ↓
   Input Validation
   ├─ Empty check
   └─ Exit command check
        ↓
search_popular_game(console)
        ↓
   Query Construction
        ↓
   HTTP GET Request
        ↓
   HTML Parsing
        ↓
   Result Extraction
   ├─ Featured snippets
   ├─ Answer boxes
   └─ Top 3 search results
        ↓
   Result Formatting
        ↓
   Return Formatted String
        ↓
    Display to User
        ↓
   Loop or Exit
```

---

## Error Codes and Messages

### Network Errors

| Message | Cause | Solution |
|---------|-------|----------|
| `Error making request: [connection error details]` | Network issue | Check internet connection |
| `Error making request: HTTPError` | HTTP error (4xx/5xx) | Google may be blocking requests |
| `Error making request: Timeout` | Request took >10 seconds | Try again later or check network |

### Parsing Errors

| Message | Cause | Solution |
|---------|-------|----------|
| `Error parsing results: [parsing error details]` | HTML structure unexpected | Google's page structure may have changed |
| `No results found. Google's HTML structure may have changed...` | CSS selectors don't match | Update CSS selectors in code |

### Input Errors

| Message | Cause | Solution |
|---------|-------|----------|
| `Please enter a valid console name.` | Empty input | Enter a console name and try again |

---

## Debugging Tips

### Enable Request Logging
```python
import logging
import requests

logging.basicConfig(level=logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
```

### Test Direct Request
```python
import requests
import urllib.parse

console = "PlayStation 5"
query = f"most popular video game for {console}"
encoded_query = urllib.parse.quote(query)
url = f"https://www.google.com/search?q={encoded_query}"

response = requests.get(url)
print(f"Status: {response.status_code}")
print(f"Length: {len(response.text)}")
```

### Inspect HTML Structure
```python
from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?q=most+popular+video+game+for+Nintendo+Switch"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all divs with class 'g'
results = soup.find_all('div', class_='g')
print(f"Found {len(results)} results")
```

---

## Dependencies

### Required
- `requests` >= 2.31.0
- `beautifulsoup4` >= 4.12.0
- Python >= 3.6

### Optional (for development)
- `pytest` (for testing)
- `requests-mock` (for mocking HTTP requests)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Initial | Initial release |

---

## Related Documentation

- [README.md](./README.md) - Installation and usage guide
- [ARCHITECTURE.md](./ARCHITECTURE.md) - System architecture and design
- [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md) - Development and contribution guide
