import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

dateEntered = "2022-04-22"
sportEntered = "14"
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
URL = "https://www.li3ib.com/en-kw/venues?sport="+sportEntered+"&date="+dateEntered
driver.get(URL)

time.sleep(6)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

nestedVenue = soup.find("div", {"class": "page__content"}).ul
singleVenue = nestedVenue.li.div

for singleVenue in nestedVenue:

    count = count + 1
    venueName = singleVenue.find("div", {"class": "venue__summary"})

    venueTitle = venueName.span.text.strip()
    lengthOfName = len(venueTitle)
    venueSubName = venueName.p.text.strip()[lengthOfName:]

    venueTimes = singleVenue.find(
        "ul", {"class": "venue__timeslots__list"})
    eachTime = venueTimes.li
    timeArr = []
    for eachTime in venueTimes:
        timeArr.append(eachTime.text)

    venueSize = singleVenue.find(
        "div", {"class": "venue__size"}).span.text.strip()
    venuesList.append({'id': count, 'Title': venueTitle, "SubName": venueSubName,
                      "AvailableTime": timeArr, "Size": venueSize})

    # venueFullName = venueTitle + " / " + venueName.p.text.strip()[lengthOfName:]
    # venuesList.append(venueFullName)


print(venuesList[0])

driver.close()
