import psycopg2
import pandas as pd


def insert_into_sql_table():
    try:
        connection = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow",
                                      port='5432')
        cur = connection.cursor()

        insert_query = "INSERT INTO class VALUES('Gaurav', 'Kothyari', 12345, 'M')"

        cur.execute(insert_query)
        print("Inserted into table successfully")

    except:
        print("Could not insert into database. Unknown error occurred.")

    finally:
        if connection is not None:
            connection.commit()
            connection.close()