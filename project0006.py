import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

# Authenticate with Google Sheets
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open_by_key('1WN7_EHVkIFOSb6FfIXrxtGjdsAo5hkQkbpgUAYrnW88').worksheet("Sheet1")

# Streamlit app
st.title('Create Form')

# Create form
with st.form('create_form'):
    name = st.text_input('Name')
    email = st.text_input('Email')
    submit_button = st.form_submit_button('Submit')

# Send data to Google Sheet when form is submitted
if submit_button:
    sheet.append_row([name, email])
    st.success('Data submitted successfully!')