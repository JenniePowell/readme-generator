def generate_template(answers, contact):
    return f"""# {answers['title']}

{answers['tagline']}

## Status

{answers['status']}

## Description

{answers['description']}

## GitHub Repository

{answers['github_url']}

## Installation

{answers['installation']}

## Usage

{answers['usage']}

## License

{answers['license']}

## Author

{contact['author']}

## Contact

{contact['contact']}
    
"""