import os
import click
from dotenv import load_dotenv
from prompt_toolkit import prompt, print_formatted_text, HTML
from langchain_core.messages import AIMessage, HumanMessage

from graph_builder import GraphBuilder

# loading env variables
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
MODEL = "gpt-4o"

def start_chat(builder: GraphBuilder):
    """Simple CLI Chat application."""

    user_input = prompt(HTML(f"<b>[You]</b>: "))
    if user_input.lower().strip() in ["quit", "exit", "q"]:
        raise EOFError
    if user_input.lower() == "":
        raise KeyboardInterrupt
    
    builder.add_message(HumanMessage(content=user_input, name="User"))
    result = builder.graph.invoke({"messages": builder.initial_messages})
    # print(result)
    reply = result['messages'][-1]
    builder.add_message(AIMessage(content=reply.content, name="Model"))
    print_formatted_text(HTML(f"<b>[Assistant]</b>: <ansigreen>{reply.content}</ansigreen>"))

@click.command()
@click.option('--temperature', default=0.7, type=float, help='Set the randomness of responses.')
def main(temperature):
    click.echo(f"Using model {MODEL} with temperature: {temperature}")
    click.echo("Type 'exit' to quit.")
    builder = GraphBuilder(model=MODEL, temperature=temperature)
    builder.build_graph()

    while True:
        try:
            start_chat(builder)
        except KeyboardInterrupt:
            continue
        except EOFError:
            click.echo("\nGoodbye!")
            break

if __name__ == "__main__":
    main()