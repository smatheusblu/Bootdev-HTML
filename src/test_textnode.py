import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a link", TextType.LINK)
        node2 = TextNode("This is a link", TextType.LINK, url=None)
        self.assertEqual(node, node2)

    def test_different_url(self):
        node = TextNode("This is a link", TextType.LINK, url="https://example.com")
        node2 = TextNode("This is a link", TextType.LINK, url="https://different.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Sample text", TextType.ITALIC, url="https://example.com")
        expected_repr = "TextNode(text='Sample text', text_type=TextType.ITALIC, url='https://example.com')"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
