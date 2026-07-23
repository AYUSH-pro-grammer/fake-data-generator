import json
from io import BytesIO

import pandas as pd
import streamlit as st

from generate import (
    generate_custom_data,
    generate_data,
    set_seed,
)


st.set_page_config(
    page_title="Fake Data Generator",
    page_icon="🎲",
    layout="wide",
)


if "generated_data" not in st.session_state:
    st.session_state.generated_data = []


if "custom_fields" not in st.session_state:
    st.session_state.custom_fields = [
        {
            "name": "full_name",
            "type": "Full Name",
            "options": {},
        },
        {
            "name": "email",
            "type": "Email",
            "options": {},
        },
    ]


def dataframe_to_excel(dataframe: pd.DataFrame):

    # convert pandas df to excel

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl",
    ) as writer:
        dataframe.to_excel(writer, index=False, sheet_name="Fake Data")

    output.seek(0)
    return output.getvalue()


def reset_generated_data():
    st.session_state.generated_data = []


def add_custom_field() -> None:
    """
    Add a new field to the custom-field list.
    """

    field_number = len(st.session_state.custom_fields) + 1

    new_field = {
        "name": f"field_{field_number}",
        "type": "Text",
        "options": {},
    }

    st.session_state.custom_fields.append(new_field)


def remove_custom_field(
    field_index: int,
) -> None:
    """
    Remove one field using its list index.
    """

    if len(st.session_state.custom_fields) <= 1:
        return

    st.session_state.custom_fields.pop(field_index)


def clean_field_name(
    field_name: str,
    field_index: int,
) -> str:
    """
    Prepare a field name for dictionary and column use.
    """

    cleaned_name = field_name.strip().lower().replace(" ", "_")

    if not cleaned_name:
        cleaned_name = f"field_{field_index + 1}"

    return cleaned_name


def find_duplicate_names(
    fields: list[dict],
) -> set[str]:
    """
    Return duplicated custom-field names.
    """

    field_names = [field["name"] for field in fields]

    duplicate_names = {name for name in field_names if field_names.count(name) > 1}

    return duplicate_names


def has_invalid_range(
    fields: list[dict],
) -> bool:
    """
    Check number and date range settings.
    """

    for field in fields:
        field_type = field.get("type")
        options = field.get("options", {})

        if field_type in ["Integer", "Float"]:
            minimum = options.get(
                "minimum",
                0,
            )

            maximum = options.get(
                "maximum",
                0,
            )

            if minimum > maximum:
                return True

        if field_type == "Date":
            start_date = options.get("start_date")

            end_date = options.get("end_date")

            if start_date > end_date:
                return True

    return False


# Main header


st.title("Fake Data Generator")

st.write(
    "Generate users, students, employees, "
    "products, orders, addresses, or your "
    "own custom datasets."
)

st.divider()


# Sidebar


with st.sidebar:
    st.header("Generator Settings")

    generator_mode = st.radio(
        label="Generation mode",
        options=[
            "Templates",
            "Custom Fields",
        ],
    )

    record_count = st.number_input(
        label="Number of records",
        min_value=1,
        max_value=10000,
        value=20,
        step=1,
    )

    use_seed = st.checkbox(
        label="Use a fixed seed",
        help=("Using the same seed generates the same random data again."),
    )

    seed = None

    if use_seed:
        seed = st.number_input(
            label="Seed value",
            min_value=0,
            max_value=999999,
            value=42,
            step=1,
        )

    st.divider()

    clear_button = st.button(
        label="Clear Generated Data",
        use_container_width=True,
    )

    if clear_button:
        reset_generated_data()
        st.rerun()


# Available custom field types


FIELD_TYPES = [
    "Full Name",
    "First Name",
    "Last Name",
    "Email",
    "Username",
    "Phone Number",
    "Address",
    "City",
    "State",
    "Country",
    "Postal Code",
    "Company",
    "Job Title",
    "Text",
    "Integer",
    "Float",
    "Boolean",
    "Date",
    "Date and Time",
    "URL",
    "IPv4 Address",
    "Color",
    "Credit Card",
    "Random Choice",
]


# Available templates


TEMPLATE_TYPES = [
    "Users",
    "Students",
    "Employees",
    "Products",
    "Orders",
    "Addresses",
]


# next part


# Template descriptions


TEMPLATE_DESCRIPTIONS = {
    "Users": (
        "Generate user profiles containing names, "
        "emails, usernames, phone numbers, addresses, "
        "birth dates, and account information."
    ),
    "Students": (
        "Generate student details containing courses, "
        "semesters, percentages, attendance, and "
        "admission information."
    ),
    "Employees": (
        "Generate employee details containing departments, "
        "job titles, salaries, joining dates, and "
        "employment information."
    ),
    "Products": (
        "Generate product details containing categories, "
        "prices, discounts, stock, ratings, and SKUs."
    ),
    "Orders": (
        "Generate order details containing customers, "
        "products, quantities, payments, and order status."
    ),
    "Addresses": (
        "Generate address details containing streets, "
        "cities, states, countries, postal codes, "
        "and coordinates."
    ),
}


