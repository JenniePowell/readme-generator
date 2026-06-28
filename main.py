from questions import get_answers
from contact import get_contact_details
from contact import validate_contact_details
from template import generate_template
from writer import save_readme




answers = get_answers()
contact_details = get_contact_details()
validate_contact_details(contact_details)

readme_content = generate_template(answers, contact_details)
save_readme(readme_content)

print(readme_content)