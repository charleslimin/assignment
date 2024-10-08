#------------------------------ START OF SCRIPT ------------------------------

#```Python
# Set up and run this Streamlit App
import streamlit as st
# from helper_functions import llm # <--- Not needed anymore. The helper function is now directly called by `customer_query_handler` 🆕
from logics.customer_query_handler import process_user_message
#Importing the pandas Library 
import pandas as pd

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response, course_details = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)
    st.divider()
    df_course_details = pd.json_normalize(course_details)
    st.dataframe(df_course_details)
    print(f"User Input is {user_prompt}")
#```

#------------------------------ END OF SCRIPT ------------------------------