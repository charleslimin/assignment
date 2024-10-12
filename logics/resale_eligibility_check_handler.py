#------------------------------ START OF SCRIPT ------------------------------

#```Python
import json
from helper_functions import llm

# Load the Text file
filepath = './data/hdb_resale_eligibility.txt'
with open(filepath, 'r') as file:
    information_text = file.read()

def generate_question_response(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with HDB Resale Flat Applicants and Occupiers details.
    The Applicants and Occupiers details will be enclosed in the pair of {delimiter}.
    Your task is to check the Applicants eligibility to purchase HDB Resale Flat.
    Your answer MUST be beased ONLY on the information contained in the following text:
    <HDB Resale Flat Eligibility>
    {information_text}
    </HDB Resale Flat Eligibility>

    Please note the following:
    - 0 to 20 years old are below 21 years old
    - 21 to 130 years old are above 21 years old
    
    Follow these steps to generate your answer.

    Step 1:{delimiter} Read the HDB Resale Flat Eligibility information 

    Step 2:{delimiter} Decide whether you have the answer.
    
    Step 3:{delimiter} If you have the answer, generate your response. Otherwise, direct user to contact HDB Customer Service Hotline.

    Step 4:{delimiter}: Generate your response in a friendly tone. Make sure the statements are factually accurate.

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
    reply = generate_question_response(user_input)
    return (reply)
#```

#------------------------------ END OF SCRIPT ------------------------------