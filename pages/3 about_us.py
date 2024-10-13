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

st.title("HDB Resale Flat Advisor")

with st.expander("Background"):
    st.write('''
        The process of purchasing an HDB resale flat in Singapore can be challenging for buyers that purchase the HDB resale flat for the first time. This is true, especially for those who do not engage a property agent to help them throughout the buying process. The process involves numerous eligibility criteria, regulations, and procedural steps that vary depending on the buyer's circumstances (e.g., citizenship, income level, and family structure). Potential buyers often face confusion when trying to understand their eligibility and the necessary steps required, leading to delays and misunderstandings that can complicate the buying process.
    ''')

with st.expander("Problem Statement"):
    st.write('''
        There is a need for an intelligent, centralized, and accessible platform that can provide accurate, real-time information and personalized assistance to users regarding HDB resale flat purchase procedures and eligibility criteria. An AI-driven solution, capable of understanding and responding to user queries in natural language, would significantly reduce confusion, enhance the user experience, and improve the efficiency of the HDB resale flat buying process.
    ''')

with st.expander("Proposed Solution"):
    st.write('''
         The HDB Resale Flat Advisor will serve as an AI-powered platform that addresses these challenges by providing users with a seamless experience. It will offer tailored guidance on eligibility criteria and step-by-step instructions for the buying process. This solution aims to streamline the process for potential buyers, ensuring they have access to reliable and personalized support, reducing the time and effort required to obtain necessary information.
    ''')

with st.expander("Project Scope"):
    st.write('''
        The scope of this project involves creation of CrewAI powered query form that allows user to type in their queries in natural language and get answer almost immediately based on information extracted from HDB Official Website. User input to this free-text form is protected from malicious prompt injection attack with LLM based protection.

        Another scope of this project involves creation of Resale Flat Eligibility Checker powered by GenAI and prompt engineering based information extracted from HDB Official Website. Instead of free-text-input, user will be asked to key in required information into predefined form that comes with input validation.
    ''')

with st.expander("Project Objective"):
    st.write('''
        To provide one stop platform that can quickly answer user queries about the procedure of buying HDB resale flat.

        To provide one stop platform for user to check their eligibility to purchase HDB resale flat.
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

        A free-text query form that allow users to ask anything about the procedure to buy HDB Resale Flat
        Protected by LLM Based query injection protection
        Powered by CrewAI
        Based on information extracted from official HDB Website

        2. Resale Flat Eligibility Check

        A form based Eligibility Checker with no free-text entry
        Protected by input validation
        Powered by GenAI and Prompt Engineering
        Based on information extracted from official HDB Website 
    ''')

#```

#------------------------------ END OF SCRIPT ------------------------------