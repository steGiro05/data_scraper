import sqlite3
import pandas as pd 
import re

def gini_index(sorted_salaries):
    # Sort salaries in ascending order
    n = len(sorted_salaries)
    total = sum(sorted_salaries)
    
    # Avoid division by zero
    if total == 0:
        return 0

    # Calculate the numerator for the Gini formula
    cumulative = 0
    for i, salary in enumerate(sorted_salaries):
        cumulative += (i + 1) * salary

    gini = (2 * cumulative) / (n * total) - (n + 1) / n
    return gini



result_list=[]
for i in range (1,4):   
    salaries=[] 
    df = pd.read_csv(f'education_level_{i}.csv')

    conn = sqlite3.connect(':memory:')  # In-memory database

    df.to_sql('my_table', conn, index=False, if_exists='replace')

    cursor = conn.cursor()

    cursor.execute("SELECT Salary FROM my_table")
    res= cursor.fetchall()
    for row in res:
        salaries.append(int(row[0]))
    conn.close()
    
    
    gini = gini_index(salaries)
    result_list.append({"Education level": i, "Gini Index": gini})

results_df = pd.DataFrame(result_list)

results_df.to_csv('gini_index.csv', index=False)