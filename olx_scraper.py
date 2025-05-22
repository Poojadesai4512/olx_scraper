import requests
from bs4 import BeautifulSoup
import csv

print("Starting scraper...")

url = "https://www.olx.in/items/q-car-cover"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)  # Check if the request succeeded

soup = BeautifulSoup(response.text, 'html.parser')

with open("car_covers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location", "Link"])

    for item in soup.select("li.EIR5N"):
        title = item.select_one("span._2tW1I")
        price = item.select_one("span._89yzn")
        location = item.select_one("span._2FcKX")
        link = item.select_one("a")

        writer.writerow([
            title.text.strip() if title else "N/A",
            price.text.strip() if price else "N/A",
            location.text.strip() if location else "N/A",
            "https://www.olx.in" + link["href"] if link else "N/A"
        ])

print("Done. Results saved to car_covers.csv")