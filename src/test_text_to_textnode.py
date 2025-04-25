import unittest
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes

def test_all_types(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ],
        new_nodes,
    )

def test_bold_text(self):
    text = "This is **bold** text"
    nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ],
        nodes,
    )

def test_italic_text(self):
    text = "This is _italic_ text"
    nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ],
        nodes,
    )

def test_code_block(self):
    text = "This is a `code block`"
    nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("", TextType.TEXT),
        ],
        nodes,
    )

def test_image(self):
    text = "This is an ![image](https://example.com/img.jpg)"
    nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.jpg"),
            TextNode("", TextType.TEXT),
        ],
        nodes,
    )

def test_link(self):
    text = "This is a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    self.assertListEqual(
        [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode("", TextType.TEXT),
        ],
        nodes,
    )