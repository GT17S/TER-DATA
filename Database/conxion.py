import psycopg2
conn = psycopg2.connect(database="TER",
                              user="postgres",
                              password="halliche",
                              host="localhost",
    port=5432)
