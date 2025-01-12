from bs4 import BeautifulSoup
import requests
import csv

print("Enter the link of the Amazon Product.")
link=input()
source = requests.get(link).text

soup = BeautifulSoup(source , 'lxml')

csv_file = open('Amazon_reviews.csv' , 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['usr_name','rating','rev_date','review'])

for data in soup.find_all(class_ = 'review aok-relative'):

    Username = data.find('div' , class_='a-row a-spacing-mini').text
    print(Username)

    rating = data.find('span' , class_='a-icon-alt').text
    print(rating)

    Date = data.find('span', class_='a-size-base a-color-secondary review-date').text
    print(Date)

    review = data.find('span', class_='a-size-base review-text').text
    print(review)

    print()
    csv_writer.writerow([Username,rating,Date,review])

csv_file.close()
