from InquirerPy import prompt
from utils import validate_email

contact_questions = [
        {"type": "input", "name": "author", "message": "Who is the author of the project?"},
        {"type": "input", "name": "contact", "message": "Email address for contact:"},
    ]

def get_contact_details():
    return prompt(contact_questions)

def validate_contact_details(contact_details):
    if not validate_email(contact_details["contact"]):
        raise ValueError("Invalid email address provided.")