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
            page_icon="=",
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
        engine = "openpyxl",

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

    field_number = (
        len(st.session_state.custom_fields) + 1
    )

    new_field = {
        "name": f"field_{field_number}",
        "type": "Text",
        "options": {},
    }

    st.session_state.custom_fields.append(
        new_field
    )


def remove_custom_field(
    field_index: int,
) -> None:
    """
    Remove one field using its list index.
    """

    if len(st.session_state.custom_fields) <= 1:
        return

    st.session_state.custom_fields.pop(
        field_index
    )


def clean_field_name(
    field_name: str,
    field_index: int,
) -> str:
    """
    Prepare a field name for dictionary and column use.
    """

    cleaned_name = (
        field_name
        .strip()
        .lower()
        .replace(" ", "_")
    )

    if not cleaned_name:
        cleaned_name = (
            f"field_{field_index + 1}"
        )

    return cleaned_name



def find_duplicate_names(
    fields: list[dict],
) -> set[str]:
    """
    Return duplicated custom-field names.
    """

    field_names = [
        field["name"]
        for field in fields
    ]

    duplicate_names = {
        name
        for name in field_names
        if field_names.count(name) > 1
    }

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
            start_date = options.get(
                "start_date"
            )

            end_date = options.get(
                "end_date"
            )

            if start_date > end_date:
                return True

    return False



