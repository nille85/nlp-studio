# NLP Studio

NLP Studio is a CLI (command line interface) written in Python to showcase what can be done with NLP and Large Language Models.

The CLI is built using [Typer](https://typer.tiangolo.com/).


# Use Cases

## Chatbot

The command:
```
python3 main.py chatbot
```
### Example

![Screenshot 2023-12-08 at 11 48 24](https://github.com/nille85/nlp-studio/assets/10157390/156bfaed-fe7d-45b9-a146-924542221d0b)

### Prerequisites

#### Ollama & Mistral
This command interfaces with a locally downloaded Mistral LLM model. It runs locally on my machine. I use [Ollama](https://ollama.ai/) to download, run, and expose these large language models locally.
For the installation of Ollama and how to run models locally using Ollama can be found [here](https://github.com/jmorganca/ollama)


### Implementation
To simplify the implementation of a chatbot, I make use of the [LangChain](https://python.langchain.com/docs/get_started/introduction) library
Check out [this documentation](https://python.langchain.com/docs/use_cases/chatbots) on how to implement a simple chatbot.

If you want to use emojis, check out [this link](https://www.webfx.com/tools/emoji-cheat-sheet/).

### Adaptation

- This example can easily be adapted, to run Llama 2 locally instead.
- It's also easy to connect to OpenAI GPT models running in the cloud instead. This will require an OpenAI API key and it will not come for free.

## Generating Images

The command:

```
python3 main.py generate-image [PROMPT]
```
### Examples
```
python3 main.py generate-image "A racoon taking a bath in the desert surrounded by camels"
```
![image_1701877430_83017](https://github.com/nille85/nlp-studio/assets/10157390/6d8c5f9e-0cdb-479e-90ac-64d218719022)

```
python3 main.py generate-image "A lizzard enjoying a soft-drink on the table of sunny terrace at the coastline"
```
![image_1701877705_19721](https://github.com/nille85/nlp-studio/assets/10157390/be5301fb-64ed-4b64-a55e-c4ac992200ba)

### Model
The pre-trained model that is used to generate the images is [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo)

### Prerequisites

Because I am running this on a Macbook with an Apple M1 chip, I've had to configure PyTorch for using the [MPS backend](https://pytorch.org/docs/stable/notes/mps.html) instead of [CUDA](https://en.wikipedia.org/wiki/CUDA). Cuda can only be used if your machine is running a NVIDIA GPU.  

Use the following command to generate images:

```
python3 main.py generate-image [PROMPT]
```





