from questions import get_answers
from contact import get_contact_details
from template import generate_template


answers = get_answers()
contact_details = get_contact_details()
readme_content = generate_template(answers)
