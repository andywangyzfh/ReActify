import openai
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
import sys
from io import StringIO
from langchain.chat_models import ChatOpenAI
import time
import threading
from outputCapturer import OutputCapturer
from contextlib import redirect_stdout


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
        if (self.chatGPT):
            while True:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1024,
                    temperature=0.8)
                message = completion.choices[0].message.content
                return message
            #messages = []
            # while True:
            #     prompt = input('\nAsk a question: ')
            #     messages.append(
            #         {
            #             'role': 'user',
            #             'content': prompt
            #         })
            #     completion = openai.ChatCompletion.create(
            #         model="gpt-3.5-turbo",
            #         messages=messages)

            #     response = completion['choices'][0]['message']['content']
            #     print(response)
            #     messages.append(
            #         {
            #             'role': 'assistant',
            #             'content': response
            #         })
        else:
            chat = ChatOpenAI(temperature=self.temperature)
        # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
            llm = OpenAI(temperature=self.temperature)
            tools = load_tools(["serpapi", "llm-math"], llm=llm)
        # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
            agent = initialize_agent(
                tools, chat, agent="chat-zero-shot-react-description", verbose=True)
        # Now let's test it out!
            agent.run(prompt)


if __name__ == "__main__":
    myquery = Query()
    myquery.setModel(0, 0, 0)
    # myquery.getResponse(
    #     "In the city where the CEO of Tesla was born, what is the average price of houses?")

    # print_thread = threading.Thread(target=print_to_terminal)
    print_thread = threading.Thread(target=myquery.getResponse, args=(
        "In the city where the CEO of Tesla was born, what is the average price of houses?",))
    print_thread.start()

    while print_thread.is_alive():
        with StringIO() as buf, redirect_stdout(buf):
            print('redirected:')
            output = buf.getvalue()
            print(output)

    print_thread.join()
