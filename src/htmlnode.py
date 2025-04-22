class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
       
        return result
    
    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("no value found")
        if self.tag is None:
            return self.value
        #print(f"Rendering LeafNode with props: {self.props}")  # Debug
        attributes = ""
        if isinstance(self.props, dict) and self.props:
            attributes = " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

        # Construct the full HTML string
        html = f'<{self.tag}{attributes}>{self.value}</{self.tag}>'
        return html
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag found")
        if self.children is None:
            raise ValueError("no children found")
        html = f"<{self.tag}"
        attributes = ""
        if isinstance(self.props, dict) and self.props:
            attributes = " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
        html += ">"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"

        return html