#!/bin/bash

# Run any setup steps or pre-processing tasks here
echo "Starting hospital chatbot frontend..."

# Run the ETL script
streamlit run main.py #--server.port=8501 --server.address=0.0.0.0