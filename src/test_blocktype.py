import unittest
from blocktype import BlockType, block_to_block_type

    
def test_paragraph_blocks(self):
    self.assertEqual(block_to_block_type("This is a normal paragraph"), BlockType.paragraph)
    self.assertEqual(block_to_block_type("Multiple\nline\nparagraph"), BlockType.paragraph)
    self.assertEqual(block_to_block_type("123"), BlockType.paragraph)

def test_heading_blocks(self):
    self.assertEqual(block_to_block_type("# Heading 1"), BlockType.heading)
    self.assertEqual(block_to_block_type("## Heading 2"), BlockType.heading)
    self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.heading)
    # Test heading with multiple lines
    self.assertEqual(block_to_block_type("# Heading\nwith multiple lines"), BlockType.heading)
    
    # This should NOT be a heading (no space after #)
    self.assertEqual(block_to_block_type("#Not a heading"), BlockType.paragraph)

def test_code_blocks(self):
    self.assertEqual(block_to_block_type("```\ncode here\n```"), BlockType.code)
    self.assertEqual(block_to_block_type("```\nmulti\nline\ncode\n```"), BlockType.code)
    self.assertEqual(block_to_block_type("```\n```"), BlockType.code)  # Empty code block

def test_quote_blocks(self):
    self.assertEqual(block_to_block_type("> This is a quote"), BlockType.quote)
    self.assertEqual(block_to_block_type("> Line 1\n> Line 2\n> Line 3"), BlockType.quote)

    #This should not be a quote (no > before 2nd line)
    self.assertEqual(block_to_block_type("> Line1\n Line2\n> Line 3"), BlockType.quote)

def test_unordered_list_blocks(self):
    # Simple single-item list
    self.assertEqual(block_to_block_type("- Item 1"), BlockType.unordered_list)
    
    # Multi-item list
    self.assertEqual(block_to_block_type("- Item 1\n- Item 2\n- Item 3"), BlockType.unordered_list)
    
    # List with complex items
    self.assertEqual(block_to_block_type("- Item with multiple\n  lines of text\n- Another item"), BlockType.unordered_list)
    
    # Edge cases that should NOT be unordered lists
    self.assertEqual(block_to_block_type("-Not a list item"), BlockType.paragraph)  # No space after dash
    self.assertEqual(block_to_block_type("- Item 1\nNot a list item"), BlockType.paragraph)  # Not all lines start with dash

def test_ordered_list_blocks(self):
    # Simple single-item list
    self.assertEqual(block_to_block_type("1. Item 1"), BlockType.ordered_list)
    
    # Multi-item list
    self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2\n3. Item 3"), BlockType.ordered_list)
    
    # List with complex items
    self.assertEqual(block_to_block_type("1. Item with multiple\n   lines of text\n2. Another item"), BlockType.ordered_list)
    
    # Edge cases that should NOT be ordered lists
    self.assertEqual(block_to_block_type("1.Not a list item"), BlockType.paragraph)  # No space after number
    self.assertEqual(block_to_block_type("1. Item 1\n3. Item 3"), BlockType.paragraph)  # Numbers not sequential
    self.assertEqual(block_to_block_type("0. Item 0\n1. Item 1"), BlockType.paragraph)
    

if __name__ == "__main__":
    unittest.main()