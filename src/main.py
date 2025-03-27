from textnode import TextNode, TextType
from leafnode import LeafNode


def main():
    text_node = TextNode("Hello, world!", TextType.BOLD , "https://www.example.com")
    print(text_node)


def text_node_to_html_node(text_node: TextNode):
    if text_node is None or text_node.text_type not in TextType:
        raise Exception("Invalid TextNode")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.NORMAL:
            return LeafNode("p", text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})


if __name__ == "__main__":
    main()



