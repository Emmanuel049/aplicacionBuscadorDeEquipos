# import pymysql
import psycopg2

# db = pymysql.connect('PostgreSQL 14', 'postgres', 'asd123', 'postgres')
# db = pymysql.connect(host='localhost',user='postgres',password='asd123',database='postgres',port=1234,bind_address="localhost")
# db = pymysql.connect(host='localhost',user='postgres',password='asd123',database='postgres',port=1234)

try:
    db = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='asd123',
        database='postgres',
        port=1234
    )

    # print(db)
    print("Conexion Exitosa")

    cursor = db.cursor()
    query = "SELECT version()"
    cursor.execute(query)
    retorno = cursor.fetchone()
    print(retorno)

    query = "SELECT * FROM login"
    cursor.execute(query)
    retorno = cursor.fetchall()
    print(retorno)

except Exception as e:
    print (e)

finally:
    db.close()
    print("Conexion Finalizada")