# Template generator


if generator_mode == "Templates":
    st.subheader("Choose a Dataset Template")

    template_type = st.selectbox(
        label="Select data type",
        options=TEMPLATE_TYPES,
    )

    st.info(TEMPLATE_DESCRIPTIONS[template_type])

    generate_template_button = st.button(
        label="Generate Data",
        type="primary",
        use_container_width=True,
    )

    if generate_template_button:
        try:
            generated_records = generate_data(
                data_type=template_type,
                count=int(record_count),
                seed=(int(seed) if seed is not None else None),
            )

            st.session_state.generated_data = generated_records

            st.success(
                f"Generated {len(generated_records)} {template_type.lower()} records."
            )

        except Exception as error:
            st.error(f"Could not generate data: {error}")


# Custom field generator


else:
    st.subheader("Build a Custom Dataset")

    st.write(
        "Create your own columns and choose what "
        "kind of fake value each column should contain."
    )

    updated_fields = []

    for field_index, saved_field in enumerate(st.session_state.custom_fields):
        with st.container(border=True):
            heading_column, remove_column = st.columns([8, 1])

            with heading_column:
                st.markdown(f"#### Field {field_index + 1}")

            with remove_column:
                remove_button = st.button(
                    label="X",
                    key=f"remove_field_{field_index}",
                    help="Remove this field",
                    disabled=(len(st.session_state.custom_fields) <= 1),
                )

                if remove_button:
                    remove_custom_field(field_index)

                    st.rerun()

            name_column, type_column = st.columns(2)

            with name_column:
                field_name = st.text_input(
                    label="Column name",
                    value=saved_field.get(
                        "name",
                        f"field_{field_index + 1}",
                    ),
                    key=f"field_name_{field_index}",
                )

            with type_column:
                saved_type = saved_field.get(
                    "type",
                    "Text",
                )

                if saved_type in FIELD_TYPES:
                    selected_type_index = FIELD_TYPES.index(saved_type)
                else:
                    selected_type_index = 0

                field_type = st.selectbox(
                    label="Value type",
                    options=FIELD_TYPES,
                    index=selected_type_index,
                    key=f"field_type_{field_index}",
                )

            field_options = {}

            # Text settings

            if field_type == "Text":
                current_options = saved_field.get(
                    "options",
                    {},
                )

                word_count = st.number_input(
                    label="Approximate word count",
                    min_value=1,
                    max_value=100,
                    value=int(
                        current_options.get(
                            "max_length",
                            10,
                        )
                    ),
                    step=1,
                    key=f"text_length_{field_index}",
                )

                field_options["max_length"] = int(word_count)

                # Integer settings

            elif field_type == "Integer":
                current_options = saved_field.get(
                    "options",
                    {},
                )

                minimum_column, maximum_column = st.columns(2)

                with minimum_column:
                    minimum = st.number_input(
                        label="Minimum value",
                        value=int(
                            current_options.get(
                                "minimum",
                                0,
                            )
                        ),
                        step=1,
                        key=(f"integer_minimum_{field_index}"),
                    )

                with maximum_column:
                    maximum = st.number_input(
                        label="Maximum value",
                        value=int(
                            current_options.get(
                                "maximum",
                                100,
                            )
                        ),
                        step=1,
                        key=(f"integer_maximum_{field_index}"),
                    )

                field_options["minimum"] = int(minimum)

                field_options["maximum"] = int(maximum)

                # Float settings

            elif field_type == "Float":
                current_options = saved_field.get(
                    "options",
                    {},
                )

                minimum_column, maximum_column = st.columns(2)

                with minimum_column:
                    minimum = st.number_input(
                        label="Minimum value",
                        value=float(
                            current_options.get(
                                "minimum",
                                0.0,
                            )
                        ),
                        key=(f"float_minimum_{field_index}"),
                    )

                with maximum_column:
                    maximum = st.number_input(
                        label="Maximum value",
                        value=float(
                            current_options.get(
                                "maximum",
                                100.0,
                            )
                        ),
                        key=(f"float_maximum_{field_index}"),
                    )

                decimal_places = st.slider(
                    label="Decimal places",
                    min_value=0,
                    max_value=8,
                    value=int(
                        current_options.get(
                            "decimal_places",
                            2,
                        )
                    ),
                    key=(f"float_decimal_places_{field_index}"),
                )

                field_options["minimum"] = float(minimum)

                field_options["maximum"] = float(maximum)

                field_options["decimal_places"] = int(decimal_places)

                # Date settings

            elif field_type == "Date":
                current_options = saved_field.get(
                    "options",
                    {},
                )

                default_start_date = current_options.get(
                    "start_date",
                    pd.Timestamp("2000-01-01").date(),
                )

                default_end_date = current_options.get(
                    "end_date",
                    pd.Timestamp.today().date(),
                )

                if isinstance(default_start_date, str):
                    default_start_date = pd.to_datetime(default_start_date).date()

                if isinstance(default_end_date, str):
                    default_end_date = pd.to_datetime(default_end_date).date()

                start_column, end_column = st.columns(2)

                with start_column:
                    start_date = st.date_input(
                        label="Start date",
                        value=default_start_date,
                        key=f"date_start_{field_index}",
                    )

                with end_column:
                    end_date = st.date_input(
                        label="End date",
                        value=default_end_date,
                        key=f"date_end_{field_index}",
                    )

                field_options["start_date"] = start_date
                field_options["end_date"] = end_date

                # Random choice settings

            elif field_type == "Random Choice":
                current_options = saved_field.get(
                    "options",
                    {},
                )

                saved_choices = current_options.get(
                    "choices",
                    [
                        "Option 1",
                        "Option 2",
                        "Option 3",
                    ],
                )

                choices_text = st.text_area(
                    label="Choices",
                    value=", ".join(saved_choices),
                    placeholder=("Pending, Processing, Completed"),
                    help=("Separate each choice using a comma."),
                    key=f"random_choices_{field_index}",
                )

                choices = [
                    choice.strip()
                    for choice in choices_text.split(",")
                    if choice.strip()
                ]

                if not choices:
                    choices = [
                        "Option 1",
                        "Option 2",
                    ]

                field_options["choices"] = choices

                # Save the configured field

            cleaned_field_name = clean_field_name(
                field_name=field_name,
                field_index=field_index,
            )

            updated_fields.append(
                {
                    "name": cleaned_field_name,
                    "type": field_type,
                    "options": field_options,
                }
            )

    # Save updated field configuration after
    # every Streamlit rerun.

    st.session_state.custom_fields = updated_fields

    # Custom field action buttons

    add_column, generate_column = st.columns(2)

    with add_column:
        add_field_button = st.button(
            label="Add Another Field",
            use_container_width=True,
        )

        if add_field_button:
            add_custom_field()
            st.rerun()

    with generate_column:
        generate_custom_button = st.button(
            label="Generate Custom Data",
            type="primary",
            use_container_width=True,
        )

    # Generate custom records

    if generate_custom_button:
        duplicate_names = find_duplicate_names(st.session_state.custom_fields)

        invalid_range = has_invalid_range(st.session_state.custom_fields)

        empty_random_choices = []

        for field in st.session_state.custom_fields:
            if field.get("type") == "Random Choice":
                field_choices = field.get(
                    "options",
                    {},
                ).get(
                    "choices",
                    [],
                )

                if not field_choices:
                    empty_random_choices.append(field.get("name", "field"))

        if duplicate_names:
            duplicate_text = ", ".join(sorted(duplicate_names))

            st.error(
                "Every column must have a unique name. "
                f"Duplicate names: {duplicate_text}"
            )

        elif invalid_range:
            st.error(
                "One or more ranges are invalid. "
                "The minimum value must not be greater "
                "than the maximum value, and the start "
                "date must not be after the end date."
            )

        elif empty_random_choices:
            invalid_fields = ", ".join(empty_random_choices)

            st.error(
                "Random Choice fields must contain at "
                f"least one choice: {invalid_fields}"
            )

        else:
            try:
                selected_seed = int(seed) if seed is not None else None

                set_seed(selected_seed)

                generated_records = generate_custom_data(
                    count=int(record_count),
                    fields=st.session_state.custom_fields,
                )

                st.session_state.generated_data = generated_records

                st.success(f"Generated {len(generated_records)} custom records.")

            except Exception as error:
                st.error(f"Could not generate custom data: {error}")


