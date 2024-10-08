#------------------------------ START OF SCRIPT ------------------------------

#```Python
# Set up and run this Streamlit App
import streamlit as st
# from helper_functions import llm # <--- Not needed anymore. The helper function is now directly called by `customer_query_handler` 🆕
from logics.resale_eligibility_check_handler import process_user_message
#Importing the pandas Library 
import pandas as pd

#from helper_functions.utility import check_password  

# Check if the password is correct.  
#if not check_password():  
#    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Resale Flat Eligibility Checker"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Resale Flat Eligibility Checker")

if "app2flg" not in st.session_state:
    st.session_state.app2flg = False
if "app3flg" not in st.session_state:
    st.session_state.app3flg = True
if "app4flg" not in st.session_state:
    st.session_state.app4flg = True
if "occ1flg" not in st.session_state:
    st.session_state.occ1flg = True
if "occ2flg" not in st.session_state:
    st.session_state.occ2flg = True
if "occ3flg" not in st.session_state:
    st.session_state.occ3flg = True
if "occ4flg" not in st.session_state:
    st.session_state.occ4flg = True

def update_applicant_inputs():
    if st.session_state.number_of_applicant_slider == 1:
        st.session_state.app2flg = True
        st.session_state.app3flg = True
        st.session_state.app4flg = True
    elif st.session_state.number_of_applicant_slider == 2:
        st.session_state.app2flg = False
        st.session_state.app3flg = True
        st.session_state.app4flg = True
    elif st.session_state.number_of_applicant_slider == 3:
        st.session_state.app2flg = False
        st.session_state.app3flg = False
        st.session_state.app4flg = True
    else:
        st.session_state.app2flg = False
        st.session_state.app3flg = False
        st.session_state.app4flg = False

def update_occupier_inputs():
    if st.session_state.number_of_occupier_slider == 0:
        st.session_state.occ1flg = True
        st.session_state.occ2flg = True
        st.session_state.occ3flg = True
        st.session_state.occ4flg = True
    elif st.session_state.number_of_occupier_slider == 1:
        st.session_state.occ1flg = False
        st.session_state.occ2flg = True
        st.session_state.occ3flg = True
        st.session_state.occ4flg = True
    elif st.session_state.number_of_occupier_slider == 2:
        st.session_state.occ1flg = False
        st.session_state.occ2flg = False
        st.session_state.occ3flg = True
        st.session_state.occ4flg = True
    elif st.session_state.number_of_occupier_slider == 3:
        st.session_state.occ1flg = False
        st.session_state.occ2flg = False
        st.session_state.occ3flg = False
        st.session_state.occ4flg = True
    else:
        st.session_state.occ1flg = False
        st.session_state.occ2flg = False
        st.session_state.occ3flg = False
        st.session_state.occ4flg = False

st.subheader("General Information")
number_of_applicant = st.slider("How many applicants will be listed in the application?", 1, 4, 2, key="number_of_applicant_slider", on_change=update_applicant_inputs)
number_of_occupier = st.slider("How many occupiers will be listed in the application?", 0, 4, 0, key="number_of_occupier_slider", on_change=update_occupier_inputs)

st.subheader("Applicant 1")
age_applicant_1 = st.slider("Age", 0, 130, 25, key="age_applicant_1")
citizenship_applicant_1 = st.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Foreigner"),
    key="citizenship_applicant_1"
)
income_applicant_1 = st.number_input("Average Monthly Income", key="income_applicant_1")

st.subheader("Applicant 2")
age_applicant_2 = st.slider("Age", 0, 130, 25, key="age_applicant_2", disabled=st.session_state.app2flg)
citizenship_applicant_2 = st.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Foreigner"),
    key="citizenship_applicant_2",
    disabled=st.session_state.app2flg
)
income_applicant_2 = st.number_input("Average Monthly Income", key="income_applicant_2", disabled=st.session_state.app2flg)
relationship_applicant_2 = st.selectbox(
    "Relationship with Application 1",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Unrelated"),
    key="relationship_applicant_2",
    disabled=st.session_state.app2flg
)

st.subheader("Applicant 3")
age_applicant_3 = st.slider("Age", 0, 130, 25, key="age_applicant_3", disabled = st.session_state.app3flg)
citizenship_applicant_3 = st.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Foreigner"),
    key="citizenship_applicant_3",
    disabled = st.session_state.app3flg
)
income_applicant_3 = st.number_input("Average Monthly Income", key="income_applicant_3", disabled = st.session_state.app3flg)
relationship_applicant_3 = st.selectbox(
    "Relationship with Application 1",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Unrelated"),
    key="relationship_applicant_3",
    disabled = st.session_state.app3flg
)

