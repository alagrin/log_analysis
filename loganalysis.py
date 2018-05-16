#!/usr/bin/env python

import psycopg2
import time


def get_top_articles():
    """Shows top viewed articles by title and number of views"""
    query1 = """
            SELECT
                articles.title,
                count(*)
            FROM
                articles
            INNER JOIN
                log
            ON
                concat('/article/', articles.slug) = log.path
            GROUP BY
                articles.title
            ORDER BY
                count(*)
                DESC
                LIMIT 3;"""
    cur.execute(query1)
    result1 = cur.fetchall()
    print ('\nHere are the top 3 articles of all time: \n')
    for title, views in result1:
        print ('"{0}" - {1} views'.format(title, views))


def get_top_viewed_authors():
    """Shows top authors and corresponding number of views"""
    query2 = """
            SELECT
                authors.name, count(*) as views
            FROM
                authors
            JOIN
                articles
            ON
                articles.author = authors.id
            JOIN
                log
            ON
                concat('/article/', articles.slug) = log.path
            GROUP BY
                authors.name
            ORDER BY
                views
            DESC;"""
    cur.execute(query2)
    result2 = cur.fetchall()
    print ('\nThe most popular article authors of all time: \n')
    for item in result2:
        print ("{0} - {1} views".format(item[0], item[1]))


def error_percentage_over_1percent():
    """Shows the day where percentage of error statuses is over 1%"""
    query3 = """
            SELECT
                table1.day, 100.0 * error_count/status_count AS percent_count
            FROM
                (select date(time) AS day, count(*) AS status_count
            FROM
                log GROUP BY day) table1,
            (SELECT
                date(time) AS day, count(status) AS error_count
            FROM
                log
            WHERE
                status = '404 NOT FOUND'
            GROUP BY day) table2
            WHERE
                table1.day = table2.day
            AND
                error_count > 0.01 * status_count;"""
    cur.execute(query3)
    result3 = cur.fetchall()
    print('\nHere are the days we had errors for over 1% of requests: \n')
    for item in result3:
        print (
            "{0:%B %d %Y} - {1:.2f}% of requests".
            format(item[0], item[1])
            )


if __name__ == '__main__':
    db = psycopg2.connect("dbname=news")
    print('Opened Database Successfully')
    cur = db.cursor()
    print("Querying database...")
    get_top_articles()
    get_top_viewed_authors()
    error_percentage_over_1percent()
    db.close()
