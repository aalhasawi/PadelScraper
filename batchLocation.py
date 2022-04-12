import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


f = open("output.txt", "a")



dateEntered = "2022-04-22"
# sportEntered = "14"
count = 0
venuesList = [
    # {"id",
    #  "Title",
    #  "Subname",
    #  "AvailableTime",
    #  "Location",
    #  "Price",
    #  "Size"}
]
driver = webdriver.Firefox()
URL = "https://www.li3ib.com/en-kw/venues/"+str(count)+"?&date="+dateEntered
# https://www.li3ib.com/en-kw/venues/386?date=2022-04-22
# https://www.li3ib.com/en-kw/error

venueIds=[]

# foundError=0

for count in range(289,500):
    URL = "https://www.li3ib.com/en-kw/venues/"+str(count)+"?&date="+dateEntered
    driver.get(URL)
    time.sleep(15)
        # html = soup.find("div",{"class":"sc-hiSbYr XqbgT"}).h1.text.strip()
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    try:
        print(soup.find("div",{"class":"sc-hiSbYr XqbgT"}).h1.text.strip())
    except:
        venueIds.append({"venueName":soup.find("div",{"class":"venue__summary"}).p.span.text.strip(),"count":count})
    print(venueIds)
    # try:
    #     soup.find("div",{"class":"sc-hiSbYr XqbgT"})
    #     #.h1.text.strip()
    # except:
    #     continue
    # if()
    # else:
    #     venueIds.append(count)

    
    # except:
    #     venueIds.append(count)
    # if( == "SORRY!"):
    #     continue

    # print(venueIds)


print(venueIds, file=f)

driver.close()
f.close()

# print(driver.page_source)

# time.sleep(6)

# html = driver.page_source

# nestedVenue = soup.find("div", {"class": "page__content"}).ul
# singleVenue = nestedVenue.li.div