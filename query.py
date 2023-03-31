import openai
import os
import IPython
from langchain.llms import OpenAI
from dotenv import load_dotenv


def setToken():
    load_dotenv()

    # API configuration
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # for LangChain
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
