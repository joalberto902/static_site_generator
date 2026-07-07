import unittest
from textnode import TextNode, TextType

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


if __name__ == "__main__":
    unittest.main()
