import json
import sys
import urllib.request

API_URL = "https://v2.jokeapi.dev/joke/Any?type=single,twopart"


def fetch_joke():
    try:
        with urllib.request.urlopen(API_URL) as response:
            if response.status != 200:
                raise RuntimeError(f"API returned status {response.status}")
            data = json.load(response)
            return data
    except Exception as e:
        sys.stderr.write(f"Error fetching joke: {e}\n")
        sys.exit(1)


def display_joke(joke_data):
    if joke_data.get("type") == "single":
        print(joke_data.get("joke"))
    elif joke_data.get("type") == "twopart":
        print(joke_data.get("setup"))
        print(joke_data.get("delivery"))
    else:
        print("Unexpected joke format.")


if __name__ == "__main__":
    joke = fetch_joke()
    display_joke(joke)
