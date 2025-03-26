from textnode import TextNode, TextType

def main():
    text_node = TextNode("Hello, world!", TextType.BOLD_TEXT , "https://www.example.com")
    print(text_node)

if __name__ == "__main__":
    main()



