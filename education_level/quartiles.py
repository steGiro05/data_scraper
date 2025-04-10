import sqlite3
import pandas as pd 
import numpy as np
import os

def compute_quartiles(data):
    data = np.array(data)
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    return q1, q2, q3

df = pd.read_csv('Salary.csv')

# Create in-memory SQLite DB
conn = sqlite3.connect(':memory:')
df.to_sql('my_table', conn, index=False, if_exists='replace')
cursor = conn.cursor()

# Fetch and sort experience values
cursor.execute("SELECT Years_of_experience FROM my_table ORDER BY Years_of_experience")
res = cursor.fetchall()
sorted_salaries = [int(row[0]) for row in res]

# Compute quartiles
q1, q2, q3 = compute_quartiles(sorted_salaries)
print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}")

# Helper to fetch data
def fetch_range(query, params):
    cursor.execute(query, params)
    return [{"Salary": int(row[0]), "Years_of_experience": int(row[1])} for row in cursor.fetchall()]

# Quartile buckets
q1_data = fetch_range("SELECT Salary, Years_of_experience FROM my_table WHERE Years_of_experience <= ? ORDER BY Years_of_experience", (q1,))
q2_data = fetch_range("SELECT Salary, Years_of_experience FROM my_table WHERE Years_of_experience > ? AND Years_of_experience <= ? ORDER BY Years_of_experience", (q1, q2))
q3_data = fetch_range("SELECT Salary, Years_of_experience FROM my_table WHERE Years_of_experience > ? AND Years_of_experience <= ? ORDER BY Years_of_experience", (q2, q3))
q4_data = fetch_range("SELECT Salary, Years_of_experience FROM my_table WHERE Years_of_experience > ? ORDER BY Years_of_experience", (q3,))

conn.close()

# Ensure directory exists
os.makedirs("quartiles", exist_ok=True)

# Save to CSV
pd.DataFrame(q1_data).to_csv('quartiles/first_fourth.csv', index=False)
pd.DataFrame(q2_data).to_csv('quartiles/second_fourth.csv', index=False)
pd.DataFrame(q3_data).to_csv('quartiles/third_fourth.csv', index=False)
pd.DataFrame(q4_data).to_csv('quartiles/fourth_fourth.csv', index=False)
