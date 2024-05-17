import psycopg2
import time

time.sleep(5)

def StartDb():
    try:
        db = psycopg2.connect(host='db', port=5432, user='postgres',
                              password='postgres', dbname='db')
        cursor = db.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS PEDIDOS (
            id SERIAL PRIMARY KEY,
            USUARIO VARCHAR(100),
            EMAIL VARCHAR(100),
            DESCRICAO VARCHAR(100)
        );
        ''')
        
        db.commit()
        cursor.close()
        db.close()
        print("Database initialization completed successfully!")
    except psycopg2.Error as e:
        print("Error initializing database:", e)

StartDb()
