# Console Game Search

A Python program that searches Google for the most popular video game for a given console.

## Features

- Interactive command-line interface
- Searches Google for the most popular game on any console
- Displays multiple search results with titles and descriptions
- Easy-to-use with simple text input

## Installation

1. Make sure you have Python 3.6 or higher installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python console_game_search.py
```

Then enter a game console name when prompted (e.g., "PlayStation 5", "Nintendo Switch", "Xbox Series X").

Type 'quit' to exit the program.

## Example

```
Enter a game console name (or 'quit' to exit): Nintendo Switch

Searching for the most popular game on Nintendo Switch...
------------------------------------------------------------
Result 1:
  Title: The Legend of Zelda: Breath of the Wild
  Info: One of the highest-rated games on Nintendo Switch...
------------------------------------------------------------
```

## Notes

- This program scrapes Google search results, which may be subject to rate limiting
- Google's HTML structure may change over time, which could affect result parsing
- Use responsibly and in accordance with Google's Terms of Service
