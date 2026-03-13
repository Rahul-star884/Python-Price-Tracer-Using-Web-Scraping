import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

target_price = 60.0

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    price_text = soup.find("p", class_="price_color").text
    print("Price found on website:", price_text)

    actual_price = float(price_text.replace("£", "").replace("Â", "").strip())
    print("Actual price:", actual_price)

    if actual_price < target_price:
        print("Price is good!")
    else:
        print("Price is too high")

except requests.exceptions.RequestException as e:
    print("Error while opening website:", e)

except Exception as e:
    print("Error while reading price:", e)