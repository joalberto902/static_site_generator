from textnode import *#type: ignore

def main() -> int:
    text_node = TextNode("This is some anchor text", 
                         TextType.LINKS,
                         "https://www.boot.dev"
                         )
    print(text_node)
    return 0

if __name__ == "__main__":
    main()