# Generated data preview


if st.session_state.generated_data:
    st.divider()

    st.subheader("Generated Data")

    dataframe = pd.DataFrame(st.session_state.generated_data)

    record_metric, column_metric = st.columns(2)

    with record_metric:
        st.metric(
            label="Records",
            value=len(dataframe),
        )

    with column_metric:
        st.metric(
            label="Columns",
            value=len(dataframe.columns),
        )

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True,
        height=450,
    )

    # Download file preparation

    csv_data = dataframe.to_csv(index=False).encode("utf-8")

    json_data = json.dumps(
        st.session_state.generated_data,
        indent=4,
        default=str,
    )

    try:
        excel_data = dataframe_to_excel(dataframe)

    except Exception as error:
        excel_data = None

        st.warning(f"Excel download could not be prepared. Error: {error}")

    st.subheader("Download Dataset")

    csv_column, json_column, excel_column = st.columns(3)

    # CSV download

    with csv_column:
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="fake_data.csv",
            mime="text/csv",
            use_container_width=True,
        )

    # JSON download

    with json_column:
        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name="fake_data.json",
            mime="application/json",
            use_container_width=True,
        )

    # Excel download

    with excel_column:
        st.download_button(
            label="Download Excel",
            data=(excel_data if excel_data is not None else b""),
            file_name="fake_data.xlsx",
            mime=("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
            use_container_width=True,
            disabled=excel_data is None,
        )


else:
    st.divider()

    st.info(
        "Configure the generator and click the "
        "Generate Data button to preview your dataset."
    )
