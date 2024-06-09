from os import listdir
from re import compile

from scripts import skips, get_project_root

IMAGE_PATTERN = compile(r"FROM\s(?P<image_name>[\w:\d\.\/\-]+)")


def display_docker_images() -> None:
    """
    Display the docker images counts used in the projects
    :return: None
    """
    projects = [
        project
        for project in listdir(f"{get_project_root()}/projects/")
        if project not in skips
    ]
    docker_images = dict()
    for project in projects:
        dockerfile_name = [
            file_name
            for file_name in listdir(f"{get_project_root()}/projects/{project}")
            if "Docker" in file_name
        ]
        with open(
            f"{get_project_root()}/projects/{project}/{dockerfile_name[0]}", "r"
        ) as file:
            if docker_image := IMAGE_PATTERN.findall(file.read())[0]:
                if docker_image in docker_images:
                    docker_images[docker_image] += 1
                else:
                    docker_images[docker_image] = 1
            else:
                raise Exception(f"No match found for {project}")

    docker_images_sorted = dict(
        sorted(docker_images.items(), key=lambda item: item[1], reverse=True)
    )

    print("Count\tDocker Image")
    for image, count in docker_images_sorted.items():
        print(f"{count} \t\t{image}")


if __name__ == "__main__":
    display_docker_images()
