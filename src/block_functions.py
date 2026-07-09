import re
from blocktype import BlockType

def markdown_to_blocks(markdown: str) -> list[str]:
    return list(filter(None, map(lambda x: x.strip(), markdown.split("\n\n"))))

def block_to_block_type(markdown: str) -> BlockType:
    heading_pattern: str = r"^#{1,6} .*?$"
    code_pattern: str = r"^```\n.*?```$"
    quote_pattern: str = r"^> {0,1}.*?$"
    unordered_list_pattern: str = r"^(- .*?\n{0,1})+$"
    ordered_list_pattern: str = r"^\d+\. .*?$"


    if re.match(heading_pattern, markdown):
        return BlockType.HEADING

    if re.match(code_pattern, markdown):
        return BlockType.CODE

    if re.match(quote_pattern, markdown):
        return BlockType.QUOTE

    if re.match(unordered_list_pattern, markdown):
        return BlockType.UNORDERED_LIST
    # TODO: Find a way to make the ordered lists really be sequential and
    # starting from 1
    if re.match(ordered_list_pattern, markdown, re.MULTILINE):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

