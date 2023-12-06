import typer
from generate_image import generate_image 

app = typer.Typer()

@app.command("generate-image")
def create(prompt: str):
    print(f"Generating image from prompt: {prompt}")
    generate_image(prompt)

@app.command("summarize-text")
def create():
    print(f"Summarizing text")
 

if __name__ == "__main__":
    app()