import unittest
from markdown_extraction import extract_markdown_images, extract_markdown_links

def test_extraction_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extraction_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with an [link](https://bootdev.com)"
    )
    self.assertListEqual([("link", "https://bootdev.com")], matches)

def test_no_markdown_images(self):
    matches = extract_markdown_images(
        "This text has no images"
    )
    self.assertListEqual([], matches)

def test_no_markdown_links(self):
    matches = extract_markdown_links(
        "This text has no links"
    )
    self.assertListEqual([], matches)

def test_improperly_formatted_image(self):
    matches = extract_markdown_images(
        "Here is a broken image markdown: ![alt text(broken"
    )
    self.assertListEqual([], matches)  # Expect no matches since it's invalid markdown

def test_improperly_formatted_links(self):
    matches = extract_markdown_links(
        "Here is a broken link markdown: [link(nope"
    )
    self.assertListEqual([], matches)

