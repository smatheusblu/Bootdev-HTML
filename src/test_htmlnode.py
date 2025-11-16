import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode('div', {'class': 'container', 'id': 'main'}, [])
        expected_html = '<div class="container" id="main"></div>'
        self.assertEqual(node.to_html(), expected_html)
