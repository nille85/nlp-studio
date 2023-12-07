from langchain.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.schema.messages import AIMessage
from rich import print
from langchain.chat_models.base import BaseChatModel
from rich.console import Console


class ChatBot:

    def __init__(self, console: Console, model : BaseChatModel, prompt: ChatPromptTemplate):
        self.console = console
        self.model = model
        self.prompt = prompt

    def talk(self, question : str):
        runnable =   self.prompt | self.model | StrOutputParser()
        self.console.print("[bold red]You:[/bold red] [red]" + question + "[/red]")
        print("\n")
        self.console.print(":robot: [bold green]NLP Studio Bot:[/bold green]")
        content = ""
        for chunk in runnable.stream({"question": question}):
            content += chunk
            print("[green]" + chunk + "[/green]", end="", flush=True)
        print("\n")
        self.prompt.messages.append(AIMessage(content=content))




class ChatBotFactory:

    @staticmethod
    def create() -> ChatBot:
        console = Console()
        model = ChatOllama(model="mistral", base_url = "http://localhost:11434")
        prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a very knowledgeable historian who provides accurate and eloquent answers to historical questions.",
            ),
            ("human", "{question}"),
        ]
        )
        return ChatBot(console, model, prompt)


