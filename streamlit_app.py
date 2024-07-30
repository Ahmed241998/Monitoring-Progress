import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from datetime import datetime, timezone, timedelta


# Display Title and Description
st.title("L'Oréal Action Plan")

# Establishing a Google Sheet Connection
conn = st.experimental_connection('gsheets',type=GSheetsConnection)

# Ftech Exisiting Vendors data
existing_data = conn.read(worksheet= 'Action Details',usecols = list(range(9)) , ttl = 5)
existing_data = existing_data.dropna(how="all")
st.dataframe(existing_data)


