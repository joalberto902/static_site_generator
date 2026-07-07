import unittest
from textnode import *
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_emptystring_plaintext(self):
        node = TextNode("", TextType.PLAIN_TEXT)
        node2 = TextNode("", TextType.PLAIN_TEXT)
        self.assertEqual(node, node2)
    def test_string_plaintext(self):
        node = TextNode("This is a node text", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a node text", TextType.PLAIN_TEXT)
        self.assertEqual(node, node2)
    def test_emptystring_boldtext(self):
        node = TextNode("", TextType.BOLD_TEXT)
        node2 = TextNode("", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_string_boldtext(self):
        node = TextNode("This is a node text", TextType.BOLD_TEXT)
        node2 = TextNode("This is a node text", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_emptystring_italictest(self):
        node = TextNode("", TextType.ITALIC_TEXT)
        node2 = TextNode("", TextType.ITALIC_TEXT)
        self.assertEqual(node, node2)
    def test_string_italictest(self):
        node = TextNode("This is a node string", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a node string", TextType.ITALIC_TEXT)
        self.assertEqual(node, node2)
    def test_emptystring_codetext(self):
        node = TextNode("", TextType.CODE_TEXT)
        node2 = TextNode("", TextType.CODE_TEXT)
        self.assertEqual(node, node2)
    def test_string_codetext(self):
        node = TextNode("This is a node string", TextType.CODE_TEXT)
        node2 = TextNode("This is a node string", TextType.CODE_TEXT)
        self.assertEqual(node, node2)
    def test_emptystring_links(self):
        node = TextNode("", TextType.LINKS, "https://boot.dev/")
        node2 = TextNode("", TextType.LINKS,"https://boot.dev/")
        self.assertEqual(node, node2)
    def test_string_links(self):
        node = TextNode("This is a node string", TextType.LINKS, "https://boot.dev/")
        node2 = TextNode("This is a node string", TextType.LINKS, "https://boot.dev/")
        self.assertEqual(node, node2)
    def test_emptystring_images(self):
        node = TextNode("", TextType.IMAGES, "https://boot.dev/")
        node2 = TextNode("", TextType.IMAGES, "https://boot.dev/")
        self.assertEqual(node, node2)
    def test_string_images(self):
        node = TextNode("This is a node string", TextType.IMAGES, "https://boot.dev/")
        node2 = TextNode("This is a node string", TextType.IMAGES, "https://boot.dev/")
        self.assertEqual(node, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    def test_italic_text(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")
    def test_code_text(self):
        node = TextNode("This is a text node", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")
    def test_link_text(self):
        node = TextNode("This is a text node", TextType.LINKS, "https://boot.dev/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href":"https://boot.dev/"})
    def test_image_text(self):
        node = TextNode("This is a text node", TextType.IMAGES, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"https://boot.dev","alt":"This is a text node"  })
if __name__ == "__main__":
    unittest.main()
