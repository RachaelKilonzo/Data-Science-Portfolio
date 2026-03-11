import pandas as pd
import requests
from bs4 import BeautifulSoup


#100 Metres Decathlon


hundred_metres = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/100-metres/summary'
page100 = requests.get(hundred_metres)
page100.encoding = 'utf-8'
soup100 = BeautifulSoup(page100.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
table100 = soup100.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
table100_titles = table100.find_all('th')
table100_titles = [titles.text.strip() for titles in table100_titles] 
#Create a dataframe with the column titles as headers
df100 = pd.DataFrame(columns = table100_titles)
#Get all the rows of the table
column_data = table100.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(df100.columns):
        length = len(df100)
        df100.loc[length] = individual_row_data
df100['Day'] = "04-AUG-2021"
df100['Time'] = "09:00"
df100['Event'] = "100 Metres"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in df100.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
df100 = df100[columns_order]




#Long Jump

long_jump = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/long-jump/summary'
pagelong = requests.get(long_jump)
pagelong.encoding = 'utf-8'
souplong = BeautifulSoup(pagelong.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
tablelong = souplong.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
tablelong_titles = tablelong.find_all('th')
tablelong_titles = [titles.text.strip() for titles in tablelong_titles] 
#Create a dataframe with the column titles as headers
dflong = pd.DataFrame(columns = tablelong_titles)
#Get all the rows of the table
column_data = tablelong.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(dflong.columns):
        length = len(dflong)
        dflong.loc[length] = individual_row_data
dflong['Day'] = "04-AUG-2021"
dflong['Time'] = "09:55"
dflong['Event'] = "Long Jump"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in dflong.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
dflong = dflong[columns_order]




#Shot Put

shot_put = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/shot-put/summary'
pageshot = requests.get(shot_put)
pageshot.encoding = 'utf-8'
soupshot = BeautifulSoup(pageshot.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
tableshot = soupshot.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
tableshot_titles = tableshot.find_all('th')
tableshot_titles = [titles.text.strip() for titles in tableshot_titles] 
#Create a dataframe with the column titles as headers
dfshot = pd.DataFrame(columns = tableshot_titles)
#Get all the rows of the table
column_data = tableshot.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(dfshot.columns):
        length = len(dfshot)
        dfshot.loc[length] = individual_row_data
dfshot['Day'] = "04-AUG-2021"
dfshot['Time'] = "11:40"
dfshot['Event'] = "Shot Put"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in dfshot.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
dfshot = dfshot[columns_order]





#High Jump

high_jump = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/high-jump/summary'
pagehigh = requests.get(high_jump)
pagehigh.encoding = 'utf-8'
souphigh = BeautifulSoup(pagehigh.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
tablehigh = souphigh.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
tablehigh_titles = tablehigh.find_all('th')
tablehigh_titles = [titles.text.strip() for titles in tablehigh_titles] 
#Create a dataframe with the column titles as headers
dfhigh = pd.DataFrame(columns = tablehigh_titles)
#Get all the rows of the table
column_data = tablehigh.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(dfhigh.columns):
        length = len(dfhigh)
        dfhigh.loc[length] = individual_row_data
dfhigh['Day'] = "04-AUG-2021"
dfhigh['Time'] = "18:30"
dfhigh['Event'] = "High Jump"
# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in dfhigh.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
dfhigh = dfhigh[columns_order]




#400 metres
fourhundred_metres = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/400-metres/summary'
page400 = requests.get(fourhundred_metres)
page400.encoding = 'utf-8'
soup400 = BeautifulSoup(page400.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
table400 = soup400.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
table400_titles = table400.find_all('th')
table400_titles = [titles.text.strip() for titles in table400_titles] 
#Create a dataframe with the column titles as headers
df400 = pd.DataFrame(columns = table400_titles)
#Get all the rows of the table
column_data = table400.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(df400.columns):
        length = len(df400)
        df400.loc[length] = individual_row_data
df400['Day'] = "04-AUG-2021"
df400['Time'] = "21:30"
df400['Event'] = "400 Metres"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in df400.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
df400 = df400[columns_order]




#110 metres Hurdles

onehundred_MetresHurdles = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/110-metres-hurdles/summary'
page110 = requests.get(onehundred_MetresHurdles)
page110.encoding = 'utf-8'
soup110 = BeautifulSoup(page110.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
table110 = soup110.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
table110_titles = table110.find_all('th')
table110_titles = [titles.text.strip() for titles in table110_titles] 
#Create a dataframe with the column titles as headers
df110 = pd.DataFrame(columns = table110_titles)
#Get all the rows of the table
column_data = table110.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(df110.columns):
        length = len(df110)
        df110.loc[length] = individual_row_data
df110['Day'] = "05-AUG-2021"
df110['Time'] = "09:00"
df110['Event'] = "110 Metres Hurdles"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in df110.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
df110 = df110[columns_order]




#Discus Throw

discus = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/discus-throw/summary'
pagediscus = requests.get(discus)
pagediscus.encoding = 'utf-8'
soupdiscus = BeautifulSoup(pagediscus.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
tablediscus = soupdiscus.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
tablediscus_titles = tablediscus.find_all('th')
tablediscus_titles = [titles.text.strip() for titles in tablediscus_titles] 
#Create a dataframe with the column titles as headers
dfdiscus = pd.DataFrame(columns = tablediscus_titles)
#Get all the rows of the table
column_data = tablediscus.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(dfdiscus.columns):
        length = len(dfdiscus)
        dfdiscus.loc[length] = individual_row_data
dfdiscus['Day'] = "05-AUG-2021"
dfdiscus['Time'] = "09:50"
dfdiscus['Event'] = "Discus Throw"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in dfdiscus.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
dfdiscus = dfdiscus[columns_order]



#Pole Vault

pole = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/pole-vault/summary'
pagepole = requests.get(pole)
pagepole.encoding = 'utf-8'
souppole = BeautifulSoup(pagepole.text, 'html.parser')

# Find the table with the class 'table table-striped' on the webpage
tablepole = souppole.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
tablepole_titles = tablepole.find_all('th')
tablepole_titles = [titles.text.strip() for titles in tablepole_titles] 
#Create a dataframe with the column titles as headers
dfpole = pd.DataFrame(columns = tablepole_titles)
#Get all the rows of the table
column_data = tablepole.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(dfpole.columns):
        length = len(dfpole)
        dfpole.loc[length] = individual_row_data
dfpole['Day'] = "05-AUG-2021"
dfpole['Time'] = "12:45"
dfpole['Event'] = "Pole Vault"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in dfpole.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
dfpole = dfpole[columns_order]



# Javelin Throw

javelin = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/javelin-throw/summary'
pagejavelin = requests.get(javelin)
pagejavelin.encoding = 'utf-8'
soupjavelin = BeautifulSoup(pagejavelin.text, 'html.parser')

# Find the table with the class 'table table-striped' on the webpage
tablejavelin = soupjavelin.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
tablejavelin_titles = tablejavelin.find_all('th')
tablejavelin_titles = [titles.text.strip() for titles in tablejavelin_titles] 
#Create a dataframe with the column titles as headers
dfjavelin = pd.DataFrame(columns = tablejavelin_titles)
#Get all the rows of the table
column_data = tablejavelin.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(dfjavelin.columns):
        length = len(dfjavelin)
        dfjavelin.loc[length] = individual_row_data
dfjavelin['Day'] = "05-AUG-2021"
dfjavelin['Time'] = "19:15"
dfjavelin['Event'] = "Javelin Throw"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in dfpole.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
dfjavelin = dfjavelin[columns_order]



# 1500 Metres

fifteenhundred_metres = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/1500-metres/result'
page1500 = requests.get(fifteenhundred_metres)
page1500.encoding = 'utf-8'
soup1500 = BeautifulSoup(page1500.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
table1500 = soup1500.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
table1500_titles = table1500.find_all('th')
table1500_titles = [titles.text.strip() for titles in table1500_titles] 
#Create a dataframe with the column titles as headers
df1500 = pd.DataFrame(columns = table1500_titles)
#Get all the rows of the table
column_data = table1500.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(df1500.columns):
        length = len(df1500)
        df1500.loc[length] = individual_row_data
df1500['Day'] = "05-AUG-2021"
df1500['Time'] = "21:40"
df1500['Event'] = "1500 Metres"

# Specify the order of the columns
columns_order = ['Event', 'Day', 'Time'] + [col for col in df1500.columns if col not in ['Event', 'Day', 'Time']]
# Reorder the DataFrame
df1500 = df1500[columns_order]



# Results

points = 'https://worldathletics.org/competitions/olympic-games/the-xxxii-olympic-games-7132391/results/men/decathlon/1500-metres/points'
page = requests.get(points)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'html.parser')
# Find the table with the class 'table table-striped' on the webpage
table = soup.find("table", class_="Table_table__2zsdR")
#Get the titles (Headers) of the table
table_titles = table.find_all('th')
table_titles = [titles.text.strip() for titles in table_titles] 
#Create a dataframe with the column titles as headers
df = pd.DataFrame(columns = table_titles)
#Get all the rows of the table
column_data = table.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data  = [data.text.strip() for data in row_data]
    
    if len(individual_row_data) == len(df.columns):
        length = len(df)
        df.loc[length] = individual_row_data





decathlon = pd.concat([df100, dflong, dfshot, dfhigh, df400, df110, dfdiscus, dfpole, dfjavelin, df1500], axis= 0, ignore_index=True)
decathlon.to_csv("C:/Users/PC/Desktop/Portfolio/Decathlon Tokyo/decathlon2020.csv", index = False)






