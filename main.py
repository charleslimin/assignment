#------------------------------ START OF SCRIPT ------------------------------

#```Python
# Set up and run this Streamlit App
import streamlit as st
# from helper_functions import llm # <--- Not needed anymore. The helper function is now directly called by `customer_query_handler` 🆕
from logics.ask_hdb_query_handler import process_user_message
#Importing the pandas Library 
import pandas as pd

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Buying HDB Resale Flat"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Buying HDB Resale Flat")

form = st.form(key="form")
form.subheader("Ask question about procedure to buy HDB resale flat")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)
#```

#------------------------------ END OF SCRIPT ------------------------------