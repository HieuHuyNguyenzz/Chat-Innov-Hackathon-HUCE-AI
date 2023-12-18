from selenium import webdriver
import pandas as pd
import csv
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrapping_tgdd():
    url = 'https://www.thegioididong.com/laptop-hp-compaq#c=44&m=1470,37208,36246,32230,29176,32075,120,122,128,119,118,203,133&o=17&pi=13' 
    s = Service("C:\\Users\\huyhi\\Downloads\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    page_source = BeautifulSoup(driver.page_source)
    laptop_list = page_source.find_all('a',attrs={'class':'main-contain', 'data-box':'BoxCateFilter'})
    link_list = []
    for laptop in laptop_list:
        laptop_link = laptop.get('href')
        if laptop_link not in link_list:
            link_list.append('https://www.thegioididong.com' + laptop_link)

    names  = [] # tên sản phẩm
    old_prices = [] # giá cũ 
    present_prices = [] # giá hiện tại
    discounts = [] # giảm giá
    due_discounts = [] # hạn giảm giá
    configs = []
    trademarks = [] # Thương hiệu
    series = []    # Dòng sản phẩm
    links = [] # links sản phẩm

    for link in link_list[:]:
        driver.get(link)
        sleep(10)
        page_source = BeautifulSoup(driver.page_source)
        try:
            #Lấy tên sản phẩm
            name = page_source.find('section', attrs={'data-cate-id':'44','class':'detail'}).find('h1').get_text().strip()
            
            #Lấy giá gốc của sản phẩm
            old_price = page_source.find('p',class_='box-price-old').get_text().strip() 
            
            #Lấy giá đã giảm của sản phẩm
            present_price = page_source.find('p',class_='box-price-present').get_text().strip() 
            
            #Lấy phần trăm discount của sản phẩm
            percent = page_source.find('p',class_='box-price-percent')
            discount = 'empty'
            if percent == None :
                discount = 'empty'
            else:
                discount = percent.get_text().strip()
                
            #Lấy hạn giảm giá
            due_discount = ' '.join(page_source.find('div', class_='pr-top').find('i',class_='pr-txt').get_text().strip().split(' ')[-3:])
            
            #Lấy tên thương hiệu
            trademark = page_source.find('section', attrs={'data-cate-id':'44','class':'detail'}).find_all('li')[1].get_text().strip().split(' ')[1]
            
            #Lấy dòng sản phẩm
            temp = name.split(' ')
            serie = temp[temp.index(trademark) + 1]
            
            #Lấy thông số sản phẩm
            config = page_source.find('div', class_='parameter')
            parameter_list = []
            ul_element = config.find('ul', class_='parameter__list')
            for li_element in ul_element.find_all('li'):
                parameter_list.append(li_element.find('div', class_='liright').text.strip())
            #Thêm các giá trị vào list tương ứng nếu không có lỗi
            names.append(name)
            old_prices.append(old_price)
            present_prices.append(present_price)
            discounts.append(discount)
            due_discounts.append(due_discount)
            configs.append(parameter_list)
            trademarks.append(trademark)
            series.append(serie)
            links.append(link)
            
        except :
            pass

    data = {'name' : names,\
        'old_price' : old_prices,\
        'present_price' : present_prices,\
        'discount' : discounts,\
        'due_discount' : due_discounts,\
        'config' : configs,\
        'trademark' : trademarks,\
        'series' : series,\
        'link' : links
    }
    df = pd.DataFrame(data)
    return df
    
def scrapping_anphat():
    i = 1
    url = 'https://www.anphatpc.com.vn/may-tinh-xach-tay-laptop.html?other_filter=in-stock&page='
    s = Service("C:\\Users\\huyhi\\Downloads\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get(url+str(i))
    page_source = BeautifulSoup(driver.page_source)

    link_list = []

    while True:
        i+=1
        laptop_list = page_source.find_all('a',attrs={'class':'p-img'})
        #print(laptop_list)
        for laptop in laptop_list:
            laptop_link = laptop.get('href')
            if laptop_link not in link_list:
                link_list.append('https://www.https://www.anphatpc.com.vn/' + laptop_link)
        if page_source.find('a','href'=='url'+str(i)) != None:
            driver = webdriver.Chrome(service=s)
            driver.get(url+str(i))
            page_source = BeautifulSoup(driver.page_source)
        else:
            break
    
    names  = []
    old_prices = []
    present_prices = []
    discounts = []
    due_discounts = []
    types = []   # Loại thiết bị
    trademarks = [] # Thương hiệu
    series = []    # Dòng sản phẩm
    links = []
    configs = []

    for link in link_list[:]:
        driver.get(link)
        sleep(10)
        page_source = BeautifulSoup(driver.page_source)
        try:
                #Lấy tên sản phẩm
                name = page_source.find('section', attrs={'data-cate-id':'44','class':'detail'}).find('h1').get_text().strip()
                
                #Lấy giá gốc của sản phẩm
                old_price = page_source.find('p',class_='box-price-old').get_text().strip() 
                
                #Lấy giá đã giảm của sản phẩm
                present_price = page_source.find('p',class_='box-price-present').get_text().strip() 
                
                #Lấy phần trăm discount của sản phẩm
                percent = page_source.find('p',class_='box-price-percent')
                discount = 'empty'
                if percent == None :
                    discount = 'empty'
                else:
                    discount = percent.get_text().strip()
                    
                #Lấy hạn giảm giá
                due_discount = ' '.join(page_source.find('div', class_='pr-top').find('i',class_='pr-txt').get_text().strip().split(' ')[-3:])
                
                #Lấy tên thương hiệu
                trademark = page_source.find('section', attrs={'data-cate-id':'44','class':'detail'}).find_all('li')[1].get_text().strip().split(' ')[1]
                
                #Lấy dòng sản phẩm
                temp = name.split(' ')
                serie = temp[temp.index(trademark) + 1]
                
                #Lấy thông số sản phẩm
                config = page_source.find('div', class_='parameter')
                parameter_list = []
                ul_element = config.find('ul', class_='parameter__list')
                for li_element in ul_element.find_all('li'):
                    parameter = []
                    parameter = li_element.find('div', class_='liright').text.strip()
                    parameter_list.append(parameter)
                #Thêm các giá trị vào list tương ứng nếu không có lỗi
                names.append(name)
                old_prices.append(old_price)
                present_prices.append(present_price)
                discounts.append(discount)
                due_discounts.append(due_discount)
                configs.append(parameter_list)
                trademarks.append(trademark)
                series.append(serie)
                links.append(link)
                
        except :
            pass

    

    