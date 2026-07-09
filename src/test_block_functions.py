import unittest
from block_functions import *
from blocktype import BlockType


class TestBlockFunctions(unittest.TestCase):
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

    def test_block_to_block_type_h1(self):
        block: str = "# lorem ipsum"
        self.assertEqual(
                BlockType.HEADING,
                block_to_block_type(block)
        )
    def test_block_to_block_type_h2(self):
        block: str = "## lorem ipsum"
        self.assertEqual(
                BlockType.HEADING,
                block_to_block_type(block)
        )
    def test_block_to_block_type_h3(self):
        block: str = "### lorem ipsum"
        self.assertEqual(
                BlockType.HEADING,
                block_to_block_type(block)
        )
    def test_block_to_block_type_h4(self):
        block: str = "#### lorem ipsum"
        self.assertEqual(
                BlockType.HEADING,
                block_to_block_type(block)
        )

    def test_block_to_block_type_h5(self):
        block: str = "##### lorem ipsum"
        self.assertEqual(
                BlockType.HEADING,
                block_to_block_type(block)
        )

    def test_block_to_block_type_h6(self):
        block: str = "###### lorem ipsum"
        self.assertEqual(
                BlockType.HEADING,
                block_to_block_type(block)
        )
    def test_block_to_block_type_heading_fail(self):
        block: str = "####### lorem ipsum"
        self.assertNotEqual(
                BlockType.HEADING,
                block_to_block_type(block)
        )
    def test_block_to_block_type_code(self):
        block: str = "```\nprint('hello, world!')```"
        self.assertEqual(
            BlockType.CODE,
            block_to_block_type(block)
        )
    def test_block_to_block_type_code_fail_1(self):
        block: str = "```\nprint('hello, world!')"
        self.assertNotEqual(
            BlockType.CODE,
            block_to_block_type(block)
        )
    def test_block_to_block_type_code_fail_2(self):
        block: str = "```print('hello, world!')```"
        self.assertNotEqual(
            BlockType.CODE,
            block_to_block_type(block)
        )
    def test_block_to_block_type_code_fail_3(self):
        block: str = "``\nprint('hello, world!')```"
        self.assertNotEqual(
            BlockType.CODE,
            block_to_block_type(block)
        )
    def test_block_to_block_type_quote(self):
        block: str = "> lorem ipsum"
        self.assertEqual(
            BlockType.QUOTE,
            block_to_block_type(block)
        )
    def test_block_to_block_type_quote_fail(self):
        block: str =  ">loremipsum"
        self.assertEqual(
            BlockType.QUOTE,
            block_to_block_type(block)
        )
    def test_block_to_block_type_ul(self):
        block: str = "- lorem ipsum\n- lorem ipsum"
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_to_block_type(block)
        )
    def test_block_to_block_type_ul_fail(self):
        block: str = "- lorem ipsum\n-lorem ipsum"
        self.assertNotEqual(
            BlockType.UNORDERED_LIST,
            block_to_block_type(block)
        )
    def test_block_to_block_type_ol(self):
        block: str = "1. lorem ipsum\n2. lorem ipsum"
        self.assertEqual(
            BlockType.ORDERED_LIST,
            block_to_block_type(block)
        )
    def test_block_to_block_type_ol_fail_1(self):
            block: str = "1.lorem ipsum\n2. lorem ipsum"
            self.assertNotEqual(
            BlockType.ORDERED_LIST,
            block_to_block_type(block)
        )
    def test_block_to_block_type_ol_fail_2(self):
            block: str = "1.lorem ipsum\n2. lorem ipsum"
            self.assertNotEqual(
            BlockType.ORDERED_LIST,
            block_to_block_type(block)
        )
    def test_block_to_block_type_ol_fail_3(self):
            block: str = "2.lorem ipsum\n2. lorem ipsum"
            self.assertNotEqual(
            BlockType.ORDERED_LIST,
            block_to_block_type(block)
        )
if __name__ == "__main__":
    unittest.main()
