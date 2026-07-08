import unittest
from inline_functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestFunction(unittest.TestCase):
    def test_bold(self):
        node = TextNode(
            "This is some **text** to test",
            TextType.PLAIN_TEXT,
        )
        res = [
            TextNode("This is some ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" to test", TextType.PLAIN_TEXT)
        ]

        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD_TEXT), res)
    def test_italic(self):
        node = TextNode(
            "This is some _text_ to test",
            TextType.PLAIN_TEXT,
        )
        res = [
            TextNode("This is some ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.ITALIC_TEXT),
            TextNode(" to test", TextType.PLAIN_TEXT)
        ]

        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT), res)

    def test_code(self):
        node = TextNode(
            "This is some `text` to test",
            TextType.PLAIN_TEXT,
        )
        res = [
            TextNode("This is some ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.CODE_TEXT),
            TextNode(" to test", TextType.PLAIN_TEXT)
        ]

        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE_TEXT), res)
    def test_various_nodes(self):
        node = TextNode(
            "This is some `text` to test",
            TextType.PLAIN_TEXT,
        )
        node2 = TextNode(
            "This is some `text` to test",
            TextType.PLAIN_TEXT,
        )
        node3 = TextNode(
            "This is some `text` to test",
            TextType.PLAIN_TEXT,
        )
        res = [
            TextNode("This is some ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.CODE_TEXT),
            TextNode(" to test", TextType.PLAIN_TEXT),
            TextNode("This is some ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.CODE_TEXT),
            TextNode(" to test", TextType.PLAIN_TEXT),
            TextNode("This is some ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.CODE_TEXT),
            TextNode(" to test", TextType.PLAIN_TEXT)
        ]

        self.assertEqual(split_nodes_delimiter([node, node2, node3], "`", TextType.CODE_TEXT), res)
    def test_error(self):
        node = TextNode(
            "This is some `text to test",
            TextType.PLAIN_TEXT,
        )
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
    def test_various_and_delimiters(self):
        node = TextNode(
            "This is some `text` to test",
            TextType.PLAIN_TEXT,
        )
        node2 = TextNode(
            "This is some _text_ to test",
            TextType.PLAIN_TEXT,
        )
        node3 = TextNode(
            "This is some **text** to test",
            TextType.PLAIN_TEXT,
        )
        res = [
            TextNode("This is some ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.CODE_TEXT),
            TextNode(" to test", TextType.PLAIN_TEXT),
            node2,
            node3
        ]

        self.assertEqual(split_nodes_delimiter([node, node2, node3], "`", TextType.CODE_TEXT), res)
    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        res = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), res)
    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        res =  [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), res)
    def test_extract_links_with_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_links(text), [])
    def test_extract_images_with_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_images(text), [])
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.LINKS, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.LINKS, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links_no_empty(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.LINKS, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_empty(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
    def test_text_to_textnodes1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.PLAIN_TEXT),
                TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
            ],
            new_nodes
        )
    def test_text_to_textnodes2(self):
        text = "This plain text has **bold words**, _italic words_, a tiny `function`, an image ![icon](https://placehold.co/15x15) and a [link](https://example.com)." 
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This plain text has ", TextType.PLAIN_TEXT),
                TextNode("bold words", TextType.BOLD_TEXT),
                TextNode(", ", TextType.PLAIN_TEXT),
                TextNode("italic words", TextType.ITALIC_TEXT),
                TextNode(", a tiny ", TextType.PLAIN_TEXT),
                TextNode("function", TextType.CODE_TEXT),
                TextNode(", an image ", TextType.PLAIN_TEXT),
                TextNode("icon", TextType.IMAGES, "https://placehold.co/15x15"),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINKS, "https://example.com"),
                TextNode(".", TextType.PLAIN_TEXT),
            ]
            ,
            new_nodes
        )
if __name__ == "__main__":
    unittest.main()
