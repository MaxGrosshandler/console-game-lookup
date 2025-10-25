# Console Game Search - Quick Start Guide

## 60-Second Setup

### 1. Install Python
Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python console_game_search.py
```

### 4. Start Searching!
```
Enter a game console name (or 'quit' to exit): Nintendo Switch
```

---

## 30-Second Usage Example

```bash
$ python console_game_search.py
============================================================
   CONSOLE GAME POPULARITY SEARCH
============================================================

Enter a game console name (or 'quit' to exit): PlayStation 5

Searching for the most popular game on PlayStation 5...
------------------------------------------------------------
Result 1:
  Title: Elden Ring
  Info: An action role-playing game developed by FromSoftware...

Result 2:
  Title: Hogwarts Legacy
  Info: A role-playing game set in the Harry Potter universe...

Result 3:
  Title: Final Fantasy XVI
  Info: A fantasy action role-playing game...
------------------------------------------------------------

Enter a game console name (or 'quit' to exit): quit

Thank you for using the Console Game Search!
```

---

## Common Commands

| Task | Command |
|------|---------|
| **Install** | `pip install -r requirements.txt` |
| **Run** | `python console_game_search.py` |
| **Search** | Type console name when prompted |
| **Exit** | Type `quit` and press Enter |
| **New Search** | Just type another console name |

---

## Popular Console Names to Try

- `Nintendo Switch`
- `PlayStation 5`
- `Xbox Series X`
- `PlayStation 4`
- `Xbox One`
- `Nintendo Wii`
- `Super Nintendo`
- `Nintendo 64`

---

## Troubleshooting Quick Fixes

| Problem | Fix |
|---------|-----|
| **"ModuleNotFoundError"** | Run `pip install -r requirements.txt` |
| **No results** | Wait a few minutes (rate limiting), try again |
| **"Timeout" error** | Check internet connection |
| **Empty input error** | Type a console name (don't press Enter empty) |
| **Hanging/Freezing** | Press `Ctrl+C` to stop |

---

## File Guide

```
📄 README.md              → Installation & basic usage
📄 QUICK_START.md         → This file (fast setup)
📄 USER_GUIDE.md          → How to use in detail
📄 ARCHITECTURE.md        → How the app works (technical)
📄 API_REFERENCE.md       → Function documentation
📄 DEVELOPER_GUIDE.md     → How to modify the code

💻 console_game_search.py → The application (main file)
📋 requirements.txt       → Required packages
```

---

## Next Steps

- **New User?** Read [USER_GUIDE.md](./USER_GUIDE.md)
- **Want to modify?** Read [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md)
- **Technical details?** Read [ARCHITECTURE.md](./ARCHITECTURE.md)
- **Full reference?** Read [API_REFERENCE.md](./API_REFERENCE.md)

---

## Requirements

- Python 3.6+
- Internet connection
- 2 packages: `requests` and `beautifulsoup4`

That's it! You're ready to search for popular games. 🎮
