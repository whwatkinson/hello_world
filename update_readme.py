from os import listdir


def make_readme() -> None:

    my_name_map = {
        "abc": "ABC",
        "awk": "AWK",
        "bcpl": "BCPL",
        "coffeescript": "CoffeeScript",
        "cpp": "C++",
        "csharp": "C#",
        "dogescript": "DogeScript",
        "fsharp": "F#",
        "javascript": "JavaScript",
        "jq": "JQ",
        "livescript": "LiveScript",
        "python2": "Python 2",
        "python3": "Python 3",
        "typescript": "TypeScript",
        "vhdl": "VHDL",
    }

    project_list = sorted(
        [
            f"- {project.capitalize() if project not in my_name_map else my_name_map[project]}\n"
            for project in listdir("projects/")
            if project != "new"
        ]
    )

    welcome = (
        f"# Hello World in {len(project_list)} languages\n"
        "## Welcome\n"
        "[Inspired by this picture I saw on r/programmerhumor.]"
        "(https://www.reddit.com/r/ProgrammerHumor/comments/kl0v6m/me_in_an_interview_room/)\n"
        "![image info](./hello_world.png)\n\n"
    )

    projects = "".join(project_list)

    requirements = (
        "\n"
        "### Requirements\n"
        "- **docker**\n"
        "- **docker-compose**\n"
        "- **git**\n"
        "- **git lfs**\n"
    )

    build_me = (
        "\n"
        "###  To be greeted:\n"
        "```\n"
        "git clone https://github.com/whwatkinson/hello_world.git\n"
        "git lfs checkout\n"
        "docker-compose up --build\n"
        "```\n"
    )

    read_me = welcome + projects + requirements + build_me

    with open("README.md", "w") as file:
        file.write(read_me)


if __name__ == "__main__":
    make_readme()
