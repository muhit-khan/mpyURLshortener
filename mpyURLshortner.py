import requests

# Get user input for the URL
url = input("\nEnter the URL to shorten: ")

def url_shortener(url):
    response = requests.get('http://tinyurl.com/api-create.php?url={}'.format(url))

    if response.status_code == 200:
        short_url = response.text
        print(f"\nShortened Link: {short_url}")
    else:
        print('\nFailed to retrieve the Shortened URL.')

# Call the function
url_shortener(url)
