import requests
from bs4 import BeautifulSoup
import pandas as pd


seasons=[
    "2019-2020",
    "2020-2021",
    "2021-2022",
    "2022-2023",
    "2023-2024"
]
leagues= [
    "Serie_A",
    "Premier_League",
    "Bundesliga",
    "Ligue_1",
    ]

def search_for_index(table_index, soup):
    # Find all tables
    tables = soup.find_all('table')
    #print(f"Total tables found: {len(tables)}\n")

    # Get the specified table if it exists
    if len(tables) > table_index:
        table = tables[table_index]
        #print(f"Content of table {table_index + 1}:\n")
        #print(table.get_text(separator="\n", strip=True))
        return table
    else:
        #print(f"Table {table_index + 1} does not exist on this page.")
        return None

def extract_columns(table, col_indexes=[2, 3]):
    """
    Extracts specified columns from an HTML table, skipping the header row.
    
    Parameters:
    - table: BeautifulSoup object representing the <table>.
    - col_indexes: List of column indexes to extract (0-based).
    
    Returns:
    - A list of lists, where each inner list is a row with selected columns.
    """
    result = []
    rows = table.find_all('tr')
    
    # Skip the first row (header)
    for row in rows[1:]:  # Start from the second row
        cols = row.find_all(['td', 'th'])  # Handle both header and data cells
        selected = []
        for i in col_indexes:
            if i < len(cols):
                selected.append(cols[i].get_text(strip=True))
            else:
                selected.append("")  # In case the row has fewer columns
        result.append(selected)
    
    return result



# === Configurable variables ===
""" for league in leagues:


    final_results = []
    for season in seasons:
            
        url = f"https://it.wikipedia.org/wiki/{league}_{season}#Classifica_finale"

        # Fetch the page content
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example usage
        table_index = 3 # Change this as needed
        selected_table = search_for_index(table_index, soup)
        extracted = extract_columns(table=selected_table, col_indexes=[2, 3])
        for row in extracted:
            final_results.append({"Name": row[0], "Points": row[1], "Season": season})
            print(row[0], row[1], season)

    results_df = pd.DataFrame(final_results)

    results_df.to_csv(f'{league}.csv', index=False) """
    
#liga
    
final_results = []
for season in seasons:
            
    url = f"https://it.wikipedia.org/wiki/Primera_División_{season}_(Spagna)#Classifica_finale"

    # Fetch the page content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example usage
    table_index = 3 # Change this as needed
    selected_table = search_for_index(table_index, soup)
    extracted = extract_columns(table=selected_table, col_indexes=[2, 3])
    for row in extracted:
        final_results.append({"Name": row[0], "Points": row[1], "Season": season})
        print(row[0], row[1], season)

results_df = pd.DataFrame(final_results)

results_df.to_csv(f'La_Liga.csv', index=False)