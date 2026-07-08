import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType,
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue 
        text_split = node_transform(
            parse_delimiters(
                node.text,
                delimiter, 
            ),
            text_type,
        ) 
        new_nodes.extend(text_split)

    return new_nodes

def parse_delimiters(
    text: str,
    delimiter: str, 
) -> list[str]:
    delimited: list[str] = list(filter(None, text.split(delimiter)))
    if len(delimited)%2 == 0:
        raise ValueError("Markdown text is invalid")
    return delimited

def node_transform(
    texts: list[str],
    text_type: TextType,
) -> list[TextNode]:
    transformed: list[TextNode] = []
    for i, text in enumerate(texts):
        type_text: TextType = text_type if i%2 else TextType.PLAIN_TEXT
        transformed.append(
            TextNode(
                text,
                type_text
            )
        )
    return transformed


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches

def split_by_links(text:str) -> list[str]:
    return list(filter(None, re.split(r"((?<!\!)\[.*?\]\(.*?\))", text)))

def split_by_images(text: str) -> list[str]:
    return list(filter(None, re.split(r"(\!\[.*?\]\(.*?\))", text)))

def split_nodes_image(nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)

            continue
        texts: list[str] = split_by_images(node.text)
        for text in texts:
            images = extract_markdown_images(text)
            if images:
                alt, url = images.pop()
                new_nodes.append(TextNode(
                    alt,
                    TextType.IMAGES,
                    url
                ))
                continue

            new_nodes.append(TextNode(
                text,
                TextType.PLAIN_TEXT
            ))
    return new_nodes


def split_nodes_link(nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)

            continue
        texts: list[str] = split_by_links(node.text)
        for text in texts:
            images = extract_markdown_links(text)
            if images:
                alt, url = images.pop()
                new_nodes.append(TextNode(
                    alt,
                    TextType.LINKS,
                    url
                ))
                continue

            new_nodes.append(TextNode(
                text,
                TextType.PLAIN_TEXT
            ))
    return new_nodes


def text_to_textnodes(text:str) -> list[TextNode]:
    original: TextNode = TextNode(text, TextType.PLAIN_TEXT)
    apply_links: list[TextNode] = split_nodes_link([original])
    apply_images: list[TextNode] = split_nodes_image(apply_links)
    apply_code: list[TextNode] = split_nodes_delimiter(apply_images, "`", TextType.CODE_TEXT)
    apply_italic: list[TextNode] = split_nodes_delimiter(apply_code, "_", TextType.ITALIC_TEXT)
    apply_bold: list[TextNode] = split_nodes_delimiter(apply_italic, "*", TextType.BOLD_TEXT)

    return apply_bold












