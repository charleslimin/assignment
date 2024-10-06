#------------------------------ START OF SCRIPT ------------------------------

#```Python
# Set up and run this Streamlit App
import streamlit as st
# from helper_functions import llm # <--- Not needed anymore. The helper function is now directly called by `customer_query_handler` 🆕
from logics.resale_eligibility_query_handler import process_user_message
#Importing the pandas Library 
import pandas as pd

#from helper_functions.utility import check_password  

# Check if the password is correct.  
#if not check_password():  
#    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("General Information")

number_of_applicant = form.slider("How many applicants will be listed in the application?", 1, 4, 2)
number_of_occupier = form.slider("How many occupiers will be listed in the application?", 1, 4, 2)
form.subheader("General Information")
age_applicant_1 = form.slider("Applicant 1 age", 0, 130, 25)
sex_applicant_1 = form.radio(
    "Applicant 1 Sex",
    [":blue[Male]", ":red[Female]"],
    captions=["Male", "Female"],
)
citizenship_applicant_1 = form.selectbox(
    "Applicant 1 Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Other"),
)
income_applicant_1 = form.number_input("Applicant 1 Average Monthly Income")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)
#```

#------------------------------ END OF SCRIPT ------------------------------