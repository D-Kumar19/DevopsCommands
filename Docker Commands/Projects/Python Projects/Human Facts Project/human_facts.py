import requests

def get_random_human_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url)
        response.raise_for_status()
        fact_data = response.json()
        return fact_data.get("text", "No fact found.")
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    fact = get_random_human_fact()
    print(f"Here's a random fact about humans: {fact}")
