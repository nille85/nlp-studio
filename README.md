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