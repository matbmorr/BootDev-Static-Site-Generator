import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link

def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

def test_split_links(self):
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a link", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ],
        new_nodes,
    )

def test_split_empty_text(self):
    node = TextNode("", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertListEqual([node], new_nodes)

def test_split_adjacent_images(self):
    node = TextNode(
        "Text![img1](url1)![img2](url2)more text",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("Text", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "url1"),
            TextNode("img2", TextType.IMAGE, "url2"),
            TextNode("more text", TextType.TEXT),
        ],
        new_nodes,
    )


def test_image_at_start_and_end(self):
    node=TextNode(
        "![start](url1)middle![end](url2)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("start", TextType.IMAGE, "url1"),
            TextNode("middle", TextType.TEXT),
            TextNode("end", TextType.IMAGE, "url2"),
        ],
        new_nodes
    )

def test_link_at_start_and_end(self):
    node=TextNode(
        "[boot dev](https://boot.dev) is the best site after [GitHub](https://github.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("boot dev", TextType.LINK, "https://boot.dev"),
            TextNode("is the best site after ", TextType.TEXT),
            TextNode("GitHub", TextType.LINK, "https://github.com"),
        ],
        new_nodes
    )

def test_no_images_in_text(self):
    node = TextNode("This text has no images", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertListEqual([node], new_nodes)

def test_non_text_node_preserved(self):
    node = TextNode("existing link", TextType.LINK, "https://example.com")
    new_nodes = split_nodes_image([node])
    self.assertListEqual([node], new_nodes)

def test_adjacent_links(self):
    node = TextNode(
        "Check [this](url1)[that](url2) out",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("Check ", TextType.TEXT),
            TextNode("this", TextType.LINK, "url1"),
            TextNode("that", TextType.LINK, "url2"),
            TextNode(" out", TextType.TEXT),
        ],
        new_nodes
    )

def test_multiple_input_nodes(self):
    node1 = TextNode("Text with ![img](url1)", TextType.TEXT)
    node2 = TextNode("More text with ![another](url2)", TextType.TEXT)
    new_nodes = split_nodes_image([node1, node2])
    self.assertListEqual(
        [
            TextNode("Text with ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "url1"),
            TextNode("More text with ", TextType.TEXT),
            TextNode("another", TextType.IMAGE, "url2"),
        ],
        new_nodes
    )


if __name__ == "__main__":
    unittest.main()