#------------------------------ START OF SCRIPT ------------------------------

#```Python
# Set up and run this Streamlit App
import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About Us"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology Flow Chart")

with st.expander("Ask question about procedure to buy HDB resale flat"):

    st.write('''
        The application accepts free text user input, which is checked for query injection attack using LLM Based validation. Error message will be displayed when a suspicious entry is detected, otherwise the input will be passed to CrewAI Agent for user profiling. Another agent will take over to generate answer to user query.
    ''')

    st.image("./data/use_case_1_flowchart.JPG", caption="Buying HDB Resale Flat")

with st.expander("Resale Flat Eligibility Checker"):

    st.write('''
        The application accepts input in a form based (non-free-text) input. Input validation is performed to filter out logically incorrect input. Error message will be displayed when incorrect input is detected, otherwise the input will be passed to GenAI to generate the answer.
    ''')

    st.image("./data/use_case_2_flowchart.JPG", caption="Resale Flat Eligibility Checker")

#```

#------------------------------ END OF SCRIPT ------------------------------