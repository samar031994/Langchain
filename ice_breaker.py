import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    load_dotenv()
    information = """Biswa Kalyan Rath is an Indian stand-up comedian, writer and YouTuber. He came into prominence through the YouTube comedy series, Pretentious Movie Reviews[3] with fellow comedian Kanan Gill.
        """
    summary_template = f"""
        given the information {information} about a person I want you to create:
        1. A short summary
        2. four interesting facts about them
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"),temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})
    print(res.content)
