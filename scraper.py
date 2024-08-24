from google_play_scraper import reviews, Sort
import csv

scraped_data, token = reviews(
    'com.pinterest',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=18000,
)

with open('reviews.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scraped_data:
        writer.writerow([review['content']])