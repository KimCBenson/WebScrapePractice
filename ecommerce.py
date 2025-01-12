# imports
import requests
import tabulate
from bs4 import BeautifulSoup

URL = "https://webscraper.io/test-sites/e-commerce/allinone"
page = requests.get(URL)

if page.status_code == 200:
    table_data = []

    soup = BeautifulSoup(page.content, 'html.parser') # parsed document
    results = soup.find(class_="wrapper").find(class_="container test-site").find(class_="row").find(class_="col-lg-9").find(class_="row")

    products = results.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")

    for product in products:
        name = product.find("p", class_="description card-text").text.strip()
        price = product.find("h4", class_="price float-end card-title pull-right").text.strip()

        review_count = product.find("p", class_="review-count float-end").text.strip()

        rating = product.find("p", attrs={"data-rating": True})
        rating_value = rating.get("data-rating")

        rating_string = review_count + " - " + rating_value + " stars"

        product = [name, price, rating_string]
        
        table_data.append(product)

    product_table = tabulate.tabulate(table_data, headers=["Product", "Price", "Reviews"], tablefmt="grid")
    print(product_table)
else:
    print("Page not found!")