# Thread of Thoughts Chain

This repository implements the "Thread of Thoughts" (ThoT) strategy, inspired by human cognitive processes. ThoT systematically segments and analyzes extended contexts while adeptly selecting pertinent information, improving reasoning performance in chaotic contexts.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Thread of Thoughts technique addresses challenges faced by Large Language Models (LLMs) when dealing with chaotic contexts, such as distractors or long irrelevant contexts. ThoT enhances the extraction of pertinent content for responding to queries by segmenting and analyzing extended contexts.

## Installation

To install the necessary dependencies, run:

pipenv install 

## Usage

    The main class implementing the Thread of Thoughts strategy is Thread_of_Thoughts_Chain. It requires an LLM chain and a context document as inputs. Here's an example of how to use the class:

    python

    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.prompts import PromptTemplate
    from langchain.chains.llm import LLMChain
    from langchain_core.documents.base import Document
    from your_module import Thread_of_Thoughts_Chain  # Replace with the correct import path

    # Initialize your LLM chain and context document
    llm_chain = LLMChain(...)  # Initialize your LLM chain here
    context = Document(...)  # Load your context document here

    # Create the Thread of Thoughts chain
    thot_chain = Thread_of_Thoughts_Chain(llm=llm_chain, context=context)

    # Generate the reasoning chain
    reasoning_chain = thot_chain.create()

    # Use the reasoning chain as needed
    result = reasoning_chain.run(query="Your query here")
    print(result)
## Example 
    You can refer to the main.py file to see a working example
## Dependencies

    langchain
    Other dependencies can be found in requirements.txt

## Contributing

We welcome contributions to enhance the functionality and performance of this implementation. Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License.