import openai
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
import sys
from io import StringIO
from langchain.chat_models import ChatOpenAI

class Query:
    showProcess = 0
    temperature = 0
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

    def setModel(self,showProcess, temperature):
        self.showProcess = showProcess
        self.temperature = temperature

    def getResponse(self,prompt):
        chat = ChatOpenAI(temperature=self.temperature)
    # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
        llm = OpenAI(temperature=self.temperature)
        tools = load_tools(["serpapi", "llm-math"], llm=llm)
    # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
        agent = initialize_agent(tools, chat, agent="chat-zero-shot-react-description", verbose=True)
    # Now let's test it out!
        output = StringIO()
        sys.stdout = output
        final_result = agent.run(prompt)
        sys.stdout = sys.__stdout__
    # Retrieve the output from the StringIO object as a string
        react_process = output.getvalue()
        if(self.showProcess):
            return react_process
        else:
            return final_result
if __name__ == "__main__":
    #for testing purposes
    myquery = Query()
    myquery.setModel(1,0)
    print(myquery.getResponse("In the city where the CEO of Tesla was born, what is the average price of houses?"))