from enum import Enum

class TextType(Enum):
    """An Enum for the types of types int the markdown files
    
    TextType is one of:
    --plain text
    --bold text
    --italic text
    --code text
    --links
    --embeded/images
    """
    PLAIN_TEXT = "plain text"
    BOLD_TEXT = "**bold text**"
    ITALIC_TEXT = "_italic text_"
    CODE_TEXT = "`code text`"
    LINKS = "[anchor](link)"
    IMAGES = "![description](image)"


class TextNode:
    """Represents a node in mardown text file
    
    Attributes:
        text: represents the text content of the node without formatting
        text_type: represents the text formatting of the text by TextType
        url: if it is a TextType with url, than url represents it, otherwise is None
    """
    def __init__(
        self, text: str, text_type: TextType, url: str | None = None
    ) -> None:
        """Initializes an instance of TextNode class:

        param:
            text:str
            text: TextType
            url(opt): str| None

        returns None
        """
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | None = url
    def __eq__(self, other: object , /) -> bool:
        """__eq__ function for the TextNode class

        param:
            other: TextNode
        """
        if not isinstance(other, TextNode):
            raise ValueError(f"{type(other)} cannot be compared to TextNode object")

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        """__repr__ for the TextNode class
        """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"










    
