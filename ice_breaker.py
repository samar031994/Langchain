import json
import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_party.linked_in import scrape_linkedin_profile
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

if __name__ == "__main__":
    load_dotenv()
    summary_template = """
        given the Linkedin information {information} about a person, I want you to create:
        1. A short summary
        2. two interesting facts about them
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(
        openai_api_key=os.environ.get("OPENAI_API_KEY"),
        temperature=0,
        model_name="gpt-3.5-turbo",
    )
    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(
        url="https://www.linkedin.com/in/eden-marco/"
    )
    res = chain.invoke(input={"information": linkedin_data})
    pp.pprint(res.content)
