from json import loads


def hello_world():
    with open("hello_world.json") as f:
        data = loads(f.read())
        print(data["Hello"])


if __name__ == "__main__":
    hello_world()
