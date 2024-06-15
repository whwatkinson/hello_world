from io import StringIO
from os import listdir

from scripts import my_names_map, skips, get_project_root


def format_project_name(project: str) -> str:
    """
    Format the project name to be more human-readable
    :param project: The name of the project
    :return: The correctly formatted project name
    """
    if project not in my_names_map:
        return project.capitalize()
    return my_names_map[project]


def make_readme() -> None:
    """
    Create the README.md file dynamically from the projects in the projects directory
    :return: None
    """

    readme_buffer = StringIO()

    languages_project_list = sorted(
        [
            f"- [{format_project_name(project)}](./projects/{project})\n"
            for project in listdir(f"{get_project_root()}/projects/")
            if project not in skips
        ]
    )

    linux_commands_list = sorted(
        [
            f"- [{format_project_name(project)}](./projects/linux_commands/{project})\n"
            for project in listdir(f"{get_project_root()}/projects/linux_commands/")
            if project not in skips
        ]
    )

    welcome = (
        f"# Hello World in {len(languages_project_list)} languages and {len(linux_commands_list)} Linux Commands\n\n"
        "## Welcome\n\n"
        "[Inspired by this picture I saw on r/programmerhumor.]"
        "(https://www.reddit.com/r/ProgrammerHumor/comments/kl0v6m/me_in_an_interview_room/)\n\n"
        "![image info](./hello_world.png)\n\n"
        "## Programming Languages\n"
    )
    readme_buffer.write(welcome)

    languages_projects_joined = "".join(languages_project_list)
    readme_buffer.write(languages_projects_joined)

    readme_buffer.write("## Linux Commands\n")
    linux_commands_projects_joined = "".join(linux_commands_list)
    readme_buffer.write(linux_commands_projects_joined)

    # TODO markup langs
    # API's?

    requirements = (
        "\n"
        "## Requirements\n"
        "- **docker**\n"
        "- **docker-compose**\n"
        "- **git**\n"
        "- **git lfs**\n"
    )
    readme_buffer.write(requirements)

    build_me = (
        "\n"
        "## To be greeted:\n"
        "```\n"
        "git clone https://github.com/whwatkinson/hello_world.git\n"
        "git lfs checkout\n"
        "docker-compose up --build\n"
        "```\n"
    )
    readme_buffer.write(build_me)

    with open(f"{get_project_root()}/README.md", "w") as file:
        file.write(readme_buffer.getvalue())


if __name__ == "__main__":
    make_readme()
