import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def scrape_products_to_csv(url: str, output_csv: str, category_name: str):
    print(f"Подключение к {url}...")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    products_data = []

    product_containers = soup.find_all('article', class_='product_pod')

    print(f"Найдено товаров на странице: {len(product_containers)}")

    for container in product_containers:  
        title_tag = container.find('h3').find('a')
        product_name = title_tag.get('title')
        
       
        price_tag = container.find('p', class_='price_color')
        price = price_tag.text.strip() if price_tag else "N/A"
        
       
        relative_url = title_tag.get('href')
        full_url = urljoin(url, relative_url)

      
        products_data.append({
            'product_name': product_name,
            'price': price,
            'category': category_name,
            'url': full_url
        })

   
    df = pd.DataFrame(products_data)

  
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Успешно сохранено в {output_csv}")

if __name__ == "__main__":
  
    TARGET_URL = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
    OUTPUT_FILE = "products.csv"
    CATEGORY = "Science"

    scrape_products_to_csv(TARGET_URL, OUTPUT_FILE, CATEGORY)
