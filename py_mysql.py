# %%
import py_mysql

mydb = py_mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

print(mydb)


# %%
