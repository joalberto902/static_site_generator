import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode#type:ignore

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode(tag = "p")
        node2 = HTMLNode(tag = "p")
        self.assertEqual(node, node2)
    def test_value(self):
        node = HTMLNode(value="This a possible value")
        node2 = HTMLNode(value="This a possible value")
        self.assertEqual(node, node2)
    def test_children(self):
        children_1 = HTMLNode(tag = "p")
        children_2 = HTMLNode(value="This a possible value")
        node = HTMLNode(children=[children_1, children_2])
        node2 = HTMLNode(children=[children_1, children_2])
        self.assertEqual(node, node2)
    def test_props(self):
        props = {
            "href": "https://boot.dev/",
            "target": "_blank",
        }
        node = HTMLNode(props = props)
        html =  node.props_to_html()
        compare_string = ' href="https://boot.dev/" target="_blank"'
        self.assertEqual(html, compare_string)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://boot.dev/"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev/">Hello, world!</a>')
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")
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
    def test_to_html_with_lots_leaf_chidren(self):
        node = ParentNode(
            "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    def test_to_html_with_lots_leaf_chidren_with_props(self):
        node = ParentNode(
            "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode("a", "Normal text", {"href":"https://boot.dev/"}),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b><a href=\"https://boot.dev/\">Normal text</a><i>italic text</i>Normal text</p>"
        )
if __name__ == "__main__":
    unittest.main()
