# Python version 3
import psycopg2
DBNAME = "news"


def popular_three_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q = "select replace(head,'/','')as head,views from most_articles limit 3;"
    c.execute(q)
    return c.fetchall()
    c.close()


def popular_article_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q = "select name,sum_views from authors,author_view where author=id;"
    c.execute(q)
    return c.fetchall()
    c.close()


def requests_lead_to_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q = "select day,rate from errors where rate >1;"
    c.execute(q)
    return c.fetchall()
    c.close()


print("\n### What are the most popular three articles of all time? ###")
for row in popular_three_articles():
    print(row[0]),
    print(" --> "),
    print(row[1]),
    print(" views")

print("\n### Who are the most popular article authors of all time? ###")
for row in popular_article_authors():
    print(row[0]),
    print(" --> "),
    print(row[1]),
    print(" views")

print("\n### On which days did more than 1% of requests lead to errors ###")
for row in requests_lead_to_errors():
    print(row[0]),
    print(" --> "),
    print(row[1]),
    print("% errors")
