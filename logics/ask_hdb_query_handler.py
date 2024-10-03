#------------------------------ START OF SCRIPT ------------------------------

#```Python
# Common imports
import os
from dotenv import load_dotenv
import json
import lolviz

# Import the key CrewAI classes
from crewai import Agent, Task, Crew

# import other necessary libraries you need
from crewai_tools import SeleniumScrapingTool, FileReadTool

seleniumscrap_tool = SeleniumScrapingTool()
file_read_tool = FileReadTool( './data/hdb_resale_info.txt' )

agent_profiler = Agent(
    role="HDB Resale Flat Buyer Profiler",
    goal=("Perform comprehensive analysis on potential HDB Resale Flat buyer"),
    backstory=("As HDB Resale Flat buyer profiler, you are an expert in analyzing potential HDB Resale Flat buyer to craft comprehensive personal profiles to better advise them on questions that they have."),
    allow_delegation=False, 
    verbose=True, 
)

agent_responder = Agent(
    role="HDB Customer Service Officer",
    goal=("Answer question from potential HDB Resale Flat buyer"),
    backstory=("As an experienced HDB Customer Service Officer, you are an expert in answering questions retalted to HDB resale flat, "
               "taking into account the profile of potential buyer"),
    tools=[file_read_tool],
    allow_delegation=False, 
	verbose=True,
)

task_profiler = Task(
    description="Compile a detailed personal profile described by the potential HDB Resale Flat buyer here (`{user_input}`)",

    expected_output=" A structured profile described by potential HDB Resale Flat buyer.",

    agent=agent_profiler,
)

task_responder = Task(
    description="""
    1. Using structured profile obtained from previous task, answer the following user question (`{user_input}`).
    2. Do not make up any information.""",

    expected_output="""
    A tailored answer based on buyer profile.""",

    agent=agent_responder,
)

crew = Crew(
    agents=[agent_profiler, agent_responder ],
    tasks=[task_profiler, task_responder],
    verbose=True
)

def process_user_message(user_input):

    hdb_resale_buyer_inputs = {'user_input': user_input}

    result = crew.kickoff(inputs=hdb_resale_buyer_inputs)

    return (result)
#```

# I am planning to buy HDB resale flat with my spouse. I am 32 years old Singapore Citizen with monthly average income of 2,000. My spouse is 30 years old Singapore Permanent Resident with monthly average income of 4,000.

# Are we eligible to buy HDB resale flat and may I know what is the procedure or how should we proceed?

#------------------------------ END OF SCRIPT ------------------------------