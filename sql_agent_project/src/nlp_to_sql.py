from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
import os
from dotenv import load_dotenv

load_dotenv()

class NLPtoSQL:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY não definido.")

        self.client = OpenAI(api_key=api_key, model="gpt-4", temperature=0.3)

        template = "Converta a seguinte pergunta para uma query SQL: {question}"
        prompt = PromptTemplate.from_template(template)

        self.chain = prompt | RunnableLambda(lambda x: self.client.invoke(x["question"]))

    def convert(self, question: str) -> str:
        try:
            response = self.chain.invoke({"question": question})
            if not response or "SELECT" not in response.upper():
                raise ValueError(f"SQL inválido: {response}")
            return response.strip()
        except Exception as e:
            return f"Erro ao gerar SQL: {str(e)}"
