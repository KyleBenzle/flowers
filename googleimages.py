import time

import requests
import bs4 as bs
import pandas as pd
import shutil
df = pd.read_csv('flowers.csv',header=None)
ls=(list(df.iloc[:,0]))
print(ls)
for l in ls:
    fname = "googleimages/"+l+".jpg"
    l = str(l).replace(' ','+')
    url = 'https://www.google.com/search?tbm=isch&sxsrf=ALeKk00Qm8_TezeukthewdejHwdDX0JZKg%3A1598191857603&source=hp&biw=1920&bih=947&ei=8XhCX6qBIsG6acDylsAB&q='+l+'&oq='+l+'&gs_lcp=CgNpbWcQAzICCAAyBQgAELEDMgIIADICCAAyBQgAELEDMgIIADICCAAyAggAMgIIADICCAA6CAgAELEDEIMBUJ4LWI8jYKQkaABwAHgAgAG1AogBkxCSAQUyLTguMZgBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ved=0ahUKEwjqvc_PwLHrAhVBXRoKHUC5BRgQ4dUDCAc&uact=5'
    resp = requests.get(url)
    soup = bs.BeautifulSoup(resp.content,"html.parser")
    img = soup.find_all('img',class_='t0fcAb',src=True)
    r = requests.get(img[0]['src'], stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(fname, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', fname)
    else:
        print('Image Couldn\'t be retreived')
    time.sleep(2)