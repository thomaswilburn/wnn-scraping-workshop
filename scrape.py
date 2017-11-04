import requests
from bs4 import BeautifulSoup
import csv

listURL = "https://en.wikipedia.org/wiki/List_of_generation_I_Pok%C3%A9mon"
prefix = "https://en.wikipedia.org"

listPage = requests.get(listURL)
listSoup = BeautifulSoup(listPage.text)

table = listSoup.find(class_="wikitable")

rows = table.find_all("tr")

with open("pokemon.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        cells = row.children()
        second = cells[1]
        nameColumn = row.find("th")
        name = nameColumn.get_text()
        writer.writerow([name, "Pokemon"])
        link = nameColumn.find("a")
        if link:
            print(prefix + link["href"])

print("All done")


