from typing import Any
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from utils import get_retriever, split_data, format_docs
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_core.documents.base import Document

class Thread_of_Thoughts_Chain: 
    def __init__(self,llm: LLMChain, context: Document ) -> None:
        self.llm = llm
        self.initiating_reasoning_template = """{context} Q:{query} 
        Walk me through this context in
        manageable parts step by step, summarizing and
        analyzing as we go 
        A:"""
        self.sumarize_thread_of_thoughts_template = "A: {answer} Therefore, the final answer: "
        self.context = context
    def _get_reasoning_chain(self):
        splits = split_data(self.context)
        retriever = get_retriever(splits)
        initiating_reasoning_prompt = PromptTemplate.from_template(
            self.initiating_reasoning_template
        )
        initiating_reasoning_sub_chain = {
            "context": retriever | format_docs,
            "query": RunnablePassthrough(),
        } | initiating_reasoning_prompt|self.llm|StrOutputParser()
        return initiating_reasoning_sub_chain
    def _sumarize_thread_of_thoughts(self):
        sumarize_thread_of_thoughts_prompt = PromptTemplate.from_template(
            self.sumarize_thread_of_thoughts_template
        )
        sumarize_thread_of_thoughts_sub_chain =  sumarize_thread_of_thoughts_prompt|self.llm|StrOutputParser()
        return sumarize_thread_of_thoughts_sub_chain
    def create(self, *args: Any, **kwds: Any) -> Any:
        return self._get_reasoning_chain()|self._sumarize_thread_of_thoughts()
        