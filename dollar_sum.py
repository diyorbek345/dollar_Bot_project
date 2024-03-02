import requests
from bs4 import BeautifulSoup
import fake_useragent

link = 'https://bank.uz/uz/currency/dollar-ssha'
user = fake_useragent.UserAgent().random
header = {'user-agent': user}

responce = requests.get(url=link,headers=header).text
soup = BeautifulSoup(responce,'lxml')

purchase = soup.find('div', class_='bc-inner-block-left')
cell = soup.find('div', class_='bc-inner-blocks-right')

purchase_bank_name = purchase.find_all('div',class_='bc-inner-block-left-text')
purcahse_bank_price = purchase.find_all('span', class_='green-date')

cell_bank_name = cell.find_all('div',class_='bc-inner-block-left-text')
cell_bank_price = cell.find_all('span', class_='green-date')


for i in range(len(cell_bank_name)):
    cell_bank_name[i] = cell_bank_name[i].find('span','medium-text')


for i in range(len(purchase_bank_name)):
    purchase_bank_name[i] = purchase_bank_name[i].find('span','medium-text')

def html_text(arr:list) -> list:
    for i in range(len(arr)):
        arr[i] = arr[i].text.replace('\n','')
    return arr

def data_in_dict(arr1:list,arr2:list)-> dict:
    # arr1 lenghts should be equal arr2
    dict = {}
    for i in range(len(arr1)):
        dict.update({arr1[i] : arr2[i]})
    return dict

html_text(purchase_bank_name)
html_text(purcahse_bank_price)
html_text(cell_bank_name)
html_text(cell_bank_price)

purchase_data = data_in_dict(purchase_bank_name,purcahse_bank_price)
cell_data =data_in_dict(cell_bank_name,cell_bank_price)
