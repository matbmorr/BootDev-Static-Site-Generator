from textnode import text_node_to_html_node, TextNode, TextType
from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode
from text_node_management import text_to_children

def markdown_to_blocks(markdown):
        return [block.strip() for block in markdown.strip().split('\n\n') if block.strip()]



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            node = ParentNode("p", text_to_children(block))
        elif block_type == BlockType.HEADING:
            # Count the number of # to determine heading level
            level = 0
            for char in block:
                if char == '#':
                    level += 1
                else:
                    break
            # Remove the # characters and any space after them
            content = block[level:].strip()
            node = ParentNode(f"h{level}", text_to_children(content))
        elif block_type == BlockType.CODE:
            # Special case: don't parse inline markdown for code blocks
            # Remove the ``` at the beginning and end
            content = "\n".join(block.split("\n")[1:-1])
            code_node = text_node_to_html_node(TextNode(content, TextType.TEXT))
            node = ParentNode("pre", [ParentNode("code", [code_node])])
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            content = "\n".join([line[1:].strip() for line in lines])
            node = ParentNode("blockquote", text_to_children(content))
        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            li_nodes = []
            for item in items:
                content = item[2:].strip()
                li_nodes.append(ParentNode("li", text_to_children(content)))
            node = ParentNode("ul", li_nodes)    
        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            li_nodes = []
            for item in items:
                prefix_end = item.find(". ") + 2
                content = item[prefix_end:].strip()
                li_nodes.append(ParentNode("li", text_to_children(content)))
            node = ParentNode("ol", li_nodes)    
        
        children.append(node)
    
    # Create the parent div containing all blocks
    return ParentNode("div", children)


