# Fake Data Generator

A Streamlit application for generating realistic sample datasets without manually writing rows of test data.

[Open the live application](https://ayush-pro-grammer-fake-data-generator-app-t5flun.streamlit.app/)

## Screenshots

![Template generation mode](assets/template-mode.png)

![Custom schema builder](assets/custom-fields-mode.png)

![Generated data preview and downloads](assets/data-preview.png)

## Overview

Fake Data Generator is a browser-based tool that creates structured sample data for testing, learning, prototypes, forms, tables, APIs, and database projects.

The app provides two ways to create a dataset. A user can select one of the ready-made templates or build a custom schema by choosing the name and type of every column. The generated records can be previewed inside the app and downloaded as CSV, JSON, or Excel files.

All generated values are synthetic and are intended only for development and testing.

## Why I Built It

While working on projects, I often needed sample records to test tables, forms, backend models, and data exports. Writing names, emails, addresses, products, and order information manually was repetitive and made it harder to test with larger datasets.

I wanted to build something practical while learning Streamlit: a single tool that could generate ready-made datasets quickly but still give the user control when a fixed template was not enough. The custom field builder became the most interesting part because it required dynamic inputs, validation, session state, and different settings for different data types.

## Features

* Generate between 1 and 10,000 records at a time
* Use ready-made templates for common datasets
* Build a custom dataset with user-defined column names and value types
* Add or remove custom fields dynamically
* Configure ranges for numeric and date fields
* Create repeatable datasets with a fixed random seed
* Detect duplicate custom column names
* Validate invalid number and date ranges before generation
* Preview generated records in a table
* Download generated data as CSV, JSON, or Excel
* Clear the current generated dataset without restarting the app
* Use the application directly in a browser without creating an account

## Available Templates

| Template  | Generated information                                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Users     | Names, usernames, emails, phone numbers, dates of birth, addresses, locations, account dates, and active status                |
| Students  | Student IDs, names, courses, academic year, semester, marks, attendance, college, city, and admission date                     |
| Employees | Employee IDs, names, departments, job titles, companies, salaries, employment type, work location, joining date, and status    |
| Products  | Product IDs, names, categories, brands, descriptions, prices, discounts, stock, ratings, review counts, SKUs, and availability |
| Orders    | Order IDs, customers, products, quantities, prices, totals, payment methods, order status, shipping addresses, and dates       |
| Addresses | IDs, names, street addresses, cities, states, countries, postal codes, latitude, and longitude                                 |

## Custom Field Types

The custom schema builder supports the following value types:

* Full Name
* First Name
* Last Name
* Email
* Username
* Phone Number
* Address
* City
* State
* Country
* Postal Code
* Company
* Job Title
* Text
* Integer
* Float
* Boolean
* Date
* Date and Time
* URL
* IPv4 Address
* Color
* Credit Card
* Random Choice

Some types provide additional controls. For example, numeric fields can use minimum and maximum values, float fields can use a selected number of decimal places, date fields can use a date range, and random-choice fields can use a custom list of choices.

## How to Use the App

### Using a Template

1. Open the [live application](https://ayush-pro-grammer-fake-data-generator-app-t5flun.streamlit.app/).
2. Select `Templates` from the generation mode in the sidebar.
3. Enter the number of records to generate.
4. Optionally enable `Use a fixed seed` and enter a seed value.
5. Select a dataset template.
6. Click `Generate Data`.
7. Review the generated records in the preview table.
8. Download the dataset as CSV, JSON, or Excel.

### Building a Custom Dataset

1. Select `Custom Fields` from the generation mode.
2. Enter the number of records to generate.
3. Give each field a column name.
4. Select the value type for each field.
5. Configure any options shown for that type.
6. Use the add-field button to create more columns.
7. Remove fields that are not required.
8. Generate the dataset and check the preview.
9. Download it in the required format.

Using the same fixed seed with the same configuration produces the same random dataset again. This is useful when a test needs predictable input.

## How It Works

The project is divided into two main Python files.

### `app.py`

This file contains the Streamlit interface and application flow. It handles:

* Page layout and sidebar controls
* Template and custom-field modes
* Dynamic custom fields
* Streamlit session state
* Input validation
* Data preview
* CSV, JSON, and Excel exports
* Clearing generated data

### `generate.py`

This file contains the data-generation logic. It handles:

* Faker-based values such as names, emails, companies, jobs, and addresses
* Random numeric and choice-based values
* Template-specific record generation
* Custom field generation
* Seeded output using Faker and Python's `random` module
* Record-count validation

After records are generated, `app.py` converts them into a Pandas DataFrame for previewing and exporting. Excel files are created in memory with `openpyxl`, so the app does not need to save temporary export files to the repository.

The project does not use a database. Generated records are kept in the current Streamlit session until they are cleared or the session ends.

## Tech Stack

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Main programming language           |
| Streamlit  | Web interface and session state     |
| Faker      | Realistic synthetic values          |
| Pandas     | Tabular preview and data conversion |
| OpenPyXL   | Excel file generation               |
| JSON       | JSON serialization and download     |

## Project Structure

```text
fake-data-generator/
├── assets/
│   ├── template-mode.png
│   ├── custom-fields-mode.png
│   └── data-preview.png
├── app.py
├── generate.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

`venv/` and `__pycache__/` are local generated folders and should not be committed.

## Running Locally

### Requirements

* Python 3.10 or newer
* Git
* `pip`

### Installation

Clone the repository:

```bash
git clone https://github.com/ayush-pro-grammer/fake-data-generator.git
cd fake-data-generator
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will print a local address, usually `http://localhost:8501`, which can be opened in a browser.

## Dependencies

The project uses these Python packages:

```text
streamlit
pandas
faker
openpyxl
```

They are listed in `requirements.txt` so the application can be reproduced locally and deployed on Streamlit Community Cloud.

## Challenges and What I Learned

The main challenge was making the custom schema builder dynamic. Every field can have a different type and different settings, but those values still need to survive Streamlit reruns. I used session state to keep the generated dataset and the custom-field configuration available while the user edits the form.

I also learned that a generator needs validation, not just random values. Duplicate column names, reversed numeric ranges, and invalid date ranges can create confusing output, so I added checks before generation.

Another useful part was implementing multiple download formats. CSV and JSON are text-based, but Excel generation required writing the DataFrame to an in-memory file before giving it to Streamlit's download button.

Finally, deploying the app helped me understand how Python dependencies must be listed in `requirements.txt` and why a Streamlit project must be started with `streamlit run app.py` instead of running the file as a normal Python script.

## AI Assistance

I used ChatGPT as a support tool while planning, debugging, reviewing, and improving parts of this project. I did not treat its suggestions as finished work. I ran the application, fixed errors, tested the generator and downloads, handled deployment issues, and worked through how the different parts fit together.

I understand the code and can explain the template generators, custom schema flow, session state, validation, seeded generation, and export logic.

## Current Limitations

* Generated records are independent; the app does not currently create relationships between multiple tables.
* The generator uses one default Faker locale.
* Custom schemas cannot yet be saved and loaded later.
* The maximum generation size is 10,000 records per run.
* Generated values are for testing and must not be treated as verified personal, financial, or production data.

## Future Improvements

* Add locale selection for country-specific names, addresses, and phone numbers
* Allow users to save and import custom schemas
* Generate related datasets using shared IDs
* Add SQL export
* Add more ready-made templates
* Add optional uniqueness rules for selected columns
* Show basic statistics about the generated dataset

## Credits

* [Streamlit](https://streamlit.io/) for the web application framework
* [Faker](https://faker.readthedocs.io/) for synthetic data generation
* [Pandas](https://pandas.pydata.org/) for tabular data handling
* [OpenPyXL](https://openpyxl.readthedocs.io/) for Excel export support

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Built by Ayush as a Hack Club project.
