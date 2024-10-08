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

with st.expander("Objective"):
    st.write('''
        1. Allow user to ask questions about the process of buying HDB Resale Flat
        2. Allow user to perform HDB Reslae Flat Eligibility Check based on the profile entered
    ''')

with st.expander("Scope"):
    st.write('''
         To create an App powered by OpenAI and CrewAI to answer customer queries on HDB Resale Flat buying procedure and perform eligibility check. 
    ''')

with st.expander("Data Sources"):
    st.write('''
         Text Files axtracted from HDB Official Website:
            1. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats
            2. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/overview
            3. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract
            4. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations
            5. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/managing-the-flat-purchase
            6. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/eip-spr-quota
            7. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/conversion-scheme-application-procedure
            8. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/mode-of-financing
            9. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/option-to-purchase
            10. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/request-for-value
            11. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application
            12. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/application
            13. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/acceptance-and-approval
            14. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/request-for-enhanced-contra-facility
            15. https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-completion
            16. https://www.hdb.gov.sg/business/estate-agents-and-salespersons/buying-a-resale-flat/eligibility

    ''')

with st.expander("Features"):
    st.write('''
         1. Ask question about procedure to buy HDB resale flat
         2. Resale Flat Eligibility Check 
    ''')

#```

#------------------------------ END OF SCRIPT ------------------------------