from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xlrd
import xlwt
import urllib.request


def get_image_link(img_nam):
    url = "https://unsplash.com/s/photos/"
    url += img_nam
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    link = driver.find_element_by_xpath("//a[@itemprop='contentUrl']").get_attribute('href')
    link += "/download?force=true"
    urllib.request.urlretrieve(link, img_nam+"_img.jpg")
    return link


wb1 = xlrd.open_workbook("img_search.xlsx")
sheet_r = wb1.sheet_by_index(0)
wb2 = xlwt.Workbook()
sheet_w = wb2.add_sheet("Outputs")

for index in range(1, 10):
    try:
        print(sheet_r.cell_value(index, 0))
        sheet_w.write(index, 0, sheet_r.cell_value(index, 0))
        i_link = get_image_link(sheet_r.cell_value(index, 0))
        sheet_w.write(index, 1, i_link)
    except IndexError:
        break

wb2.save("img_search_output.xlsx")


