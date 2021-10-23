import psycopg2
def create_employee_table():
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="..",
                            host="127.0.0.1",
                            port='5432')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS employee")
    cur.execute('''CREATE TABLE employee(
    id serial, 
    fname varchar(10), 
    lname varchar(10));''')
    conn.commit()
    cur.close()
    conn.close()