import unittest
from markdown_to_blocks import markdown_to_blocks

def test_markdown_to_blocks(self):
    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

def test_markdown_empty_lines(self):
    md = """
    This is **bolded** paragraph

    

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )


def test_markdown_whitespace(self):
    md = """
        This is **bolded** paragraph

    

    This is another paragraph with _italic_ text and `code` here   
        This is the same paragraph on a new line    

    - This is a list
    - with items    
    """
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

def test_markdown_empty(self):
    md = ""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks, [],
    )

def test_markdown_one_line(self):
    md= "This is **bolded**"
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        ["This is **bolded**"],
    )

if __name__ == "__main__":
    unittest.main()