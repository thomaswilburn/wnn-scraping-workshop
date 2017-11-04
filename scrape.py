# load modules to do page requests, scraping, and CSV output
import requests
from bs4 import BeautifulSoup
import csv

# useful to load these into variables instead of writing them into code
listURL = "https://en.wikipedia.org/wiki/List_of_generation_I_Pok%C3%A9mon"
prefix = "https://en.wikipedia.org"

# get the overview page and create a searchable "soup" version
listPage = requests.get(listURL)
listSoup = BeautifulSoup(listPage.text)

# find the table of pokemon
table = listSoup.find(class_="wikitable")

# within that table, let's get all the rows
rows = table.find_all("tr")

# open a CSV file for output
with open("pokemon.csv", "w", newline="") as f:
    # create an object that "writes" CSV data to the hard drive
    writer = csv.writer(f)
    # loop through each row...
    for row in rows:
        # we could get the children to access each cell
        cells = row.children()
        second = cells[1]
        # but otherwise we could find a cell by HTML tag name
        nameColumn = row.find("th")
        # get the contents of that cell
        name = nameColumn.get_text()
        # write out a row to our CSV with the name and the word "Pokemon"
        writer.writerow([name, "Pokemon"])
        # are there any links in that name cell?
        link = nameColumn.find("a")
        # if so...
        if link:
            # log out the URL for additional information
            print(prefix + link["href"])
            # homework: scrape those pages to get additional data by filing
            # a second request to the link URL

# this is outside the loop (indentation is gone)
print("All done")


