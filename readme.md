# Notion Intern Take Home Project

## Overview

The project consists of a Jupyter notebook (`InternTakeHome.ipynb`) that processes a ratings CSV file, performs computations, and generates an output CSV file (`output_file.csv`). Additionally, there's a Python script (`test.py`) that makes an API call to the notion database to populate it with data from the (`output_file.csv`).

## How to Run

1. **Prerequisites:**
    - Make sure you have Python installed on your system.
    - Ensure that your `ratings.csv` file is in the same directory as the `InternTakeHome.ipynb` file and the `test.py` script.

2. **Install Required Packages:**
    ```bash
    pip install requests
    pip install pandas
    ```

    If installation fails, consider upgrading your pip version:
    ```bash
    pip install --upgrade pip
    ```

    If pandas is still not identified, upgrade it:
    ```bash
    pip install pandas --upgrade
    ```

3. **Run the Jupyter Notebook:**
    - Open the `InternTakeHome.ipynb` notebook.
    - Execute the notebook cells to process the ratings and generate the `output_file.csv`.

4. **Replace Notion Token and Database ID:**
    - In the `test.py` script, replace the placeholder values for Notion Token and Database ID with the appropriate information.

5. **Run the Python Script:**
    ```bash
    python test.py
    ```

    If you encounter any issues, ensure that your Notion API integration is set up correctly, and the provided token and database ID are valid.

Feel free to reach out if you have any questions or encounter difficulties during the process.


## Computation Details

1. **Read and Clean Data:**
    - Reads the ratings CSV file.
    - Converts ratings column to integers.
    - Removes leading/trailing whitespaces and converts names to lowercase.

2. **Group and Analyze:**
    - Groups by member name and book name.
    - Selects the last rating by each member for each book.
    - Calculates the mean of ratings and counts how many ratings of 5 each book has.

3. **Generate Output:**
    - Writes the result to "output_file.csv" with NaN values replaced with zero.

## Short Answer Questions

### Challenges Faced

I spent a longer time than expected figuring out the best approach to clean the data, specifically how to select the last rating by a user for a book.

### API Documentation Suggestions

I suggest adding a clearer indication in the API documentation that "connections" may also refer to integrations.

## Major Sources

- [Notion API Status Codes](https://developers.notion.com/reference/status-codes)
- [Create a Notion Integration](https://developers.notion.com/docs/create-a-notion-integration)
- [PyNotion Documentation](https://www.pynotion.com/getting-started-with-python)
- [GeeksforGeeks - Pandas DataFrame GroupBy](https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/)

## Major Open-Source Libraries

- **requests:** To make HTTP requests to the Notion API.
- **json:** Provides methods for working with JSON data.
- **pandas:** Used for data manipulation and analysis of the CSV file.

