import re

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
   

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_title(markdown):
    # Split the markdown into lines
    lines = markdown.split('\n')
    
    # Look for a line that starts with exactly one '#' followed by a space
    for line in lines:
        if line.startswith('# '):
            # Remove the '# ' and any extra whitespace
            return line[2:].strip()
    
    # If no title is found, raise an exception
    raise Exception("No h1 header found in markdown")