import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Text File
Data = open("demo.txt","w")

#Data Scrap Proccess
driver = webdriver.Chrome("D:\Senti AI\selenium drivers\chromedriver.exe") #Driver Directory
driver.get('https://www.sunstar.com.ph/article/1766076/Pampanga/Opinion/Miyayaliwang-Tabas-king-Kapampangan-(Various-Shapes-in-Kapampangan)') #Website

main = driver.find_element_by_class_name("col-sm-11 ") #Where to Find the Scrap 
print(main.text)
Data.write(main.text)


#Inputing The Data Scrap into Text File
Data.close()


##Converting Text Into Json
def write_json(data, filename="TRY.json"):
    with open(filename, "a+") as f:
        json.dump(data, f, indent=4)


with open("TRY.json") as json_file:
    data = json.load(json_file)
    temp = data["kapampanganWords"]
    
    with open("demo.txt", "r") as f:
        words = f.read()
        words = words.replace(',','')
        words = words.replace('.','')
        words = words.replace('?','')
        words = words.replace('!','')
        words = words.replace('-','')
        words = words.replace(' ','\n')
        words = words.split('\n')


        while "" in words:
            words.remove("")
            
        
        for i in words:
            if i.isalpha()==False:
                continue
            y = {"token": i.lower()}
            temp.append(y)

driver.close()
write_json(data)
