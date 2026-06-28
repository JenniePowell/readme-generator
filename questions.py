from InquirerPy import prompt

# Get user input with InquirerPy
questions = [
    {"type": "input", "name": "title", "message": "What is your project title?"},
    {"type": "input", "name": "tagline", "message": "What is your project's tagline?"},
    {"type": "list", "name": "status", "choices": ["in development", "active", "deprecated"], "message": "What is the status of your project? (e.g., in progress, completed, deprecated)"},
    {"type": "input", "name": "description", "message": "Describe your project:"},
    {"type": "input", "name": "github_url", "message": "What is the GitHub repository URL?"},
    {"type": "input", "name": "installation", "message": "How do you install your project?"},
    {"type": "input", "name": "usage", "message": "How do you use your project?"},
    {"type": "list", "name": "license", "choices": ["MIT", "Apache 2.0", "GPL", "None"], "message": "What is the license for your project?"},
]

def get_answers():
    return prompt(questions)