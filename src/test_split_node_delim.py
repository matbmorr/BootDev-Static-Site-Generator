import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_simple_delimiter_pair(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.NORMAL)
    
    def test_multiple_delimiter_pairs(self):
        node = TextNode("This has `code` and another `code block`", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "This has ")
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " and another ")
        self.assertEqual(result[3].text, "code block")
        self.assertEqual(result[3].text_type, TextType.CODE)
        self.assertEqual(result[4].text, "")
    
    def test_different_delimiter_types(self):
        # Test bold
        node = TextNode("This has **bold** text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This has ")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.NORMAL)
        
        # Test italic
        node = TextNode("This has _italic_ text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This has ")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.NORMAL)

if __name__ == "__main__":
    unittest.main()