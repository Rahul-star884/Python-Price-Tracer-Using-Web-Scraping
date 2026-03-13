Price Tracer (Web Scraping Assignment)

This project is a simple Python program that tracks the price of a product from a website using web scraping.

The script sends a request to a product page, extracts the product price from the HTML content, converts it into a numeric value, and compares it with a target price.

If the product price is lower than the target price, the program prints a message saying that the price is good. Otherwise, it shows that the price is higher than expected.

Libraries used in this project:

- requests
- BeautifulSoup (bs4)

How the program works:

1. The script sends an HTTP request to the product page.
2. It reads the HTML content of the page.
3. BeautifulSoup is used to find the product price element.
4. The price text is cleaned and converted into a number.
5. The actual price is compared with the target price.
6. A message is printed in the terminal.

How to run the program:

1. Install required libraries:
   pip install requests
   pip install beautifulsoup4

2. Run the script:
   python price_tracer.py

Example output:

Price on website: £51.77
Actual price: 51.77
Price is good!

This project demonstrates basic web scraping, HTML parsing, and simple conditional logic in Python.
