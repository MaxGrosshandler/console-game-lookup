# Console Game Search - Architecture Documentation

## System Overview

The Console Game Search application is a lightweight, single-purpose command-line tool designed to search Google for the most popular video games on specified gaming consoles.

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User (CLI Interface)                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │   main() Function      │
        │  (Interactive Loop)    │
        └──────────┬─────────────┘
                   │
                   ▼
        ┌────────────────────────────────────┐
        │ search_popular_game() Function     │
        │  (Core Search Logic)               │
        └──────────┬───────────────────────┘
                   │
         ┌─────────┴────────────┐
         ▼                      ▼
    ┌─────────────┐     ┌──────────────────┐
    │ Google API  │     │  BeautifulSoup   │
    │  (HTTP)     │     │  (HTML Parser)   │
    └─────────────┘     └──────────────────┘
         │                      │
         └──────────┬───────────┘
                    ▼
            ┌───────────────┐
            │ Search Results│
            │  (Formatted)  │
            └───────────────┘
```

## Component Details

### 1. Main Entry Point: `main()` Function

**Location:** `console_game_search.py:71-99`

**Responsibilities:**
- Manages the application lifecycle
- Handles user input/output
- Controls the interactive loop
- Displays welcome banner and prompts

**Flow:**
```
Start
  ↓
Display Banner
  ↓
Loop Until Quit:
  - Prompt for console name
  - Validate input
  - Call search_popular_game()
  - Display results
  - Continue or exit
  ↓
Exit
```

**Key Features:**
- Input validation (non-empty console names)
- Exit condition: user types 'quit'
- Formatted output with separators
- Continuous operation until user exits

### 2. Core Search Component: `search_popular_game()` Function

**Location:** `console_game_search.py:5-68`

**Responsibilities:**
- Construct Google search queries
- Perform HTTP requests to Google
- Parse HTML response
- Extract relevant game information
- Handle errors gracefully

**Data Flow:**

```
Input: Console Name
  ↓
1. Query Construction
   - Format: "most popular video game for {console}"
   - URL encode the query
   - Build Google search URL
  ↓
2. HTTP Request
   - Browser-like User-Agent header
   - 10-second timeout
   - Error handling for network issues
  ↓
3. HTML Parsing
   - Parse response with BeautifulSoup
   - Look for featured snippets (class 'hgKElc')
   - Look for answer boxes (class 'IZ6rdc')
   - Extract search results (class 'g')
  ↓
4. Data Extraction
   - Extract titles from <h3> tags
   - Extract snippets from 'VwiC3b' class
   - Limit to top 3 results
  ↓
5. Output Formatting
   - Format results with labels
   - Return as readable string
  ↓
Output: Formatted Search Results
```

## Dependencies

### External Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| `requests` | >=2.31.0 | HTTP client for making Google search requests |
| `beautifulsoup4` | >=4.12.0 | HTML parsing and DOM traversal |

### Standard Library

| Module | Purpose |
|--------|---------|
| `urllib.parse` | URL encoding for search queries |

## Data Structures

### Search Result Format

The `search_popular_game()` function returns a formatted string containing:

```
Featured Answer: [featured snippet text if available]
Answer: [answer box text if available]

Result 1:
  Title: [h3 text content]
  Info: [description snippet]

Result 2:
  Title: [h3 text content]
  Info: [description snippet]

Result 3:
  Title: [h3 text content]
  Info: [description snippet]
```

## Error Handling

### Request Errors
- **Type:** `requests.RequestException`
- **Handling:** Return error message with exception details
- **User Message:** "Error making request: {error}"

### Parsing Errors
- **Type:** General `Exception`
- **Handling:** Return error message with exception details
- **User Message:** "Error parsing results: {error}"

### Google Structure Changes
- **Scenario:** HTML structure no longer matches CSS selectors
- **Handling:** Return graceful fallback message
- **User Message:** "No results found. Google's HTML structure may have changed..."

## Configuration

### Hardcoded Settings

| Setting | Value | Notes |
|---------|-------|-------|
| User-Agent | Chrome 91 (Windows) | Prevents blocking by appearing as browser |
| Request Timeout | 10 seconds | Prevents hanging requests |
| Results Limit | 3 results | Limits output to top 3 search results |
| Search Query Format | "most popular video game for {console}" | Standard query template |
| Featured Snippet Selector | `.hgKElc` | CSS class for featured snippets |
| Answer Box Selector | `.IZ6rdc` | CSS class for answer boxes |
| Search Results Selector | `.g` | CSS class for regular search results |
| Title Selector | `h3` | HTML tag for result titles |
| Snippet Selector | `.VwiC3b` | CSS class for result descriptions |

## Design Decisions

### 1. Web Scraping Approach
**Choice:** Direct Google search scraping with BeautifulSoup

**Rationale:**
- No API key required
- Real-time results from Google
- Flexible and adaptable

**Trade-offs:**
- Vulnerable to Google HTML structure changes
- Subject to rate limiting
- May violate Google's Terms of Service

### 2. Single-File Architecture
**Choice:** Monolithic structure with two main functions

**Rationale:**
- Simple and easy to understand
- Minimal dependencies
- Quick to execute

**Limitations:**
- Limited scalability
- No code reusability
- Difficult to test individual components

### 3. Interactive CLI Loop
**Choice:** Continuous prompt-response cycle

**Rationale:**
- User-friendly interface
- Allows multiple searches without restarting
- Clear exit mechanism

**Alternative:** Single-run mode (would require command-line arguments)

## Limitations and Considerations

### Known Issues
1. **Google HTML Structure Fragility**
   - CSS selectors may break if Google changes their page structure
   - No fallback or adaptive parsing strategy
   - Manual updates required to fix parsing

2. **Rate Limiting**
   - No built-in rate limiting or retry logic
   - May get blocked after multiple rapid requests
   - No exponential backoff strategy

3. **Network Dependencies**
   - Requires internet connection
   - 10-second timeout may be insufficient for slow connections
   - No offline functionality

4. **Search Result Limitations**
   - Only shows top 3 results
   - No pagination or filtering
   - No sorting or relevance weighting

### Security Considerations
- User-Agent spoofing may violate Google's TOS
- No HTTPS certificate validation options
- No proxy support for anonymization

## Future Enhancement Opportunities

### Code Structure
- Separate presentation layer (CLI) from business logic
- Add result caching to reduce requests
- Implement logging for debugging
- Add unit and integration tests

### Features
- Support for specific game console generations
- Search result filtering/sorting
- Export results to file (JSON, CSV)
- Search history tracking
- Configuration file for custom queries

### Robustness
- Implement retry logic with exponential backoff
- Add Google HTML structure version detection
- Implement multiple parsing strategies (fallbacks)
- Add proxy rotation support
- Implement rate limiting

### User Experience
- Color-coded output for better readability
- Result caching with refresh option
- Configurable results limit
- Advanced search filters
- Interactive result selection

## Performance Characteristics

| Aspect | Performance |
|--------|-------------|
| Cold Start | ~1-3 seconds (first search request) |
| Subsequent Searches | ~1-3 seconds (network dependent) |
| Memory Usage | ~50-100 MB typical |
| CPU Usage | Minimal (I/O bound) |
| Scalability | Single instance only |

## Deployment

### System Requirements
- Python 3.6+
- Internet connection
- ~100 MB disk space (with dependencies)

### Installation Steps
1. Clone or download the repository
2. Install Python 3.6+
3. Run: `pip install -r requirements.txt`
4. Run: `python console_game_search.py`

### Dependency Installation
```bash
pip install requests>=2.31.0 beautifulsoup4>=4.12.0
```
