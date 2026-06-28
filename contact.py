from InquirerPy import prompt

contact_questions = [
        {"type": "input", "name": "author", "message": "Who is the author of the project?"},
        {"type": "input", "name": "contact", "message": "Email address for contact:"},
    ]

def get_contact_details():
    return prompt(contact_questions)