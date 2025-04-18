import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_single_prop(self):
        node = HTMLNode("a", "", None, {"href": "https://boot.dev"})
        assert node.props_to_html() == ' href="https://boot.dev"'

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(
            "a", 
            "", 
            None, 
            {"href": "https://boot.dev", "target": "_blank", "class": "link"}
        )
        # Note: The exact order might vary since dictionaries don't guarantee order
        # You might need to check for presence of substrings instead of exact matching
        result = node.props_to_html()
        assert ' href="https://boot.dev"' in result
        assert ' target="_blank"' in result
        assert ' class="link"' in result

    def test_props_to_html_with_no_props(self):
        node = HTMLNode("p", "Hello, world!", None, None)
        assert node.props_to_html() == ""

    def test_repr(self):
        node = HTMLNode("div", "content", [], {"id": "main"})
        repr_result = repr(node)
        assert "div" in repr_result
        assert "content" in repr_result
        assert "id" in repr_result


if __name__ == "__main__":
    unittest.main()