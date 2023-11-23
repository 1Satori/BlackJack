import pymysql
from main import username
from constants import userbalans

from config_DB import host, user, password, db_name
try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
except Exception as ex:
    print("Connection refused...")
    print(ex)


# add users


with connection.cursor() as cursor:
    query = "INSERT INTO users(username, balance) VALUES(%s, %s);"
    cursor.execute(query, (username,userbalans))
    connection.commit()
    print(f'User succsessfully added')


def check_user_exists(username):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
    except Exception as ex:
        print("Connection refused...")
        print(ex)
