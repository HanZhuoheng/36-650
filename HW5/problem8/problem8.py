import psycopg2
def select_ten():
    conn = psycopg2.connect(database = "postgres",
                            user = "postgres",
                            password = "..",
                            host = "127.0.0.1",
                            port = '5432')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM employee LIMIT 10;''')
    print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()