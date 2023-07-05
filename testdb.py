import cx_Oracle
import traceback

conn=None
try:
    conn=cx_Oracle.connect("mojo/mojo@127.0.0.1/xe")
    print("connected successfully to the db")
    print("db version:",conn.version)
    print("username:",conn.username)
except cx_Oracle.DatabaseError:
    print("sorry conn failed")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("disconn successfully with the db")