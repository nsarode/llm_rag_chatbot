import dotenv
import os
from langchain.document_loaders.csv_loader import CSVLoader
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings




REVIEWS_CSV_PATH = "data/reviews.csv"
REVIEWS_CHROMA_PATH = "chroma_data"


dotenv.load_dotenv()

loader = CSVLoader(file_path=REVIEWS_CSV_PATH, source_column="review")
reviews = loader.load()

# api_key = os.getenv("GEMINI_API_KEY")
# my_model="gemini-2.0-flash"

# create chroma vector store from document

reviews_vector_db = Chroma.from_documents(reviews, embedding =OpenAIEmbeddings(), persist_directory=REVIEWS_CHROMA_PATH)
