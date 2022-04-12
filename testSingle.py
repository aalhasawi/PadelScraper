import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
# Bugs:
# Printing empty list initializer
# times appearing as one string instead of separate

driver = webdriver.Firefox()

dateEntered = "2022-04-22"
sportEntered = "14"
count = 0
venuesList = [
    {"id",
     "Title",
     "Subname",
     "AvailableTime",
     "Location",
     "Price",
     "Size"}
]


URL = "https://www.li3ib.com/en-kw/venues?sport="+sportEntered+"&date="+dateEntered
driver.get(URL)

time.sleep(10)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# toSection = soup.body.div.main.section
# toVenue = toSection.find("div",{"class":"page__container bounceInUp"})

# nestedVenue = soup.find("div", {"class": "page__content"}).ul
singleVenue = soup.find("ul", {"class": "venue__timeslots__list"})
eachTime = singleVenue.li
timeArr = []
for eachTime in singleVenue:
    timeArr.append(eachTime.text)


print(timeArr)

# for singleVenue in nestedVenue:
#     count = count + 1
#     venueName = singleVenue.find("div", {"class": "venue__summary"})
#     venueTitle = venueName.span.text.strip()
#     lengthOfName = len(venueTitle)
#     venueSubName = venueName.p.text.strip()[lengthOfName:]
#     venueTimes = singleVenue.find(
#         "ul", {"class": "venue__timeslots__list"}).text.strip()
#     # for eachSlot in venueTimes:

#     venueSize = singleVenue.find(
#         "div", {"class": "venue__size"}).span.text.strip()
#     venuesList.append({'id': count, 'Title': venueTitle, "SubName": venueSubName,
#                       "AvailableTime": venueTimes, "Size": venueSize})

#     # venueFullName = venueTitle + " / " + venueName.p.text.strip()[lengthOfName:]
#     # venuesList.append(venueFullName)


# print(venuesList)

driver.close()
