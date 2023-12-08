# NLP Studio

NLP Studio is a CLI (command line interface) written in Python to showcase what can be done with NLP and Large Language Models.
It will use different known libraries from the Python NLP and LLM ecosystem.

The CLI will be built using [Typer](https://typer.tiangolo.com/).

Ideas so far that can be integrated:
- Generate Images using stabilityai/sxdl-turbo pretrained model
- Using LangChain to integrate with OpenAI GPT LLM
- Integrate with local Mistral LLM running on Ollama
- Showcase on how to use vector databases using something like GenSim or word2vec
- Example of simple Bag Of Words sentence classification
- Extractive Summarization using Spacy
- Scraping public information for the web and Reading PDF files to feed it to an LLM for
    - Abstractive Summarization
    - Ask questions about the content


I will explain how to use prompting techniques using zero-Shot prompting, Few-shot prompting and Chain-of-thought prompting and the difference in outcome between foundation models and a "smaller" locally running LLM 

# Use Cases

## Generating Images
[SDXL Turbo information on HuggingFace](https://huggingface.co/stabilityai/sdxl-turbo)

Because I am running this on a Macbook with an Apple M1 chip, I've had to configure PyTorch for using the [MPS backend](https://pytorch.org/docs/stable/notes/mps.html) instead of [CUDA](https://en.wikipedia.org/wiki/CUDA). Cuda can only be used if your machine is running a NVIDIA GPU.  

Use the following command to generate images:

```
python3 main.py generate-image [PROMPT]
```

Examples:
```
python3 main.py generate-image "A racoon taking a bath in the desert surrounded by camels"
```

```
python3 main.py generate-image "A lizzard enjoying a soft-drink on the table of sunny terrace at the coastline"
```

## Chatbot


The command:
```
python3 main.py chatbot
```

## Prerequisites

### Ollama & Mistral
This command interfaces with the Mistral LLM model that locally runs on my machine. I use [Ollama](https://ollama.ai/) to run large language models locally.
For the installation of Ollama and how to run models locally using Ollama can be found [here](https://github.com/jmorganca/ollama)


## Implementation
To simplify the implementation of a chatbot, I make use of the [LangChain](https://python.langchain.com/docs/get_started/introduction) library
Checkout [this documentation](https://python.langchain.com/docs/use_cases/chatbots) on how to implement a simple chatbot.

If you want to use emojis, check out [this link](https://www.webfx.com/tools/emoji-cheat-sheet/).

## Adaptation

- This example can easily be adapted, to run Llama 2 locally instead.
- It's also easy to connect to OpenAI GPT models running in the cloud instead. This will require an OpenAI API key and it will not come for free.
