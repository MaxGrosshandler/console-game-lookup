import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_popular_game(console):
    """
    Search Google for the most popular video game for a given console.

    Args:
        console (str): The name of the game console

    Returns:
        str: Information about the most popular game
    """
    # Construct the search query
    query = f"most popular video game for {console}"
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded_query}"

    # Set up headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Make the request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to find the featured snippet or answer box
        results = []

        # Look for featured snippet
        featured_snippet = soup.find('div', class_='hgKElc')
        if featured_snippet:
            results.append(f"Featured Answer: {featured_snippet.get_text(strip=True)}")

        # Look for answer box
        answer_box = soup.find('div', class_='IZ6rdc')
        if answer_box:
            results.append(f"Answer: {answer_box.get_text(strip=True)}")

        # Get regular search results
        search_results = soup.find_all('div', class_='g')

        if search_results:
            for i, result in enumerate(search_results[:3], 1):
                title = result.find('h3')
                snippet = result.find('div', class_='VwiC3b')

                if title:
                    results.append(f"\nResult {i}:")
                    results.append(f"  Title: {title.get_text(strip=True)}")
                    if snippet:
                        results.append(f"  Info: {snippet.get_text(strip=True)}")

        if results:
            return "\n".join(results)
        else:
            return "No results found. Google's HTML structure may have changed or the request was blocked."

    except requests.RequestException as e:
        return f"Error making request: {e}"
    except Exception as e:
        return f"Error parsing results: {e}"


def main():
    """
    Main function to run the console game search program.
    """
    print("=" * 60)
    print("   CONSOLE GAME POPULARITY SEARCH")
    print("=" * 60)
    print()

    while True:
        # Get user input
        console = input("Enter a game console name (or 'quit' to exit): ").strip()

        if console.lower() == 'quit':
            print("\nThank you for using the Console Game Search!")
            break

        if not console:
            print("Please enter a valid console name.\n")
            continue

        print(f"\nSearching for the most popular game on {console}...")
        print("-" * 60)

        # Perform the search
        results = search_popular_game(console)
        print(results)
        print("-" * 60)
        print()


if __name__ == "__main__":
    main()
