import json
from io import BytesIO

import pandas as pd
import streamlit as st

from generate import (
    generate_custom_data,
    generate_data,
    set_seed,
)


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
        page_title="Fake Data Generator",
            page_icon="# # #                 
)