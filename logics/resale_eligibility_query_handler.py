#------------------------------ START OF SCRIPT ------------------------------

#```Python
import json
from helper_functions import llm

# Load the Text file
filepath = './data/hdb_resale_eligibility.txt'
with open(filepath, 'r') as file:
    information_text = file.read()

def check_question_relevancy(user_message):
    delimiter = "####"

    system_message = f"""
    You will need to check whether user is asking about HDB resale flat eligibility.
    If yes, return TRUE, otherwise return FALSE.
    You must response with only TRUE or FALSE.
    """
    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    relevancy_check_response = llm.get_completion_by_messages(messages)
    
    return relevancy_check_response

def generate_question_response(user_message):
    delimiter = "####"

    system_message = f"""
    You will need to answer user queries based on the following information provided:
    {information_text}

    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} Decide if user has provided sufficient details in their query.
    
    Step 2:{delimiter} If the user has provided sufficient detail, generate the answer, otherwise \
    list down additional information that the user has to provide.\
    Your response should be as detail as possible. \

    Step 3:{delimiter}: Answer the customer in a friendly tone. \
    Make sure the statements are factually accurate.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer


def process_user_message(user_input):
    delimiter = "```"

    relevancy_check = check_question_relevancy(user_input)

    if relevancy_check == "TRUE":
        reply = generate_question_response(user_input)
    else:
        reply = "This module only support questions regarding HDB Resale Flat eligibility."
    
    return (reply)
#```

# I am planning to buy HDB resale flat with my spouse. I am 32 years old Singapore Citizen with monthly average income of 2,000. My spouse is 30 years old Singapore Permanent Resident with monthly average income of 4,000.

# Are we eligible to buy HDB resale flat and may I know what is the procedure or how should we proceed?

#------------------------------ END OF SCRIPT ------------------------------