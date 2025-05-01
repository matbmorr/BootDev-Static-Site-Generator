from markdown_to_blocks import markdown_to_html_node
from markdown_extraction import extract_title
import htmlnode

def generate_page(from_path, template_path, dest_path, basepath):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path, 'r') as file:
        markdown_content = file.read()

    with open(template_path, 'r') as file:
        template_content = file.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)
    
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    # Replace href="/" with href="{basepath}"
    final_html = final_html.replace('href="/', f'href="{basepath}')
    # Replace src="/" with src="{basepath}"
    final_html = final_html.replace('src="/', f'src="{basepath}')
    
    import os
    
    # Make sure the directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the file
    with open(dest_path, 'w') as file:
        file.write(final_html)


import os

def generate_pages_recursive(content_dir, template_path, dest_dir, basepath):
    # Walk through all directories under content_dir
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            # Process only markdown files
            if file.endswith(".md"):
                # Get the full path of the source file
                source_path = os.path.join(root, file)
                
                # Calculate the relative path from content_dir
                rel_path = os.path.relpath(source_path, content_dir)
                
                # Create the destination path, replacing .md with .html
                # but preserve the directory structure
                dest_path = os.path.join(
                    dest_dir, 
                    os.path.splitext(rel_path)[0] + ".html"
                )
                
                # Generate the page
                generate_page(source_path, template_path, dest_path, basepath)