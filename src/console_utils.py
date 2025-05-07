import time

from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt

console = Console()


def print_markdown(text: str) -> None:
    """
    Print the given text as markdown in the console.

    Args:
        text (str): The text to print as markdown.
    """
    md = Markdown(text)
    console.print(md)


def prompt_user(prompt: str) -> str:
    """
    Prompt the user for input and return the response.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        str: The user's input.
    """
    return Prompt.ask(prompt)


def type_writer_effect_machine(message: str, is_dim: bool, delay: float = 0.01):
    """
    Simulate a typewriter effect for the given message.

    Args:
        message (str): The message to display.
        delay (float): The delay between each character.
    """
    for char in message:
        console.print(char, end="", style="dim" if is_dim else None, markup=True)
        time.sleep(delay)
    print()  # Move to the next line after the message is printed
