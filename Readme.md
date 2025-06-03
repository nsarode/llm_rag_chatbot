![Python 3.13.12](https://img.shields.io/badge/python-3.13.12-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C.svg?style=for-the-badge&logo=LangChain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Neo4J](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white)
![fastapi](https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white)

# Overview

This repo contains code examples of using LangChain. The material follows and extends from [Build an LLM RAG Chatbot With LangChain](https://realpython.com/build-llm-rag-chatbot-with-langchain/)

The tutorial assumes you have *at minimum* a basic understanding of the following concepts and technologies,
- Large language models (LLMs) and prompt engineering
- Text embeddings and vector databases
- Graph databases and Neo4j
- The OpenAI developer ecosystem
- REST APIs and FastAPI
- Asynchronous programming
- Docker and Docker Compose

# Pre-requisites

- API key from [OpenAI](https://platform.openai.com/account/api-keys) or others of choice
- Neo4j account (free tier perfectly ok) - with active (running) instance 


# Business problem & requirements

You are an AI engineer working for a large hospital system in the US. Your stakeholders would like more visibility into the ever-changing data they collect. They want answers to ad-hoc questions about patients, visits, physicians, hospitals, and insurance payers without having to understand a query language like SQL, request a report from an analyst, or wait for someone to build a dashboard.

To accomplish this, your stakeholders want an internal chatbot tool, similar to ChatGPT, that can answer questions about your company’s data. After meeting to gather requirements, you’re provided with a list of the kinds of questions your chatbot should answer:

- What is the current wait time at XYZ hospital? (Objective answer)
- Which hospital currently has the shortest wait time? (Objective answer)
- At which hospitals are patients complaining about billing and insurance issues? (Subjective answer)
- Have any patients complained about the hospital being unclean? (Subjective answer)
- What have patients said about how doctors and nurses communicate with them? (Subjective answer)
- What are patients saying about the nursing staff at XYZ hospital? (Subjective answer)
- What was the total billing amount charged to Cigna payers in 2023? (Objective answer)
- How many patients has Dr. John Doe treated? (Objective answer)
- How many visits are open and what is their average duration in days? (Objective answer)
- Which physician has the lowest average visit duration in days? (Objective answer)
- How much was billed for patient 789’s stay? (Objective answer)
- Which hospital worked with the most Cigna patients in 2023? (Objective answer)
- What’s the average billing amount for emergency visits by hospital? (Objective answer)
- Which state had the largest percent increase inedicaid visits from 2022 to 2023? (Objective answer)

Depending on the query you give it, the agent needs to decide between the Cypher chain, reviews chain, and wait times functions

    - Subjective answer - the chatbot will have to read through reviews to get an answer for the question. Since the response could be subjective, there is no additional special ask of it

    - Objective answer - since the answer to the question is objective, but the questions could be phrased differenty by the user or may need some aggregation operation, the chatbot should *dynamically generate accurate queries* to retrieve an objective answer for the question being asked

# Data

HOSPITALS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/hospitals.csv
PAYERS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/payers.csv
PHYSICIANS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/physicians.csv
PATIENTS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/patients.csv
VISITS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/visits.csv
REVIEWS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/reviews.csv

The datasets have all the information needed to answer *most* of the questions, with the exception of 'wait times'. Since that information can't be stored in a static table, the bot will need to make an API call to answer the question. 

# Directory tree

# Setup

- Follow conda env setup instructions from [LangChain Basics](https://github.com/nsarode/langchain_basics/blob/main/Readme.md) for OpenAI (it will be commented out since in that repo I was trying out Google's Gemini - genai)
- Depending on the system, you may have to install `Docker`, `docker-compose`

```bash
conda activate llm
pip install chromadb
pip install langchain-community
pip instal neo4j

```
# Learnings

- Retrieval augmented generation (RAG) agent combines strengths of RAG with AI agents to allows agents to intelligently explore and utilize a knowledge base for more accurate and adaptable responses 
- Good prompt engineering skill is the most critical component to project like this. Being very explicit (background, expectations), assertive ("make sure", "never") and **extremely** specific with the details (desired outcome, format, style etc) takes practice and continuous revisions
- Leveraging llm agents to create complex Cypher queries is breathtaking to see, however for the purpose of few-shot prompting, example queries are needed within the prompt template for context. For that a solid understanding of the data model at hand is paramount
- LangChain agents can also run python code (not just chaining components and/or methods)
- Leveraging REPL tool like `ptpython` with its Emacs like interface makes testing half-baked code on the terminal a cinch
- Existing functionalities I didn't know before
    - `np.argmin` function returns index of minimum value within an input array
    - `from typing import Any` allows for flexibility in creating a thowaway variable that can be used by the llm agent
- Asynchronous serving capability of FastAPI helps dealing with the latency involved in waiting for agent to respond. Essentially, instead of waiting for OpenAI to respond to each of the agent’s requests, we can have our agent make multiple requests in a row and store the responses as they’re received. Deploying the agent asynchronously allows us to scale to a high-request volume without having to increase infrastructure demands


# Disclosure and precautions

The data is sourced & cleaned from Kaggle. It is synthetic and stupendously clean, to help focus on the aim on the project (create chatbot using langchain, OpenAI & Neo4j), without necessitating in-depth exploratory data analysis (EDA), feature engineering or cleaning of the data. In real life, you are NEVER going to come across a dataset as clean (error-free, standardized, etc.) as this one. See my code from [Physionet 2012](https://github.com/nsarode/physionet_2012) to see an example of data EDA (though to be honest, that dataset is also cleaner than what you will handle in real life. Real datasets are often proprietary and/or paid, so this is the best option I had to add to my public repo)