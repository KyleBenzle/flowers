from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xlrd
import xlwt
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.error import HTTPError
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import easygui

imageNameList = easygui.fileopenbox()

def get_image_link(img_nam):
    try:
        url = "https://www.google.com/imghp?hl=EN"
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(img_nam)
        action = ActionChains(driver)
        action.send_keys(Keys.ENTER)
        action.perform()
        time.sleep(1)
        driver.find_element_by_xpath("//img[@class='rg_i Q4LuWd']").click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//img[@class='n3VNCb']")))
        time.sleep(2)
        link = driver.find_element_by_xpath("//img[@class='n3VNCb']").get_attribute('src')
        urllib.request.urlretrieve(link, img_nam+"_img.jpg")
        driver.quit()
        if len(link) < 30000:
            return link
        else:
            return ">32000"
    except HTTPError:
        pass


wb1 = xlrd.open_workbook("img_search.xlsx")
sheet_r = wb1.sheet_by_index(0)
wb2 = xlwt.Workbook()
sheet_w = wb2.add_sheet("Outputs")

for index in range(0, 100):
    try:
        print(sheet_r.cell_value(index, 0))
        sheet_w.write(index, 0, sheet_r.cell_value(index, 0))
        i_link = get_image_link(sheet_r.cell_value(index, 0))
        sheet_w.write(index, 1, i_link)
    except IndexError:
        break


wb2.save("img_search_output.xlsx")


