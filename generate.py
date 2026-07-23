import random
import uuid
from typing import Any
from faker import Faker

fake = Faker()


def set_seed(seed: int | None = None):
    if seed is not None:
        Faker.seed(seed)
        random.seed()


def generate_users(count: int = 10):

    users = []

    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()

        user = {
            "id": str(uuid.uuid4()),
            "first_name": first_name,
            "last_name": last_name,
            "full_name": f"{first_name} {last_name}",
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "date_of_birth": fake.date_of_birth(
                minimum_age=10, maximum_age=80
            ).isoformat(),
            "gender": random.choice(["Male", "Female", "Other"]),
            "address": fake.address().replace("\n", ","),
            "city": fake.city(),
            "state": fake.state(),
            "postal_code": fake.postcode(),
            "created_at": fake.date_time_between(
                start_date="-2y", end_date="now"
            ).isoformat(),
            "is_active": fake.boolean(chance_of_getting_true=85),
        }

        users.append(user)

    return users


def generate_students(count: int = 10) -> list[dict[str, Any]]:
    """
    Generate fake student records.
    """

    courses = [
        "Computer Science",
        "Information Technology",
        "Mechanical Engineering",
        "Civil Engineering",
        "Electrical Engineering",
        "Business Administration",
        "Commerce",
        "Mathematics",
        "Physics",
        "English",
    ]

    students = []

    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()

        student = {
            "student_id": f"STU-{random.randint(100000, 999999)}",
            "name": f"{first_name} {last_name}",
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "age": random.randint(17, 28),
            "course": random.choice(courses),
            "year": random.randint(1, 4),
            "semester": random.randint(1, 8),
            "percentage": round(random.uniform(45, 98), 2),
            "attendance_percentage": round(random.uniform(50, 100), 2),
            "college": fake.company(),
            "city": fake.city(),
            "admission_date": fake.date_between(
                start_date="-4y",
                end_date="today",
            ).isoformat(),
        }

        students.append(student)

    return students


def generate_employees(count: int = 10) -> list[dict[str, Any]]:
    """
    Generate fake employee records.
    """

    departments = [
        "Engineering",
        "Design",
        "Marketing",
        "Sales",
        "Human Resources",
        "Finance",
        "Customer Support",
        "Operations",
        "Legal",
        "Management",
    ]

    job_titles = [
        "Software Developer",
        "Frontend Developer",
        "Backend Developer",
        "UI Designer",
        "Product Manager",
        "Data Analyst",
        "Marketing Executive",
        "Sales Manager",
        "HR Specialist",
        "Accountant",
        "Support Engineer",
        "Operations Manager",
    ]

    employees = []

    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()

        employee = {
            "employee_id": f"EMP-{random.randint(10000, 99999)}",
            "name": f"{first_name} {last_name}",
            "email": fake.company_email(),
            "phone_number": fake.phone_number(),
            "department": random.choice(departments),
            "job_title": random.choice(job_titles),
            "company": fake.company(),
            "salary": random.randint(25000, 250000),
            "joining_date": fake.date_between(
                start_date="-10y",
                end_date="today",
            ).isoformat(),
            "employment_type": random.choice(
                ["Full-time", "Part-time", "Contract", "Intern"]
            ),
            "work_location": random.choice(["Office", "Remote", "Hybrid"]),
            "city": fake.city(),
            "is_active": fake.boolean(chance_of_getting_true=90),
        }

        employees.append(employee)

    return employees


def generate_products(count: int = 10):
    categories = [
        "Electronics",
        "Clothing",
        "Home & Kitchen",
        "Books",
        "Toys & Games",
        "Sports & Outdoors",
        "Beauty & Personal Care",
        "Health & Wellness",
        "Automotive",
        "Grocery & Gourmet Food",
    ]

    product_adjectives = [
        "Portable",
        "Wireless",
        "Smart",
        "Eco-friendly",
        "Durable",
        "Compact",
        "Lightweight",
        "High-performance",
        "Multi-functional",
        "Premium",
    ]

    product_types = [
        "Headphones",
        "Backpack",
        "Blender",
        "Novel",
        "Board Game",
        "Yoga Mat",
        "Skincare Set",
        "Vitamins",
        "Car Vacuum Cleaner",
        "Organic Coffee",
    ]

    products = []

    for _ in range(count):
        price = round(random.uniform(100, 50000), 2)
        discount_percentage = random.choice([0, 5, 10, 15, 20, 25, 30])

        discounted_price = round(
            price - (price * discount_percentage / 100),
            2,
        )

        product = {
            "product_id": f"PRD-{random.randint(100000, 999999)}",
            "product_name": f"{random.choice(product_adjectives)} {random.choice(product_types)}",
            "category": random.choice(categories),
            "brand": fake.company(),
            "description": fake.sentence(nb_words=12),
            "price": price,
            "discount_percentage": discount_percentage,
            "discount_price": discounted_price,
            "stock_quantity": random.randint(0, 5000),
            "rating": round(random.uniform(1, 5), 1),
            "review_count": random.randint(0, 10000),
            "sku": fake.bothify(text="SKU-####-????").upper(),
            "created_at": fake.date_time_between(
                start_date="-3y", end_date="now"
            ).isoformat(),
            "is_available": fake.boolean(chance_of_getting_true=90),
        }

        products.append(product)

    return products


