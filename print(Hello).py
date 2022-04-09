import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Bugs:
# Printing empty list initializer
# times appearing as one string instead of separate

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

driver = webdriver.Firefox()
URL = "https://www.li3ib.com/en-kw/venues?sport="+sportEntered+"&date="+dateEntered
driver.get(URL)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

# toSection = soup.body.div.main.section
# toVenue = toSection.find("div",{"class":"page__container bounceInUp"})

nestedVenue = soup.find("div",{"class":"page__content"}).ul
singleVenue = nestedVenue.li

for singleVenue in nestedVenue:
    count = count + 1
    venueName = singleVenue.find("div",{"class":"venue__summary"})
    venueTitle = venueName.span.text.strip()
    lengthOfName = len(venueTitle)
    venueSubName = venueName.p.text.strip()[lengthOfName:]
    venueTimes = singleVenue.find("ul",{"class":"venue__timeslots__list"}).text.strip()
    venueSize = singleVenue.find("div",{"class":"venue__size"}).span.text.strip()
    venuesList.append({'id':count, 'Title':venueTitle, "SubName":venueSubName,"AvailableTime":venueTimes,"Size":venueSize})

    # venueFullName = venueTitle + " / " + venueName.p.text.strip()[lengthOfName:]
    # venuesList.append(venueFullName)
    

print(venuesList)

driver.close()





# for nesting in parentDiv:
#     print(nesting)


# divNests = soup.body.div.main
# divNests.find("div",)































# # print(soup.prettify)
# ulContainer = soup.find_all("ul", string="venue__timeslots__list")
# # for litag in ulContainer.find('li'):
# #     print (litag.text)
# print (soup.venue__timeslots__list.li.)
















































# import requests
# from bs4 import BeautifulSoup

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id="ResultsContainer")
# print(results.prettify())
# job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#     print(job_element, end="\n"*2)
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element)
#     print(company_element)
#     print(location_element)
#     print()

#     for job_element in job_elements:
#         title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text)
#     print(company_element.text)
#     print(location_element.text)
#     print()

#     for job_element in job_elements:
#         title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()