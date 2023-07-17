import requests

def fetch_random_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"{quote} - {author}"
    else:
        return "Failed to fetch a quote. Please try again later."

def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        input("Press Enter to get a random quote (or type 'q' to quit): ")
        quote = fetch_random_quote()
        print(f"\n{quote}\n")
        quit_choice = input("Press 'q' to quit or any other key to get another quote: ")
        if quit_choice.lower() == 'q':
            print("Thank you for using the Random Quote Generator!")
            break

if __name__ == "__main__":
    main()
