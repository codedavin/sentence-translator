import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

#Loading the variables from the environment

load_dotenv()

#Now loading the key from the environment
Google_API_Key=os.getenv("Google_API_Key")
print(Google_API_Key)

#Now I have to declare the LLM or the model
llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

#Now I have to declare the Prompt for the model


prompt=PromptTemplate.from_template("In an easy way, translate the following sentence '{sentence}' into {language}.")


#Now I have to build the chain that can connect the LLM model to the prompt and the output parser
chain=LLMChain(
    llm=llm,
    prompt=prompt,
    output_parser=StrOutputParser()

)

inputs = {"sentence": "Generative AI will change the future in upcoming days", "language": "Spanish"}

# Run the chain
response = chain.run(inputs)
print(response)
