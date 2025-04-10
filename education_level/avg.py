import sqlite3
import pandas as pd 
import re

result_list=[]

for i in range (1,4):   
    salaries=[] 
    df = pd.read_csv(f'education_level_{i}.csv')

    conn = sqlite3.connect(':memory:')  # In-memory database

    df.to_sql('my_table', conn, index=False, if_exists='replace')

    cursor = conn.cursor()

    cursor.execute("SELECT AVG(Salary) FROM my_table")
    res= cursor.fetchone()
    avg_salary = res[0]
    conn.close()
    
    
    result_list.append({"Education level": f'{i}', "Average": avg_salary})

results_df = pd.DataFrame(result_list)

results_df.to_csv('avg.csv', index=False)