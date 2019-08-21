import pymysql
connection = pymysql.connect(host='localhost',user='root',password='wyh123456',db='sqlite_test',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO COMPANY VALUES (2, 'Allen', 25, 'Texas', 15000.00)"
        cursor.execute(sql)
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM COMPANY;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(type(result))
        print(result)
finally:
    connection.close()