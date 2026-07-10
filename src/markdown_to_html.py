from htmlnode import *
from textnode import * 
from blocktype import *
from inline_functions import *
from block_functions import *

def markdown_to_html_node(markdown: str) -> HTMLNode:
    markdown_blocks: list[str] = markdown_to_blocks(markdown)
    final_html: HTMLNode = ParentNode("div", [])
    if markdown == "":
        return final_html
    for block in markdown_blocks:
        block_type: BlockType = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                hashtags, text = block.split(" ", maxsplit=1)
                heading: HTMLNode = ParentNode(f"h{len(hashtags)}",text_to_html_nodes(text.strip())) 
                final_html.set_children(heading)
            case BlockType.CODE:
                wrapper: HTMLNode = ParentNode("pre", [])
                code_text: HTMLNode = LeafNode("code", block[4:-3])
                wrapper.set_children(code_text)
                final_html.set_children(wrapper)
            case BlockType.QUOTE:
                text = block.split('>', maxsplit=1)[1].strip()
                quote: HTMLNode = ParentNode("blockquote", text_to_html_nodes(text))
                final_html.set_children(quote)
            case BlockType.UNORDERED_LIST:
                lst: HTMLNode = ParentNode("ul", [])
                for item in block.split("\n"):
                    if not item.strip():
                        continue
                    item = item.strip()
                    item = item.strip()
                    text = item.split(" ", maxsplit=1)[1].strip()
                    new_item: HTMLNode = ParentNode("li", text_to_html_nodes(text))
                    lst.set_children(new_item)
                final_html.set_children(lst)
            case BlockType.ORDERED_LIST:
                lst: HTMLNode = ParentNode("ol", [])
                for item in block.split("\n"):
                    if not item.strip():
                        continue
                    item = item.strip()
                    text = item.split(" ", maxsplit=1)[1].strip()
                    new_item: HTMLNode = ParentNode("li", text_to_html_nodes(text))
                    lst.set_children(new_item)
                final_html.set_children(lst)
            case BlockType.PARAGRAPH:
                paragraph: HTMLNode = ParentNode("p", text_to_html_nodes(block))
                final_html.set_children(paragraph)
    return final_html

def text_to_html_nodes(markdown: str) -> list[HTMLNode]:
    children: list[HTMLNode] = []
    for text_node in text_to_textnodes(markdown.replace("\n"," ")):
        children.append(text_node_to_html_node(text_node))
    return children

