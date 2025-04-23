from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL to scrape
url = 'https://www.census.gov/retail/marts/www/adv44W72.txt'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text content
    data = soup.get_text()

    # Convert the data into a pandas DataFrame
    data_lines = data.splitlines()[1:]  # Split the text into lines
    data_list = [line.split() for line in data_lines if line.strip()]  # Split each line into columns

    # Create a DataFrame
    df = pd.DataFrame(data_list)

    # Convert the first row as column names
    df.columns = df.iloc[0]  # Set the first row as column names
    df = df[1:]  # Remove the first row from the data

    # Reset the index without keeping the old index as a column
    df.reset_index(drop=True, inplace=True)

    # Delete the last two rows of the DataFrame
    df = df[:-2]  # Keep all rows except the last two

    # Debugging: Print the first few rows of the DataFrame to inspect the data
    print("Initial DataFrame:")
    print(df.head())

    # Create a new DataFrame by combining the YEAR column with month columns (JAN-DEC)
    new_data = []
    for index, row in df.iterrows():
        year = row['YEAR']
        for month in ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']:
            if month in df.columns:
                new_data.append({
                    'Month-Year': f"{month}-{year}",
                    'Value': row[month]
                })

    # Convert the list of dictionaries into a new DataFrame
    new_df = pd.DataFrame(new_data)

    # Debugging: Print the new DataFrame
    print("New DataFrame with Month-Year and Values:")
    print(new_df.head())

    # Export the new DataFrame to a CSV file named 'sales_data.csv'
    new_df.to_csv('sales_data.csv', index=False)

    print("New DataFrame has been exported to 'sales_data.csv'.")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")