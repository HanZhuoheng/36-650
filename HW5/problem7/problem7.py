import psycopg2
def add_data():
    conn = psycopg2.connect(database = "postgres", 
                            user = "postgres", 
                            password = "..", 
                            host = "127.0.0.1", 
                            port = '5432')
    cur = conn.cursor()
    cur.execute('''INSERT INTO employee (id, fname, lname)
    SELECT generate_series(1,500),
    REPEAT('X', (RANDOM()*(10-1)+1)::INTEGER),
    REPEAT('Y', (RANDOM()*(10-1)+1)::INTEGER);''')
    conn.commit()
    cur.close()
    conn.close()