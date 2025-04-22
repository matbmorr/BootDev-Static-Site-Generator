import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    # LeafNode Tests
    def test_leafnode_to_html_with_tag(self):
        node = LeafNode("b", "Bold Text")
        assert node.to_html() == "<b>Bold Text</b>"

    def test_leafnode_to_html_with_attributes(self):
        node = LeafNode("a", "Click Here", {"href": "https://example.com"})
        html = node.to_html()
        #print(f"Generated HTML: {html}")  # Debugging helper: print the output
        assert html == '<a href="https://example.com">Click Here</a>'  # Check the output


    def test_leafnode_to_html_no_tag(self):
        node = LeafNode(None, "Just Text")
        assert node.to_html() == "Just Text"

    def test_leafnode_to_html_raises_error_without_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


    # ParentNode Tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()