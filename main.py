from bs4 import BeautifulSoup
import requests
def parse():
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', class_='pagecontent') # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег <p>
            description = data.text # записываем в переменную содержание тега

    print(description)
parse()