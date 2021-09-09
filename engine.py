from html.parser import HTMLParser

def get(data, indexes):
    for i in indexes:
        data = data[i]
    return data

class HtmlNode:
    def __init__(self, tag, attrs={}, data=[]):
        self.tag = tag
        self.attrs = attrs
        self.data = data

    def add_data(self, data):
        self.data.append(data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        txt = f"<{self.tag}"
        print(txt)
        for k, v in self.attrs.items():
            txt += f" {k}={repr(v)}"
            print(txt)
        txt += '>' + '\n'
        print(txt)
        for d in self.data:
            txt += '\t'+repr(d)+'\n'
            print(txt)
        txt += f"</{self.tag}>"
        print(txt)
        return txt

class HtmlCodeInterface(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_node_path = []
        self.document = HtmlNode("html")

    def handle_starttag(self, tag, attrs):
        node = self.document
        for i in self.current_node_path:
            print(f"n={node}")
            print(f"ni={node[i]}")
            node = node[i]
        node.add_data(HtmlNode(tag, dict(attrs)))
        print(repr(self.document))


    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
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

print(repr(HtmlNode('div', {"class": "testclass", "an":"other"}, ["test essay"])))