import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        self.assertEqual(node, node2)

    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://www.example.com)")

    def test_eq_with_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.example.com/2")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node 2", TextType.BOLD, "https://www.example.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.example.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type_and_text(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node 2", TextType.ITALIC, "https://www.example.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type_and_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.example.com/2")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_and_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node 2", TextType.BOLD, "https://www.example.com/2")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type_and_text_and_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node 2", TextType.ITALIC, "https://www.example.com/2")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_url_and_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