st.subheader("Applicant 4")
age_applicant_4 = st.slider("Age", 0, 130, 25, key="age_applicant_4", disabled = st.session_state.app4flg)
citizenship_applicant_4 = st.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Foreigner"),
    key="citizenship_applicant_4",
    disabled = st.session_state.app4flg
)
income_applicant_4 = st.number_input("Average Monthly Income", key="income_applicant_4", disabled = st.session_state.app4flg)
relationship_applicant_4 = st.selectbox(
    "Relationship with Application 1",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Unrelated"),
    key="relationship_applicant_4",
    disabled = st.session_state.app4flg
)

st.subheader("Occupier 1")
citizenship_occupier_1 = st.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Foreigner"),
    key="citizenship_occupier_1",
    disabled = st.session_state.occ1flg 
)
relationship_occupier_1 = st.selectbox(
    "Relationship with Application 1",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Unrelated"),
    key="relationship_occupier_1",
    disabled = st.session_state.occ1flg
)

st.subheader("Occupier 2")
citizenship_occupier_2 = st.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Foreigner"),
    key="citizenship_occupier_2",
    disabled = st.session_state.occ2flg 
)
relationship_occupier_2 = st.selectbox(
    "Relationship with Application 2",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Unrelated"),
    key="relationship_occupier_2",
    disabled = st.session_state.occ2flg
)

st.subheader("Occupier 3")
citizenship_occupier_3 = st.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Foreigner"),
    key="citizenship_occupier_3",
    disabled = st.session_state.occ3flg 
)
relationship_occupier_3 = st.selectbox(
    "Relationship with Application 3",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Unrelated"),
    key="relationship_occupier_3",
    disabled = st.session_state.occ3flg
)

st.subheader("Occupier 4")
citizenship_occupier_4 = st.selectbox(
    "Citizenship",
    ("Singpore Citizen", "Singapore Permanent Resident", "Foreigner"),
    key="citizenship_occupier_4",
    disabled = st.session_state.occ4flg 
)
relationship_occupier_4 = st.selectbox(
    "Relationship with Application 4",
    ("Spouse", "Parent", "Child", "Grandparent", "Grandchild", "Sibling", "Unrelated"),
    key="relationship_occupier_4",
    disabled = st.session_state.occ4flg
)

user_prompt = ""

form = st.form(key="form")

if form.form_submit_button("Submit"):
    #st.toast(f"User Input Submitted - {user_prompt}")
    #response = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    #st.write(response)
    question = f"""Applicant 1: {str(age_applicant_1)}  years old {citizenship_applicant_1} with average monthly income of {str(income_applicant_1)} """
    if number_of_applicant > 1:
        question += f"""
        \n Applicant 2: {str(age_applicant_2)}  years old {citizenship_applicant_2} with average monthly income of {str(income_applicant_2)} the relationship between Applicant 1 and Applicant 2 are {relationship_applicant_2}
        """
    if number_of_applicant > 2:
        question += f"""
        \n Applicant 3: {str(age_applicant_3)}  years old {citizenship_applicant_3} with average monthly income of {str(income_applicant_3)} the relationship between Applicant 1 and Applicant 3 are {relationship_applicant_3}
        """
    if number_of_applicant > 3:
        question += f"""
        \n Applicant 4: {str(age_applicant_4)}  years old {citizenship_applicant_4} with average monthly income of {str(income_applicant_4)} the relationship between Applicant 1 and Applicant 4 are {relationship_applicant_4}
        """
    if number_of_occupier > 0:
        question += f"""
        \n Occupier 1: {citizenship_occupier_1} with relationship between Applicant 1 and Occupier 1 are {relationship_occupier_1}
        """
    if number_of_occupier > 1:
        question += f"""
        \n Occupier 2: {citizenship_occupier_2} with relationship between Applicant 1 and Occupier 2 are {relationship_occupier_2}
        """
    if number_of_occupier > 2:
        question += f"""
        \n Occupier 3: {citizenship_occupier_3} with relationship between Applicant 1 and Occupier 3 are {relationship_occupier_3}
        """
    if number_of_occupier > 3:
        question += f"""
        \n Occupier 4: {citizenship_occupier_4} with relationship between Applicant 1 and Occupier 4 are {relationship_occupier_4}
        """
    st.write("Question:")
    st.write(question)
    response = process_user_message(question) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)
#```

#------------------------------ END OF SCRIPT ------------------------------