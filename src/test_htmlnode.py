import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, None, None)")

    def test_eq_with_children(self):
        node = HTMLNode("div", children=[HTMLNode("p", "This is a paragraph")])
        node2 = HTMLNode("div", children=[HTMLNode("p", "This is a paragraph")])
        self.assertEqual(node, node2)

    def test_repr_with_children(self):
        node = HTMLNode("div", children=[HTMLNode("p", "This is a paragraph")])
        self.assertEqual(repr(node), "HTMLNode(div, None, [HTMLNode(p, This is a paragraph, None, None)], None)")

    def test_eq_with_props(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "paragraph"})
        node2 = HTMLNode("p", "This is a paragraph", props={"class": "paragraph"})
        self.assertEqual(node, node2)
        self.assertEqual(node.props_to_html(), 'class="paragraph"')

    def test_props_to_html_with_props(self):
        node = HTMLNode("p", "This is a paragraph", props={"href": "http://example.com", "src": "http://example.com"})
        self.assertEqual(node.props_to_html(), 'href="http://example.com" src="http://example.com"')
