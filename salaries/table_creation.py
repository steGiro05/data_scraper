import sqlite3
import pandas as pd

league_list = [
    "Serie A TIM",
    "LALIGA EA SPORTS",
    "Bundesliga",
    "Premier League",
    "Ligue 1 Uber Eats",
    "Roshn Saudi League"
]

def league_count(cursor):
    results_list = []

    for league in league_list:
        cursor.execute("SELECT COUNT(*) FROM my_table WHERE division LIKE ?", (f"%{league}%",))
        count = cursor.fetchone()[0]
        results_list.append({"League": league, "Count": count})

    results_df = pd.DataFrame(results_list)

    results_df.to_csv('league_counts.csv', index=False)
    
def salaries_per_league(cursor):

    for league in league_list:
        results_list = []
        cursor.execute("SELECT Name, Salary FROM my_table WHERE division LIKE ?", (f"%{league}%",))
        res = cursor.fetchall()
        for row in res:
            results_list.append({ "Name": row[0],"Salary": row[1]})


        results_df = pd.DataFrame(results_list)
        results_df.to_csv(f'{league}_salaries.csv', index=False)

# Load CSV into a DataFrame
df = pd.read_csv('raw_wages.csv')

# Create an SQLite connection
conn = sqlite3.connect(':memory:')  # In-memory database

# Write the DataFrame to the SQLite database
df.to_sql('my_table', conn, index=False, if_exists='replace')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

#league_count(cursor)
salaries_per_league(cursor)

# Close the connection
conn.close()
