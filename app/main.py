import asyncio
import dspy

from app.core.config import settings
from app.generator.chat import ChatModule

async def main():
    lm = dspy.LM(model="gemini/gemini-2.0-flash", api_key=settings.gemini_api_key)
    dspy.configure(lm=lm)

    chat = ChatModule()

    while True:
        question = input("Ask a question (q to quit): ")
        if question.lower() == "q":
            print("Goodbye!")
            break
        
        print(f"User: {question}")

        result = chat(question=question)
        print(f"Assistant: {result.answer}")

if __name__ == "__main__":
    asyncio.run(main())