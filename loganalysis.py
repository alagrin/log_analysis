import psycopg2

db = psycopg2.connect("dbname=news")
cur = db.cursor()

def get_top_articles():
    query1 = "SELECT articles.title, count(*) FROM articles JOIN log ON log.path ILIKE '%' || articles.slug || '%' GROUP BY articles.title ORDER BY count(*) DESC LIMIT 3;"
    cur.execute(query1)
    result1 = cur.fetchall()
    
    for item in result1:
        print(item)
get_top_articles()

def get_top_viewed_authors():
    query2 = "SELECT authors.name, count(*) as views FROM authors JOIN articles ON articles.author = authors.id JOIN log ON log.path ILIKE '%' || articles.slug || '%' GROUP BY authors.name ORDER BY views DESC;"
    cur.execute(query2)
    result2 = cur.fetchall()

    for item in result2:
        print (item)
get_top_viewed_authors()

# def error_percentage_below_1percent():
#     query3 = "select table1.day, 100.0 * error_count/status_count as percent_count" 
#     " from (select date(time) as day, count(*) as status_count from log group by day) table1," 
# " (select date(time) as day, count(status) as error_count from log where status = '404 NOT FOUND' group by day) table2"
# " where table1.day = table2.day and error_count > 0.01 * statuscount;"
#     cur.execute(query3)
#     result3 = cur.fetchall()
#     return result3
# print(error_percentage_below_1percent)

# cur.close()
# db.close()

if __name__ == '__main__':
    get_top_articles()
    get_top_viewed_authors()