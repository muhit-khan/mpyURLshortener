# mpyURLshortener

This is a simple Python script that uses the TinyURL API to shorten a given URL. It prompts the user to enter a URL and then generates a shortened version of it using the TinyURL service.

## Prerequisites
Before running the script, make sure you have the following requirements:

Python 3.x installed on your system.

The requests library. If you don't have it installed, you can install it by running the following command:

`pip install requests`

## Usage
Clone or download this repository to your local machine.

Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script by executing the following command:

`python url_shortener.py`

Enter the URL you want to shorten when prompted.

The script will make a request to the TinyURL API and retrieve the shortened URL. It will then display the shortened link on the console.

### Note: If the request fails or the response status code is not 200, an error message will be displayed.

You can repeat the process by running the script again and entering a new URL.

## License
This project is licensed under the MIT License.

Feel free to use and modify the code as per your needs.