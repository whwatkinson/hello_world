from bs4 import BeautifulSoup


def hello_world():
    with open("hello_world.html", 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    print(soup.title.text)


if __name__ == "__main__":
    hello_world()
