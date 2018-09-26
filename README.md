# Logs Analysis :


an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

# Startup :
before using this program you must have The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, my code will answer questions about the site's user activity.

# features :
- Analiyze the site's user activity.
- show the most popular three articles of all time? Which articles have been accessed the most.
- show the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views.
- On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.
- It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

# Set Up :


1. download data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
this file contains data that you will use>

2. unzip this file and run the query on your postgre SQL serever
using this command :
```sh
psql -d news  #news the name of database.
```
3. after logging to the database create this views:

- view1---get most articles that have been viewed :
``` create view most_articles as select replace(path,'/article/','')as head,count(*) as views   from  log group by path order by views desc ; ```

- view2---'get the most articles's authors that have been viewed'
```create view author_view as select author ,sum(views) as sum_views from articles,most_articles where slug=head group by author;```

- view3---get the sum of error request for each day :
```create view allnfreqs as select date(time) as day,count(status) as n from log where status like '%404%' group by day;```

- view4---get the sum of all request for each day :
```create view allreqs as select date(time) as d,count(status)as num from log  group by d;```

- view5---get the the sum of all request and the sum of error request for each day and ratio :
```create view errors as select day ,num,n,round(((n+0.0)/(num+0.0))*100,2) as rate from allreqs,allnfreqs where day=d ;```

3. go to the myscript.py file and run it using this command:
```sh
python myscript.py
```
4. you will get the output> 
