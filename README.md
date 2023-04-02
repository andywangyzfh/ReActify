# ReActify

This is a tool that includes the ReAct framework and a Data-Augmented Chat tool to create a user-friendly chat interface that can understand and respond to complex or nuanced user queries. 

[DEMO](https://youtu.be/WPlIWKec9O4)

## Installation

To install the tool, you'll need to clone this repository to your local machine and install the necessary dependencies. You'll also need to have Python 3 installed.

The required Python packages are:

- chromadb
- customtkinter
- dotenv
- Pillow
- langchains
- openai

## SerpAPI and OpenAI API Keys

Before using the tool, you'll need to obtain API keys for SerpAPI and OpenAI. You can register for these APIs on their respective websites and obtain your API keys.

Once you have your API keys, create a new file named `.env` in the root directory of the project and add the following lines:

```
SERP_API_KEY=your_serp_api_key
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_serp_api_key` and `your_openai_api_key` with your actual API keys.

Or, you can go to the settings to set these two parameters.

## Usage

To use the tool, run the following command from the command line:

``$ python app.py``

This will launch the tool's user interface in the customtkinterGUI. You can engage in a natural language chat with the AI language models using the provided interface.



