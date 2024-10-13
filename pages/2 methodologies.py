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
    st.image("./data/use_case_1_flowchart.JPG", caption="Buying HDB Resale Flat")

with st.expander("Resale Flat Eligibility Checker"):
    st.image("./data/use_case_2_flowchart.JPG", caption="Resale Flat Eligibility Checker")

#```

#------------------------------ END OF SCRIPT ------------------------------