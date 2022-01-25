from bs4 import BeautifulSoup as bs
import pandas as pd 
import requests
 
dwarf_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs' 
page2 = requests.get(dwarf_url)

print(page2)
soup = bs(page2.text,'html.parser')
dwarf_table = soup.find('table')

temp_list = []
table_rows = dwarf_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]

    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df3 = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns = ['star_names','distance','mass','radius'])
print(df3)

df3.to_csv('dwarf.csv')