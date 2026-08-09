# Demo #1 — Website → CSV

**URL** → **Python (`requests`)** → **Scraping (`BeautifulSoup`)** → **Pandas DataFrame** → **CSV**

The script collects public data about products (books) from the demo site and structures them for further analysis.

## Example

**Input:**
`http://books.toscrape.com/catalogue/category/books/science_22/index.html`

**Output (`products.csv`):**
```csv
product_name,price,category,url
"The Most Perfect Thing: Inside (and Outside) a Bird's Egg",£42.96,Science,[http://books.toscrape.com/catalogue/the-most-perfect-thing-inside-and-outside-a-birds-egg_939/index.html](http://books.toscrape.com/catalogue/the-most-perfect-thing-inside-and-outside-a-birds-egg_939/index.html)
"Immunity: How Elie Metchnikoff Changed the Course of Modern Medicine",£57.36,Science,[http://books.toscrape.com/catalogue/immunity-how-elie-metchnikoff-changed-the-course-of-modern-medicine_900/index.html](http://books.toscrape.com/catalogue/immunity-how-elie-metchnikoff-changed-the-course-of-modern-medicine_900/index.html)
"Sorting the Beef from the Bull: The Science of Food Fraud Forensics",£44.74,Science,[http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html](http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html)
