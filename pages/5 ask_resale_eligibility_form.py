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

form.subheader("Applicant 1")
age_applicant_1 = form.slider("Age", 0, 130, 25, key="age_applicant_1")
citizenship_applicant_1 = form.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Other"),
    key="citizenship_applicant_1"
)
income_applicant_1 = form.number_input("Average Monthly Income", key="income_applicant_1")

form.subheader("Applicant 2")
age_applicant_2 = form.slider("Age", 0, 130, 25, key="age_applicant_2")
citizenship_applicant_2 = form.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Other"),
    key="citizenship_applicant_2"
)
income_applicant_2 = form.number_input("Average Monthly Income", key="income_applicant_2")
relationship_applicant_2 = form.selectbox(
    "Relationship with Application 1",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Other"),
    key="relationship_applicant_2"
)

form.subheader("Applicant 3")
age_applicant_3 = form.slider("Age", 0, 130, 25, key="age_applicant_3")
citizenship_applicant_3 = form.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Other"),
    key="citizenship_applicant_3"
)
income_applicant_3 = form.number_input("Average Monthly Income", key="income_applicant_3")
relationship_applicant_3 = form.selectbox(
    "Relationship with Application 1",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Other"),
    key="relationship_applicant_3"
)

form.subheader("Applicant 4")
age_applicant_4 = form.slider("Age", 0, 130, 25, key="age_applicant_4")
citizenship_applicant_4 = form.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Other"),
    key="citizenship_applicant_4"
)
income_applicant_4 = form.number_input("Average Monthly Income", key="income_applicant_4")
relationship_applicant_4 = form.selectbox(
    "Relationship with Application 1",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Other"),
    key="relationship_applicant_4"
)

form.subheader("Occupier 1")
citizenship_occupier_1 = form.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Other"),
    key="citizenship_occupier_1"
)
relationship_occupier_1 = form.selectbox(
    "Relationship with Application 1",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Other"),
    key="relationship_occupier_1"
)

user_prompt = ""

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)
#```

#------------------------------ END OF SCRIPT ------------------------------