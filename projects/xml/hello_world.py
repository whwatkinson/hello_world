from xml.etree.ElementTree import parse


def hello_world():
    tree = parse('hello_world.xml')
    root = tree.getroot()
    print(root.text)


if __name__ == "__main__":
    hello_world()
