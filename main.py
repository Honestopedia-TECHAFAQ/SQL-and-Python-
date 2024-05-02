import sqlite3

conn = sqlite3.connect('sample.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("All employees:")
for row in rows:
    print(row)
cursor.execute("SELECT * FROM employees WHERE salary > 50000")
rows = cursor.fetchall()
print("\nEmployees earning more than $50,000:")
for row in rows:
    print(row)
new_employee = (4, 'Emily', 60000)
cursor.execute("INSERT INTO employees (id, name, salary) VALUES (?, ?, ?)", new_employee)
conn.commit()
print("\nNew employee added.")
cursor.close()
conn.close()
