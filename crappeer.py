from selenium import webdriver
from selenium.webdriver.common.by import By
import requests 
from bs4 import BeautifulSoup
import csv
import time

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser= webdriver.Chrome('chromedriver.exe')
browser.get(start_url)


time.sleep(10)

planets_data = []

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink", 
            "planet_type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]

def scrape():
    for i in range(1,5):
        while True:
            time.sleep(2)

            soup = BeautifulSoup(browser.page_source, "html.parser")

            # Check page number    
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))

            if current_page_num < i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break

        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            # Get Hyperlink Tag
            hyperlink_li_tag = li_tags[0]

            temp_list.append("https://exoplanets.nasa.gov"+ hyperlink_li_tag.find_all("a", href=True)[0]["href"])
            
            planets_data.append(temp_list)

        browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

        print(f"Page {i} scraping completed")
    
scrape()

Newplanets = []

def scrape2(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        temp_list = []
        for tr_tag in soup.find_all("tr", attrs={"class":"factrow"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        Newplanets.append(temp_list)                

    except:
        scrape2(hyperlink)
   
finalplanetdata = []

for index,data in enumerate(planets_data):
    scrape2(data[5])
    
for index,data in enumerate(planets_data):
    newdata = newdata[index]
    newdata = [elem.replace("\n", "") for elem in newdata]   
    newdata = newdata[:14]
    finalplanetdata.append(data+newdata)  
    
with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(finalplanetdata)