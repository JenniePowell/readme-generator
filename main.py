from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import time

console = Console()

# Get user input with Inquirer
questions = [
    {"type": "input", "name": "title", "message": "What is your project title?"},
    {"type": "input", "name": "tagline", "message": "What is your project's tagline?"},
    {"type": "input", "name": "description", "message": "Describe your project:"},
    {"type": "input", "name": "github_url", "message": "What is the GitHub repository URL?"},
    {"type": "list", "name": "status", "message": "What is the status of your project? (e.g., in progress, completed, deprecated)"},
    {"type": "input", "name": "installation", "message": "How do you install your project?"},
    {"type": "input", "name": "usage", "message": "How do you use your project?"},
    {"type": "input", "name": "author", "message": "Who is the author of the project?"},
    {"type": "input", "name": "contact", "message": "Email address for contact:"},
    {"type": "list", "name": "license", "choices": ["MIT", "Apache 2.0", "GPL", "None"]}
answers = prompt(questions)

# Display a formatted message with Rich
console.print(
    f"Hello, [bold {answers['color']}] {answers['name']}![/bold {answers['color']}]",
    style=answers["color"],
)
