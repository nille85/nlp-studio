import typer
from rich.prompt import Prompt
from rich import print
from rich.console import Console
from generate_image import generate_image 
from chatbot import ChatBotFactory






app = typer.Typer()
console = Console()

@app.command("generate-image")
def create(prompt: str):
    console.print(f"[bold green]Generating image from prompt: {prompt}[/bold green] :rocket:")
    generate_image(prompt)

@app.command("chatbot")
def chat():
    chat_bot = ChatBotFactory.create()
    console.print("[bold green]Hi there :waving_hand:, I'm the NLP Studio Bot, how can I help you today?[/bold green]")
    while(True):
        question = Prompt.ask("")
        if(question != '\\bye'):
           chat_bot.talk(question)
        else:
            break


        
 

if __name__ == "__main__":
    app()