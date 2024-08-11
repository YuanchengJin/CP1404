import wikipedia


def get_wikipedia_info():
    while True:
        query = input("Enter page title: ").strip()
        if not query:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(query, auto_suggest=False)
            print(f"\n{page.title}")
            print(f"{page.summary[:471]}")

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle ambiguous terms by providing a list of possible matches
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            # Handle cases where no page matches the query
            print(f'Page id "{query}" does not match any pages. Try another id!')

        except Exception as e:
            # Handle any other exceptions that might occur
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_wikipedia_info()
