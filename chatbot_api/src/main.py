from fastapi import FastAPI
from agents.hospital_rag_agent import hospital_rag_agent_executor
from models.hospital_rag_query import HospitalQueryInput, HospitalQueryOutput
from utils.async_utils import async_retry

# instantiate FastAPI object
app = FastAPI(
    title="Hospital Chatbot",
    description="Endpoints for a hospital system graph RAG chatbot",
)


@async_retry(max_retries=10, delay=1) # to tackle neo4j intermittent connection issue
async def invoke_agent_with_retry(query: str): # run agent aynchronously
    """Retry the agent if a tool fails to run.

    This can help when there are intermittent connection issues
    to external APIs.
    """
    return await hospital_rag_agent_executor.ainvoke({"input": query})

@app.get("/")
async def get_status():
    return {"status": "running"}

@app.post("/hospital-rag-agent")
# extracts the text field from the request body, passes it to the agent, and returns the agent’s response to the user.
async def query_hospital_agent(query: HospitalQueryInput) -> HospitalQueryOutput:
    query_response = await invoke_agent_with_retry(query.text)
    query_response["intermediate_steps"] = [
        str(s) for s in query_response["intermediate_steps"]
    ]

    return query_response