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

st.title("About This App")

st.write("This is a Streamlit App that demonstrates how to use OpenAI API to generate text completions")

with st.expander("How to use this app?"):
    st.write('''
        1. Enter your prompt in the text area.
        2. Click the Submit button.
        3. The app will generate a text completion based on your prompt.
    ''')

#```

#------------------------------ END OF SCRIPT ------------------------------