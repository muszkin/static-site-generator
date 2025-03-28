from textnode import TextNode, TextType, TextTypeMarkdown
from leafnode import LeafNode
import re

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


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if TextTypeMarkdown(delimiter).name != text_type.name:
        raise Exception(f"Invalid delimiter \"{delimiter}\" for text type \"{text_type}\"")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            nodes = node.text.split(delimiter)
            new_nodes.append(TextNode(nodes[0], TextType.TEXT))
            for i in range(1, len(nodes), 2):
                new_nodes.append(TextNode(nodes[i], text_type))
                new_nodes.append(TextNode(nodes[i+1], TextType.TEXT))
    return new_nodes


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    links = []
    for match in matches:
        links.append((match[0], match[1]))
    return links


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    images = []
    for match in matches:
        images.append((match[0], match[1]))
    return images


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(images) == 0:
                new_nodes.append(node)
            else:
                for image in images:
                    nodes = node.text.split("![" + image[0] + "](" + image[1] + ")", 1)
                    new_nodes.append(TextNode(nodes[0], TextType.TEXT))
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                    if len(nodes[1]) > 0:
                        new_nodes.append(TextNode(nodes[1], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(links) == 0:
                new_nodes.append(node)
            else:
                for link in links:
                    nodes = node.text.split("[" + link[0] + "](" + link[1] + ")", 1)
                    new_nodes.append(TextNode(nodes[0], TextType.TEXT))
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                    if len(nodes[1]) > 0:
                        new_nodes.append(TextNode(nodes[1], TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, TextTypeMarkdown.BOLD.value, TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, TextTypeMarkdown.ITALIC.value, TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, TextTypeMarkdown.CODE.value, TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def markdown_to_blocks(markdown):
    split_text = markdown.split("\n\n")
    blocks = []
    for text in split_text:
        stripped = text.strip()
        if len(stripped) == 0:
            continue
        blocks.append(stripped)
    return blocks


if __name__ == "__main__":
    main()



