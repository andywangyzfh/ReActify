import openai
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
import sys
from io import StringIO
from langchain.chat_models import ChatOpenAI

# for implemetngin chatgpt with memory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferMemory


class Query:
    showProcess = 0
    temperature = 0
    chatGPT = 0

    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

    def setModel(self, showProcess, temperature, chatGPT):
        self.showProcess = showProcess
        self.temperature = temperature
        self.chatGPT = chatGPT

    def getResponse(self, prompt):
        if (self.chatGPT):  # 尝试implement一个带历史记录的ChatGPT 但接口不一样了 不能return一个string，而是得让他一直跑着跟用户对话，估计得写到前端去
            # https://ahmadrosid.com/blog/langchain-openai-tutorial
            llm = OpenAI(temperature=.7)
            # 可以加个功能：让用户自定义prompt format，
            template = """Consider the chat history given below. You are an AI. Answer to Human.
                {chat_history}
                Human: {question}
                AI:
            """
            prompt_template = PromptTemplate(
                input_variables=["chat_history", "question"], template=template)
            memory = ConversationBufferMemory(memory_key="chat_history")
            llm_chain = LLMChain(
                llm=OpenAI(),
                prompt=prompt_template,
                verbose=True,
                memory=memory,
            )
            answer = llm_chain.predict(question=prompt)
            return answer
        else:
            chat = ChatOpenAI(temperature=self.temperature)
        # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
            llm = OpenAI(temperature=self.temperature)
            tools = load_tools(["serpapi", "llm-math"], llm=llm)
        # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
            agent = initialize_agent(
                tools, chat, agent="chat-zero-shot-react-description", verbose=True)
        # Now let's test it out!
            output = StringIO()
            sys.stdout = output
            final_result = agent.run(prompt)
            sys.stdout = sys.__stdout__
        # Retrieve the output from the StringIO object as a string
            react_process = output.getvalue()
            if (self.showProcess):
                return react_process
            else:
                return final_result


if __name__ == "__main__":
    # for testing purposes
    myquery = Query()
    myquery.setModel(1, 1, 1)
    print(myquery.getResponse(
        "I am traveling from Shanghai to Williamsburg in May, how?"))
