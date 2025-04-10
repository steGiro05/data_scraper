import sqlite3
import pandas as pd 
import re

def gini_index(sorted_salaries):
    
    return gini



result_list=[]
quartiles=[
    0,
    3.0,
    7.0,
    12.0,
    50.0
]
for i in range (1,5):   
    salaries=[] 
    df = pd.read_csv(f'{i}_fourth.csv')

    conn = sqlite3.connect(':memory:')  # In-memory database

    df.to_sql('my_table', conn, index=False, if_exists='replace')

    cursor = conn.cursor()

    cursor.execute("SELECT Salary FROM my_table")
    res= cursor.fetchall()
    for row in res:
        salaries.append(int(row[0]))
    conn.close()
    
    
    gini = gini_index(salaries)
    result_list.append({"Years of experience": f'{quartiles[i-1]} - {quartiles[i]}', "Gini Index": gini})

results_df = pd.DataFrame(result_list)

results_df.to_csv('gini_index.csv', index=False)