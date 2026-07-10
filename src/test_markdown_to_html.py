import unittest

from htmlnode import *
from textnode import *
from blocktype import *
from inline_functions import *
from block_functions import *
from markdown_to_html import *


class TestMardownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_heading_h1(self):
        md = "# Heading"

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><h1>Heading</h1></div>"
        )
    def test_heading_h2(self):
        md = "## Heading"

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><h2>Heading</h2></div>"
        )
    def test_quote(self):
        md = "> Hello"

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><blockquote>Hello</blockquote></div>"
        )
    def test_unordered_list(self):
        md = """- Apple
    - Banana
    - Orange"""

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><ul><li>Apple</li><li>Banana</li><li>Orange</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """1. Apple
    2. Banana
    3. Orange"""

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><ol><li>Apple</li><li>Banana</li><li>Orange</li></ol></div>"
        )
    def test_heading_with_bold(self):
        md = "# **Heading**"

        node = markdown_to_html_node(md)
    
        self.assertEqual(
            node.to_html(),
            "<div><h1><b>Heading</b></h1></div>"
        )
    def test_heading_with_italic(self):
        md = "# _Heading_"

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><h1><i>Heading</i></h1></div>"
        )
    def test_link(self):
        md = "[Boot.dev](https://boot.dev)"

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            '<div><p><a href="https://boot.dev">Boot.dev</a></p></div>'
        )
    def test_image(self):
        md = "![Logo](https://example.com/logo.png)"

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            '<div><p><img src="https://example.com/logo.png" alt="Logo"></img></p></div>'
        )
    def test_paragraph_with_link(self):
        md = "Visit [Boot.dev](https://boot.dev)"

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            '<div><p>Visit <a href="https://boot.dev">Boot.dev</a></p></div>'
        )

    def test_paragraph_with_image(self):
        md = "Logo: ![Logo](image.png)"

        node = markdown_to_html_node(md)

        self.assertIn("<img", node.to_html())
    def test_empty_document(self):
        md = ""

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div></div>"
        )
    def test_multiple_headings(self):
        md = """# A

    ## B"""

        node = markdown_to_html_node(md)

        html = node.to_html()

        self.assertIn("<h1>A</h1>", html)
        self.assertIn("<h2>B</h2>", html)
    def test_heading_and_paragraph(self):
        md = """# Title

    Paragraph."""

        node = markdown_to_html_node(md)

        html = node.to_html()

        self.assertIn("<h1>Title</h1>", html)
        self.assertIn("<p>Paragraph.</p>", html)
    def test_empty_code_block(self):
        md = """```
    ```"""

        node = markdown_to_html_node(md)

        self.assertIn("<pre>", node.to_html())
    def test_unordered_list_italic(self):
        md = """- _Apple_
    - Banana"""

        node = markdown_to_html_node(md)

        html = node.to_html()

        self.assertIn("<i>Apple</i>", html)










    
if __name__ == "__main__":
    unittest.main()
