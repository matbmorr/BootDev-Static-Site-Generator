from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Check if this is a text node (you need to use the correct constant)
        if node.text_type != TextType.TEXT:  
            new_nodes.append(node)
            continue
        
        text = node.text
        
        # Find the first delimiter
        first_delimiter_pos = text.find(delimiter)
        if first_delimiter_pos == -1:
            # No delimiter found, just add the node as is
            new_nodes.append(node)
            continue
            
        # Find the second delimiter
        second_delimiter_pos = text.find(delimiter, first_delimiter_pos + len(delimiter))
        if second_delimiter_pos == -1:
            # Found only one delimiter - that's an error
            raise ValueError(f"Unclosed delimiter: {delimiter}")
            
        # Split the text into three parts
        before_text = text[:first_delimiter_pos]
        delimited_text = text[first_delimiter_pos + len(delimiter):second_delimiter_pos]
        after_text = text[second_delimiter_pos + len(delimiter):]
        
        # Add the parts as nodes
        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))
            
        new_nodes.append(TextNode(delimited_text, text_type))
        

        # Process the remaining text (even if it's empty)
        # Create a new node with the remaining text
        remaining_node = TextNode(after_text, TextType.TEXT)
            
        # Recursively process this node (important for multiple delimiters)
        remaining_nodes = split_nodes_delimiter([remaining_node], delimiter, text_type)
            
        # Add all resulting nodes to our list
        new_nodes.extend(remaining_nodes)

                

    return new_nodes