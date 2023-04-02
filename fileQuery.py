import openai
import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI

class fileQuery:
    
    def __init__(self):
        load_dotenv()

        # API configuration
        openai.api_key = os.getenv("OPENAI_API_KEY")

        # for LangChain
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
    
    def getFileResponse(self,fileAddress,query,temp,output):
        with open(fileAddress) as f:
            file=f.read()
        text_splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
        texts=text_splitter.split_text(file)
        embeddings=OpenAIEmbeddings()
        
        metadatas=[]
        for i in range(len(texts)):
            metadatas.append({"source":str(i)})
        docsearch=Chroma.from_texts(texts,embeddings,metadatas)
        docs=docsearch.similarity_search(query)
        chain=load_qa_with_sources_chain(OpenAI(temperature=temp),chain_type="stuff")
        result=chain({"input_documents": docs, "question": query}, return_only_outputs=output)
        if output==False:
            response="DOCUMENTS RELATED: "+str(result['input_documents'])+"\n\nQUESTION: "+str(result['question'])+"\nRESPONSE GENERATED:"+str(result['output_text'])
        else:
            response="RESPONSE GENERATED:"+str(result['output_text'])
        return response
        
if __name__ == "__main__":
    # for testing purposes
    myQuery=fileQuery()
    resp=myQuery.getFileResponse('./Resources/state_of_the_union.txt','What did the president say about LGBTQ+',0,False)
    print(resp)
        