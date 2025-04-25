import re
from textnode import TextType, TextNode
from markdown_extraction import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Check if this is a text node
        if node.text_type != TextType.TEXT:  
            new_nodes.append(node)
            continue
        
        text = node.text
        images = extract_markdown_images(text)

        #if no images, add original node
        if len(images) == 0:
            new_nodes.append(node)
            continue
        
        remaining_text = text
        for image_alt, image_url in images:
            image_markdown = f"![{image_alt}]({image_url})"

            parts = remaining_text.split(image_markdown, 1)

            before_image = parts[0]

            if before_image:
                new_nodes.append(TextNode(before_image, TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
                

    
def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Check if this is a text node
        if node.text_type != TextType.TEXT:  
            new_nodes.append(node)
            continue
        
        text = node.text
        links = extract_markdown_links(text)

        #if no images, add original node
        if len(links) == 0:
            new_nodes.append(node)
            continue
        
        remaining_text = text
        for anchor_text, link_url in links:
            link_markdown = f"[{anchor_text}]({link_url})"

            parts = remaining_text.split(link_markdown, 1)

            before_link = parts[0]

            if before_link:
                new_nodes.append(TextNode(before_link, TextType.TEXT))

            new_nodes.append(TextNode(anchor_text, TextType.LINK, link_url))

            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes