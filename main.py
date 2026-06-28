from questions import get_answers
from contact import get_contact_details
from contact import validate_contact_details
from template import generate_template
from writer import save_readme


class ReadmeGenerator:
    def __init__():
        self.answers = None
        self.contact_details = None
        self.readme_content = None

    def run(self):
        self.answers = get_answers()
        self.contact_details = get_contact_details()
        validate_contact_details(self.contact_details)

        self.readme_content = generate_template(self.answers, self.contact_details)
        save_readme(self.readme_content)

        print(self.readme_content)

generator = ReadmeGenerator()
generator.run()