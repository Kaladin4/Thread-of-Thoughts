from langchain import hub
from langchain_anthropic import ChatAnthropic
import os 
from utils import read_files
from thread_of_thought import Thread_of_Thoughts_Chain

def main():
    context_files = ["thread_of_thought.pdf"]
    context = read_files(context_files)
    llm = ChatAnthropic(model='claude-3-opus-20240229')
    thread_of_thoughts_chain = Thread_of_Thoughts_Chain(llm=llm,context=[context]).create()

    print(thread_of_thoughts_chain.invoke("What is thread of thought"))
if __name__ == "__main__":
    main()
    