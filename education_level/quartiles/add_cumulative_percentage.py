import pandas as pd
import sqlite3

def query_csv(input_csv, output_csv, i):
    result=[]
    # Step 1: Read data from CSV
    df = pd.read_csv(input_csv)

    # Step 2: In-memory SQLite DB
    conn = sqlite3.connect(':memory:')
    df.to_sql('data', conn, index=False, if_exists='replace')
    
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT SUM(Salary) FROM data")
    res= cursor.fetchone()
    sum=res[0]
    
    cursor.execute(f'SELECT Salary FROM data')
    r = cursor.fetchall()
    percentage=0
    for row in r:
        percentage += (row[0] / sum) * 100
        result.append({"Salary": row[0],"Cumulative Percentage":percentage})


    # Step 6: Write to CSV
    pd.DataFrame(result).to_csv(output_csv, index=False)

    conn.close()


for i in range (1,5):
    input_csv = f'{i}_fourth.csv'  # Replace with your input CSV path

    query_csv(input_csv, input_csv, i)