def generate_orders(count: int = 10):

    payment_methods = [
        "Credit Card",
        "Debit Card",
        "UPI",
        "Net Banking",
        "Cash on Delivery",
        "Wallet",
    ]

    order_status = [
        "Pending",
        "Confirmed",
        "Shipped",
        "Delivered",
        "Cancelled",
        "Returned",
    ]

    orders = []

    for _ in range(count):
        quantity = random.randint(1, 10)
        unit_price = round(random.uniform(100, 10000), 2)

        order = {
            "order_id": f"ORD-{random.randint(100000, 999999)}",
            "customer_name": f"{fake.first_name()} {fake.last_name()}",
            "customer_email": fake.email(),
            "product_name": fake.catch_phrase(),
            "quantity": quantity,
            "unit_price": unit_price,
            "payment_method": random.choice(payment_methods),
            "order_status": random.choice(order_status),
            "shipping_address": fake.address().replace("\n", ","),
            "order_date": fake.date_time_between(
                start_date="-1y", end_date="now"
            ).isoformat(),
        }

        orders.append(order)


def generate_addresses(count: int = 10):

    addresses = []

    for _ in range(count):
        address = {
            "address_id": str(uuid.uuid4()),
            "name": fake.name(),
            "street_address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "postal_code": fake.postal_code(),
            "country": fake.country(),
            "latitude": fake.latitude(),
            "longitude": fake.longitude(),
        }

        addresses.append(address)

    return addresses



fake = Faker()


def generate_custom_value(field_type: str, options: dict[str, Any] | None = None):

    options = options or {}

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

    if field_type == "Text":
        return fake.sentence(nb_words=options.get("max_length", 10))

    if field_type == "Integer":
        minimum = options.get("minimum", 0)
        maximum = options.get("maximum", 100)

        return random.randint(minimum, maximum)

    if field_type == "Float":
        minimum = options.get("minimum", 0.0)
        maximum = options.get("maximum", 100.0)
        decimal_places = options.get("decimal_places", 2)

        return round(random.uniform(minimum, maximum), decimal_places)

    if field_type == "Boolean":
        return random.choice([True, False])

    if field_type == "Date":
        return fake.date_between(
            start_date=options.get("start_date", "-30y"),
            end_date=options.get("end_date", "today"),
        )

    if field_type == "Date and Time":
        return fake.date_time_between(
            start_date="-2y",
            end_date="now",
        ).isoformat()

    if field_type == "URL":
        return fake.url()

    if field_type == "IPv4 Address":
        return fake.ipv4()

    if field_type == "Color":
        return fake.hex_color()

    if field_type == "Credit Card":
        return fake.credit_card_number()

    if field_type == "Random Choice":
        choices = optoins.get("choices", ["Option 1", "Option 2", "Option 3"])

        return random.choice(choices)

    return fake.word()


def generate_custom_data(
    count: int,
    fields: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    records = []

    for _ in range(count):
        record = {}

        for field in fields:
            field_name = field.get("name", "field")
            field_type = field.get("type", "Text")
            field_options = field.get("options", {})

            record[field_name] = generate_custom_value(
                field_type=field_type,
                options=field_options,
            )

        records.append(record)

    return records


def generate_data(data_type: str, count: int, seed: int | None = None):

    if count < 1:
        raise ValueError("Count must be greater than 0")

    if count > 10000:
        raise ValueError("Count must be less than or equal to 10000")

    set_seed(seed)

    generators = {
        "Users": generate_users,
        "Students": generate_students,
        "Employees": generate_employees,
        "Products": generate_products,
        "Orders": generate_orders,
        "Addresses": generate_addresses,
    }

    generator = generators.get(data_type)

    if generator is None:
        raise ValueError(f"Invalid data type: {data_type}")

    return generator(count)
