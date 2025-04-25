import split_delimiter, split_nodes
from textnode import TextType, TextNode

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_delimiter.split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_delimiter.split_nodes_delimiter(nodes, "_", TextType.ITALICS)
    nodes = split_delimiter.split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes.split_nodes_image(nodes)
    nodes = split_nodes.split_nodes_link(nodes)

    return nodes