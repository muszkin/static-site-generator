import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph")
        node2 = LeafNode("p", "This is a paragraph")
        self.assertEqual(node, node2)
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_repr(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(repr(node), "LeafNode(p, This is a paragraph, None)")

    def test_a_href(self):
        node = LeafNode("a", "Click here", {"href": "http://example.com"})
        self.assertEqual(node.to_html(), '<a href="http://example.com">Click here</a>')