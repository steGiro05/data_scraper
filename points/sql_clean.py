import pandas as pd
import sqlite3

def query_csv(input_csv, output_csv, query):
    # Step 1: Read data from the input CSV into a pandas DataFrame
    df = pd.read_csv(input_csv)

    # Step 2: Create an SQLite in-memory database
    conn = sqlite3.connect(':memory:')  # In-memory database
    df.to_sql('data', conn, index=False, if_exists='replace')

    # Step 3: Execute the SQL query on the data
    result = pd.read_sql_query(query, conn)

    # Step 4: Write the result to the output CSV
    result.to_csv(output_csv, index=False)

    # Close the database connection
    conn.close()

leagues= [
    "Serie_A",
    "Premier_League",
    "Bundesliga",
    "Ligue_1",
    "La_Liga",
]

for league in leagues:
    input_csv = f'{league}.csv'  # Replace with your input CSV path
    output_csv = f'clean_data/{league}_clean.csv'  # Replace with your output CSV path
    query = 'SELECT Name, sum(Points) as sum_points FROM data GROUP BY Name ORDER BY sum_points'  # Modify the query

    query_csv(input_csv, output_csv, query)
