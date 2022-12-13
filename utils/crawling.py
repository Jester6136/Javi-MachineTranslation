from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import sys
sys.path.append('/media/ba/N_Vol/ubuntu/Javi-MachineTranslation')
from config import *

button_routes = np.arange(0,1001*40,step=40)
print('Preparing crawing')
result = []
driver:webdriver.Chrome = webdriver.Chrome(CHROME_DRIVER)
options = webdriver.ChromeOptions() 
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
print('Crawing.....')
for button_route in button_routes:
    driver.get('https://www.opensubtitles.org/en/search/sublanguageid-jpn,vie/offset-'+str(button_route))    
    elems = driver.find_elements(By.CLASS_NAME, 'change')
    for elem in elems:
        tds = elem.find_elements(By.TAG_NAME,'td')
        film_name = tds[0].find_elements(By.TAG_NAME,'strong')[0].text
        flag = tds[1].find_elements(By.CLASS_NAME,'flag')[0].get_attribute('class')
        time = tds[3].find_elements(By.TAG_NAME,'time')[0].text
        link = tds[4].find_elements(By.TAG_NAME,'a')[0].get_attribute('href')
        uploader = tds[8].find_elements(By.TAG_NAME,'a')[0].text
        result.append([film_name,flag.replace('flag ',''),time,link,uploader])
driver.close()
print('Crawed')
df = pd.DataFrame(result, columns=['film_name','flag','time', 'link','uploader'])
df.to_csv(RAW_DATA_PATH,index=False)
print('saved to ',RAW_DATA_PATH)