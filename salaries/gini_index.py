import sqlite3
import pandas as pd 
import re

league_list = [
    "Serie A TIM",
    "LALIGA EA SPORTS",
    "Bundesliga",
    "Premier League",
    "Ligue 1 Uber Eats",
    "Roshn Saudi League"
]

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


def cast_integer(s):
    return re.sub(r'\D', '', s)

result_list=[]
for league in league_list:   
    salaries=[] 
    df = pd.read_csv(f'{league}_salaries.csv')

    conn = sqlite3.connect(':memory:')  # In-memory database

    df.to_sql('my_table', conn, index=False, if_exists='replace')

    cursor = conn.cursor()

    cursor.execute("SELECT salary FROM my_table")
    res= cursor.fetchall()
    for row in res:
        salaries.append(int(cast_integer(row[0])))
    conn.close()
    
    sorted_salaries=salaries[::-1]
    gini = gini_index(sorted_salaries)
    result_list.append({"League": league, "Gini Index": gini})

results_df = pd.DataFrame(result_list)

results_df.to_csv('gini_index.csv', index=False)
