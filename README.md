# Fake Data Generator

A Streamlit application for generating realistic sample datasets without manually writing rows of test data.

[Open the live application](https://ayush-pro-grammer-fake-data-generator-app-t5flun.streamlit.app/)

## Screenshots


<img width="1511" height="858" alt="Screenshot 2026-07-23 at 5 54 41 PM" src="https://github.com/user-attachments/assets/49a65b0f-2e07-4aab-91f7-56c1a0001bcd" />

<img width="1512" height="861" alt="Screenshot 2026-07-23 at 5 55 00 PM" src="https://github.com/user-attachments/assets/b2e530a7-7a73-468c-a91b-73ed58c200d3" />


<img width="1196" height="717" alt="Screenshot 2026-07-23 at 5 55 24 PM" src="https://github.com/user-attachments/assets/b80c1b14-9cae-4841-9359-d4657e62b923" />


<img width="1512" height="859" alt="Screenshot 2026-07-23 at 5 56 00 PM" src="https://github.com/user-attachments/assets/7d8d592d-d9af-4ec1-8205-b536d72977de" />
<img width="1512" height="861" alt="Screenshot 2026-07-23 at 5 55 49 PM" src="https://github.com/user-attachments/assets/ed375182-97ef-4f4a-b394-33290922bbd7" />



<img width="1512" height="545" alt="Screenshot 2026-07-23 at 5 56 36 PM" src="https://github.com/user-attachments/assets/426f30c2-4fde-4eac-b434-753b4ec342ed" />


## Overview

Fake Data Generator is a browser-based application which generates structured sample data for testing, educational purposes, prototyping, forms, tables, APIs and database applications.

The application gives a choice between using pre-made templates and creating custom schema by choosing name and type of each column. Generated data could be previewed inside the application and exported into CSV, JSON and Excel formats.

All the generated data are fake and are intended for use only in development and testing.

## Reasons To Build It

In the course of projects I needed sample data in order to test my tables, forms, backend models and data exports. Entering names, emails, addresses, products and orders manually was a tedious and time-consuming process.

So I decided to develop a useful tool for myself in the course of learning Streamlit which would generate sample datasets fast but at the same time provide a possibility to customize them if needed. Custom fields builder became the most challenging part of development since it required usage of dynamic inputs, validation, session state and various settings depending on data type.


## Features

* Create from 1 up to 10,000 records at once
* Utilize pre-built templates of typical datasets
* Make a custom dataset with a name of your columns and data types
* Modify the amount of custom fields
* Set up value ranges for numeric and date fields
* Create repeatable dataset using a certain random seed
* Spot duplicates of custom columns
* Verify the correctness of number and date ranges before creation
* Preview created records in the table format
* Export created data in CSV, JSON and Excel formats
* Delete the current dataset without closing the application
* Use the application without registration right in your web-browser
  

## Available Templates

| Template  | Information generated                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------- |
| Users     | Names, usernames, emails, phone numbers, DOB, address, location, account created on, and status            |
| Students  | ID, name, course, academic year, semester, marks, attendance, college, city, and admission date           |
| Employees | ID, name, department, designation, company, salary, employment type, location, joining date, and status   |
| Products  | ID, name, category, brand, description, price, discount, stock, rating, number of reviews, SKU, and status|
| Orders    | ID, customer, product(s), quantity, price, total, payment method, status, shipping address, and date     |
| Addresses | ID, name, street address, city, state, country, pincode, latitude, and longitude                       |

## Custom Field Data Types

The schema builder allows for the following data types to be created:

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
* Zipcode
* Company
* Position
* Text
* Integer
* Float
* Boolean
* Date
* Date & Time
* URL
* IPv4
* Color
* Credit Card
* Random Choice

Certain data types have extra options. For instance, integer types can set minimum and maximum values, floating point values can set number of digits after dot, dates can have a range, and random choice can have custom list of choices.


## How to use the app ### Use a template

1. Go to [live app](https://ayush-pro-grammer-fake-data-generator-app-t5flun.streamlit.app/).
2. Choose `Templates` as the generation mode in the sidebar.
3. Specify how many records you want to generate:
4. (Optional) Select Use a fixed seed and type a seed value.
5. Choose a dataset template.
6. Click on `Generate Data`.
7. Examine the generated records in the preview table.
8. Download the data set in CSV, JSON or Excel format.

#### Building Your Own Dataset

1. Choose `Custom Fields` as generation mode.
2. Indicate how many records you wish to create.
3. Name each field with a column name.
4. Select value type for each field.
5. Choose any options displayed for that type.
6. Click on the add-field button to create more columns.
7. Remove any unnecessary fields.
8. Create the data set and preview it.
9. Download it in the needed format.

Using the same fixed seed and same configuration you will generate the same random dataset again. This is useful when you want a test to have predictable inputs.

How It works

The project can be decomposed into two separate Python file.

# app.py

TheStreamlit interface andapplication logicliveshere. This filewill:

* Setup the page layout and sidebar options.
* Set up the twomodes,templates and custom-fields.
*dynamicallygenerate thecustom-fields.
* Manage the session statewith Streamlit.
*validateuserinputs.
* Preview the data.
* Export to CSV, JSON, and Excel formats.
* Clear generated data.


# generate.py

Data generation logic. Handles:

* Faker-generated values such as names, emails, companies, jobs, addresses
* random integer and choice values

* template-specific record generation

* custom fields

* seeded output using both Faker and Python's random module

* record-count check

Generated records are passed to app.py for conversion into a Pandas DataFrame where users can preview and download them. Exported files are generated in memory using openpyxl (no temporary export files need to be saved to the repository).

There is no database underlying the project. Records are held in the session until either they are cleared or the Streamlit session expires.

Tech Stack

| Tech    | Role                    |

| ------- | ----------------------- |

| Python  | All-around              |

| Streamlit | Web Interface/State     |

| Faker   | Realistic Synthetic Data |

| Pandas  | Preview / Data          |

| OpenPyXL | Excel Export            |

| JSON    | JSON Download           |




## Project Structure

```text
fake-data-generator/
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

Struggles and learnings. The first struggle was how to make schema builder dynamic, you would expect that since each field has its own type and different settings then all that information would persist whenever Streamlit would rerun the application. Here, I usedsession state to hold on the generated dataframe and the custom-field's configuration so that they survive reruns while you edit the form. 

Another thing that i have learnt is that generators need validation, and not random values and i got issues in the beginning when trying to generate data using reversed ranges of the date and numeric types,or with duplicated column names or an unparsable format of a datetime. 

So in this solution I included a schema validation phase before actually sending for the generator's work. Another interesting implementation was the Multiple download formats support because I was accustomed to deal with text files so CSV & json had not come up too much struggle but on the other hand Excel download involves writing to an in-memory python file before providing this to download button. Finally the Streamlit project Deployment was very useful, because it helped me to realize the importance of providing in an adequate list of python dependencies in therequirements.txt and understand why is it necessary to run a Streamlit projects from its main script by simply usingstreamlit run app.py and it is impossible to run it like any other python file. ## How I Used Ai: i leveragedChatGPT as my support system throughout the different phases of this project (plan,debug,review and enhance). 

I took his response as a start and verified the output, handled errors, managed deployments, validated downloads, ran test case and managed the different moving parts of the application, also i can understand why these implementation have been put into a specific place.


## Author

Built by Ayush as a Hack Club project.
