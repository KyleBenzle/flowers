from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xlrd
import xlwt
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def get_image_link(img_nam):
    url = "https://www.google.com/imghp?hl=EN"
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(img_nam)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    driver.find_element_by_xpath("//img[@class='rg_i Q4LuWd']").click()
    time.sleep(3)
    link = driver.find_element_by_xpath("//img[@class='n3VNCb']").get_attribute('src')
    urllib.request.urlretrieve(link, img_nam+"_img.jpg")
    driver.quit()
    return link


wb1 = xlrd.open_workbook("img_search.xlsx")
sheet_r = wb1.sheet_by_index(0)
wb2 = xlwt.Workbook()
sheet_w = wb2.add_sheet("Outputs")

for index in range(4, 30):
    try:
        print(sheet_r.cell_value(index, 0))
        sheet_w.write(index, 0, sheet_r.cell_value(index, 0))
        i_link = get_image_link(sheet_r.cell_value(index, 0))
        sheet_w.write(index, 1, i_link)
    except IndexError:
        break
    except:
        continue

wb2.save("img_search_output.xlsx")


