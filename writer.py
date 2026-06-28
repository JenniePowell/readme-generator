def save_readme(content, filename="README.md"):
    with open(filename, "w") as f:
        f.write(content)