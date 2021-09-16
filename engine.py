from html.parser import HTMLParser
from pprint import pprint as pp

from reprlib import recursive_repr

class Node:
    def __init__(self, tag, attrs={}, data=[]):
        self.tag = tag
        self.attrs = attrs
        self.data = data

    def add_data(self, data):
        self.data.append(data)

    def __getitem__(self, index):
        if len(self.data) == 0:
            return self
        if len(index) == 1:
            print("wait what:", index)
            return self.data[index[0]]
        return self.data[index[0]][index[1:]]

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

class DataNode(Node):
    def __init__(self, data):
        super().__init__('', {}, [data])

    def __getitem__(self, i):
        return self

    def __repr__(self):
        return "".join(self.data)

class HtmlCodeInterface(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_node_path = [0]
        self.document = DataNode("")

    def handle_starttag(self, tag, attrs):
        if isinstance(self.document, DataNode):
            self.document = Node(tag, dict(attrs))
            return
        self.document[self.current_node_path].add_data(Node(tag, dict(attrs)))
        self.current_node_path.append(0)

        print(f"Found {tag}")


    def handle_endtag(self, tag):
        print(f"Closing {tag}")
        self.current_node_path = self.current_node_path[:-1]
        try:
            self.current_node_path[-1] += 1
        except IndexError:
            self.current_node_path.append(0)

    def handle_data(self, data):
        print(data.strip().strip())
        self.document[self.current_node_path].add_data(DataNode(data))

test_page = """
<html lang="en">
    <head><title>Test Title</title></head>
    <body>
        <h1>I know, this a test !</h1>
    </body>
</html>
"""
test_page = """
<html>
    <body>
        <h1>I know, this a test !</h1>
    </body>
</html>
"""


test_parser = HtmlCodeInterface()
test_parser.feed(test_page)
print(repr(test_parser.document))

"""print(repr(
    Node('div', {"class": "testclass", "an":"other"}, [
        Node("a", {"href":"https://creepysite.com"}, ["dont go here"])
    ])
))"""