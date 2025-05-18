import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
cursor = connection.cursor()
result = cursor.execute("SELECT * FROM titles")
fetchAllResult = result.fetchall()

description = result.description
keyList = []
for tuple in description:
    keyList.append(tuple[0])

isbnList = []
titleList = []
editionList = []
copyrightList = []

for tuple in fetchAllResult:
    isbnList.append(tuple[0])
    titleList.append(tuple[1])
    editionList.append(tuple[2])
    copyrightList.append(tuple[3])

df = pd.DataFrame(list(zip(isbnList, titleList, editionList, copyrightList)), columns=[keyList])
print(df)