import mysql.connector as mysql


def admin_sign_in(username, passwd):

    admin_db = mysql.connect(
        host="localhost",
        user=username,
        password=passwd
    )
    cursor = admin_db.cursor()

    try:
        cursor.execute("use lifechoicesonline")

    except:
        print("Database does not exist.")
        cursor.execute("show databases")


def create_or_drop_user():
    if

