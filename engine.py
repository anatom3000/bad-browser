from html.parser import HTMLParser
from pprint import pprint as pp

from reprlib import recursive_repr

def get(data, indexes):
    for i in indexes:
        data = data[i]
    return data

class Node:
    def __init__(self, tag, attrs={}, data=[]):
        self.tag = tag
        self.attrs = attrs
        self.data = data

        self.__name__ = self.__qualname__ = tag

    def add_data(self, data):
        self.data.append(data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    @recursive_repr()
    def __repr__(self):
        txt = f"<{self.tag}"
        for k, v in self.attrs.items():
            txt += f" {k}={repr(v)}"
        txt += '>' + '\n'
        for d in self.data:
            txt += "\n".join(map(lambda x: '\t'+x, repr(d).split("\n")))+'\n'
        txt += f"</{self.tag}>"
        return txt


class RootNode(Node):
    def __init__(self):
        super().__init__("internal")
    def add_data(self, data):
        pass

class HtmlCodeInterface(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_node_path = []
        self.document = []

    def handle_starttag(self, tag, attrs):
        node = self.document
        for i in self.current_node_path:
            node = node[i]
        node.add_data(Node(tag, dict(attrs)))
        self.current_node_path.append(0)

        #print(f"Found {tag}")


    def handle_endtag(self, tag):
        #print(f"Closing {tag}")
        self.current_node_path = self.current_node_path[:-1]
        tryself.current_node_path[-1] += 1

    def handle_data(self, data):
        #print(data)
        pass

test_page = """
<html>
    <head><title>Test Title</title></head>
    <body>
        <h1>I know, this a test !</h1>
    </body>
</html>
"""

test_parser = HtmlCodeInterface()
#test_parser.feed(test_page)
#print(repr(test_parser.document))

print(repr(
    Node('div', {"class": "testclass", "an":"other"}, [
        Node("a", {"href":"https://creepysite.com"}, ["dont go here"])
    ])
))