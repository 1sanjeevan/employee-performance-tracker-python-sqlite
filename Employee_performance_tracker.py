# importing the sqlite3 to use database
import sqlite3

# connect to database (file will be created automatically na here)
conn = sqlite3.connect("employee.db")

# create cursor
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee(
name TEXT,
score INTEGER
)
""")

# menu
print("1. Add Employee")
print("2. View Employees")
print("3. Show Best Performer")

choice = input("Enter choice: ")


#  ADD EMPLOYEE
if choice == "1":

    # take employee name
    name = input("Enter employee name: ")

    # take performance score
    score = int(input("Enter performance score (1-10): "))

    # insert into database
    cursor.execute("INSERT INTO employee VALUES(?,?)", (name, score))

    # save data
    conn.commit()

    print("Employee Added")


#  VIEW ALL EMPLOYEES
elif choice == "2":

    # get all data
    cursor.execute("SELECT * FROM employee")

    data = cursor.fetchall()

    print("Employee List:")

    for row in data:
        print("Name:", row[0], "| Score:", row[1])


#  SHOW BEST PERFORMER
elif choice == "3":

    # get highest score
    cursor.execute("SELECT * FROM employee ORDER BY score DESC LIMIT 1")

    best = cursor.fetchone()

    if best:
        print(" Best Performer →", best[0], "Score:", best[1])
    else:
        print("No data found")

# close connection
conn.close()