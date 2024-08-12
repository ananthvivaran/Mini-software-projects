import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch HTML content from a URL
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to parse the HTML and extract product information
def parse_product_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    # Assuming products are in a div with class 'product-item'
    product_elements = soup.find_all('div', class_='product-item')

    for product in product_elements:
        name = product.find('h2', class_='product-title').text.strip()
        price = product.find('span', class_='product-price').text.strip()
        rating = product.find('div', class_='product-rating').text.strip() if product.find('div', class_='product-rating') else 'No rating'
        
        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    return products

# Function to save product information to a CSV file
def save_to_csv(products, filename):
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)

def main():
    url = 'https://www.example.com/products'  # Replace with the actual URL of the product listing page
    html = fetch_html(url)
    
    if html:
        products = parse_product_info(html)
        save_to_csv(products, 'products.csv')
        print("Product information has been saved to 'products.csv'")
    else:
        print("Failed to fetch the webpage.")

if __name__ == "__main__":
    main()
