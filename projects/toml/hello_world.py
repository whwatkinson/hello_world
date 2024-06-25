from tomllib import load


def hello_world():
    with open("hello_world.toml", "rb") as f:
        data = load(f)
        print(data["Hello"])


if __name__ == "__main__":
    hello_world()
