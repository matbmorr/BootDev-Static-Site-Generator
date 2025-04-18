import textnode

def main():
    dummy_node = textnode.TextNode("This is some anchor text", textnode.TextType.LINK, "https://www.boot.dev")
    print(dummy_node)
    
main()
