from bs4 import BeautifulSoup
import csv
import requests

#Find table and move to csv
def getTableToCsv(link,index):

    #Grab content
    result = requests.get(link)

    #Save source in variable
    source = result.content     

    #Activate soup
    soup = BeautifulSoup(source,'lxml')

    #Find all tables
    findtable = soup.find_all('table')

    #Find specific table with index
    findtable2 = findtable[index]

    #Open csv and save table
    with open('DeathByTraffic.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        for x in findtable2('tr'):
            row = [t.get_text(strip=True)for t in x(['td','th'])]
            writer.writerow(row)

#Link, CSV file name and index table to scrape
getTableToCsv('https://en.wikipedia.org/wiki/List_of_countries_by_traffic-related_death_rate',1)

#########################################CSV CLEAN UP#########################################################

#Open csv file and read
with open ('DeathByTraffic.csv') as inf:
    reader = csv.reader(inf.readlines()[8:])

#Clean and overwrite CSV
with open ('DeathByTraffic.csv','w',newline='') as outf:
    writer = csv.writer(outf)
    writer.writerow(('Country','Road fatalities per 100000 inhabitants per year','Road fatalities per 100000 motor vehicles','Estimated fatalities per year'))
    for line in reader:
        cell1 = line[0]
        cell3 = line[2].replace("[nb 3]","")
        cell4 = line[3].replace(" ","0").replace("n/a","0").replace("[nb05]","")
        cell6 = line[5].replace(","," ").replace("[nb 3]","")
        row = [cell1,cell3,cell4,cell6]
        writer.writerow(row)
