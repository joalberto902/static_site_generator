import re
from textnode import TextNode, TextType


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
        open_delimiter: bool = False
        text = node.text
        while True:
            find_delimiter: list[str] = text.split(delimiter, maxsplit=1)
            if text == find_delimiter[0]:
                if open_delimiter:
                    raise ValueError(f"{delimiter} was not closed on{node.text}")
                if find_delimiter[0] != "":
                    new_nodes.append(TextNode(
                        find_delimiter[0], 
                        TextType.PLAIN_TEXT
                    ))
                break
            if find_delimiter[0] == "":
                text = find_delimiter[1]
                open_delimiter = not open_delimiter
                continue
            if open_delimiter:
                text = find_delimiter[1]
                new_nodes.append(TextNode(
                    find_delimiter[0],
                    text_type
                ))
            else:
                text = find_delimiter[1]
                new_nodes.append(TextNode(
                    find_delimiter[0], 
                    TextType.PLAIN_TEXT
                ))
            open_delimiter = not open_delimiter
    return new_nodes


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
    apply_bold: list[TextNode] = split_nodes_delimiter(apply_italic, "**", TextType.BOLD_TEXT)

    return apply_bold

def extract_title(markdown: str) -> str:
    title = re.findall(r"^\s*#{1}\s+(.*)", markdown, re.MULTILINE)
    if not title:
        raise Exception("Markdown has no title")
    return title[0]















