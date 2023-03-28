from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.findAll('div', id='pagecontent')
    description = ''
    for data in block:
        if data.find('li'):
            description = data.text
    descriprion = description.split('\n')
    description = [line.strip() for line in descriprion if line.strip()]

    return (description)