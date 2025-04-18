from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eg__(self, TextNode_2):
        if TextNode_1 == TextNode_2:
            return True
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")


