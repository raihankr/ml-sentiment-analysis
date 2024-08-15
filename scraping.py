from google_play_scraper improt reviews, Sort
import csv

PATH = 'reviews.csv'

scraped_data, token = reviews(
    'com.pinterest',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=15000,
)

with open(PATH, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scraped_data:
        writer.writerow([review['content']])
