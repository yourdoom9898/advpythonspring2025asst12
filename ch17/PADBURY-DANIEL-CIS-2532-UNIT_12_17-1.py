import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
cursor = connection.cursor()
resultAuthLastDesc = pd.read_sql("SELECT last FROM authors ORDER BY last DESC", connection)
print(resultAuthLastDesc)

resultTitleAsc = pd.read_sql("SELECT title FROM titles ORDER BY title ASC", connection)
print(resultTitleAsc)

queryIJ = """
SELECT titles.title, titles.isbn, titles.copyright
FROM titles
INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
INNER JOIN authors on author_ISBN.id = authors.id
WHERE authors.first = 'Abbey' AND authors.last = 'Deitel'
ORDER BY titles.title
"""
resultInnerJoinAuthBooksAsc = pd.read_sql(queryIJ, connection)
print(resultInnerJoinAuthBooksAsc)

newAuthorFirst = "Ray"
newAuthorLast = "Bradbury"

queryIA = f"INSERT INTO authors (first, last) VALUES ('{newAuthorFirst}', '{newAuthorLast}')"

cursor.execute(queryIA)
connection.commit()
connection.close
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

updated_authors = pd.read_sql("SELECT id, first, last FROM authors", connection)
print(updated_authors)

queryIT = "INSERT INTO titles VALUES ('1501179497', 'Something Wicked This Way Comes', '1', '1952')"
queryIAISBN = "INSERT INTO author_isbn VALUES ('6', '1501179497')"

cursor.execute(queryIT)
cursor.execute(queryIAISBN)
connection.commit()
connection.close
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

updated_titles = pd.read_sql("SELECT * FROM titles", connection)
print(updated_titles)

updatedAuthISBN = pd.read_sql("SELECT * FROM author_ISBN WHERE author_ISBN.id = 6", connection)
print(updatedAuthISBN)