import random
import uuid 
from typing import Any 
from datetime import date, datetime 
from faker import Faker 


fake = Faker()

def generate_custom_value(field_type: str, options: dict[str, Any] | None = None):

    optoins = options or {}

    if field_type == "Full Name":
        return fake.name() 

    if field_type == "First Name":
        return fake.first_name()

    if field_type == "Last Name":
        return fake.last_name() 

    if field_type == "Email":
        return fake.email() 

    if field_type == "Phone Number":
        return fake.phone_number()

    if field_type == "Username":
        return fake.user_name() 

    if field_type == "Phone Number":
        return fake.phone_number()


    if field_type == "Address":
        return fake.address() 

    if field_type == "City":
        return fake.city()

    if field_type == "State":
        return fake.state()

    if field_type == "Country":
        return fake.country() 


    if field_type == "Postal Code":
        return fake.postcode()

    if field_type == "Company":
        return fake.company() 

    if field_type == "Job Title":
        return fake.job() 

    if field_type == 'Text':
        return fake.sentence(nb_words=options.get('max_length', 10))




    if field_type == 'Integer':
        minimum = options.get("minimum", 0)
        maximum = options.get("maximum", 100)

        return random.randint(minimum, maximum)

    if field_type == 'Float':
        minimum = options.get('minimum', 0.0)
        maximum = options.get('maximum', 100.0)
        decimal_places = options.get('decimal_places', 2)


        return round(random.uniform(minimum, maximum), decimal_places)

    if field_type == 'Boolean':
        return random.choice([True, False])

    if field_type == 'Date':
        return fake.date_between(start_date=options.get('start_date', '-30y'), end_date=options.get('end_date', 'today'))

    if field_type == 'Date and Time':
        return fake.date_time_between(
            start_date = '-2y',
            end_date = 'now',
        ).isoformat()


    if field_type == 'URL':
        return fake.url() 


    if field_type == "IPv4 Address":
        return fake.ipv4()

    if field_type == "Color":
        return fake.hex_color() 

    if field_type == 'Credit Card':
        return fake.credit_card_number() 

    if field_type == 'Random Choice':
        choices = optoins.get('choices', ['Option 1', 'Option 2', 'Option 3'])

        return random.choice(choices)


    return fake.word()



    
