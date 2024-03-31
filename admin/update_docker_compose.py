from io import StringIO
from os import listdir
from admin import skips, get_project_root


def make_docker_compose():
    docker_compose_buffer = StringIO()
    head = (
        '# As noted in the Docker best practices "each container should have only one concern"\n'
        "\n"
        'version: "3.9"\n'
        "\n"
        "services:\n\n"
    )

    docker_compose_buffer.write(head)

    project_compose_list = sorted(
        [
            (
                f"  {project}:\n"
                f"    container_name: hello_world_{project}\n"
                "    build:\n"
                f"      context: projects/{project}\n"
                f"      dockerfile: Dockerfile{project.capitalize()}\n\n"
            )
            for project in listdir(f"{get_project_root()}/projects/")
            if project not in skips
        ]
    )

    project_compose = "".join(project_compose_list)
    docker_compose_buffer.write(project_compose)

    with open(f"{get_project_root()}/docker-compose.yml", "w") as file:
        file.write(docker_compose_buffer.getvalue())


if __name__ == "__main__":
    make_docker_compose()
