from os import listdir
from re import compile

from scripts import skips, get_project_root

IMAGE_PATTERN = compile(r"FROM\s(?P<image_name>[\w:\d\.\/\-]+)")


# https://pypi.org/project/docker/


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
    checked = 0
    eso_langs_count = 0

    for project in projects:
        # Get Dockerfile name dynamically
        dockerfile_name = [
            file_name
            for file_name in listdir(f"{get_project_root()}/projects/{project}")
            if "Dockerfile" in file_name
        ]

        # Open Dockerfile
        with open(
            f"{get_project_root()}/projects/{project}/{dockerfile_name[0]}", "r"
        ) as file:
            # Get image counts
            if docker_image := IMAGE_PATTERN.findall(file.read())[0]:
                if 'esolang' in docker_image:
                    eso_langs_count += 1
                if docker_image in docker_images:
                    docker_images[docker_image] += 1
                else:
                    docker_images[docker_image] = 1
                checked += 1
            else:
                raise Exception(f"No match found for {project}")

    if checked != len(projects):
        raise Exception("Not all projects checked")

    # Sort by count then image name
    docker_images_sorted = dict(
        sorted(docker_images.items(), key=lambda item: (item[1], item[0]), reverse=True)
    )

    display_results(docker_images_sorted, eso_langs_count)


def display_results(docker_images_sorted: dict, eso_langs_count: int) -> None:

    print("\nIdeally each project should use the ubuntu:20.04 base image...\n")
    print(f"Number of different images: \t{len(docker_images_sorted.keys())}")
    print(f"Esolangs count: \t\t\t\t{eso_langs_count}\n")
    print("Count\tDocker Image")
    for image, count in docker_images_sorted.items():
        print(f"{count} \t\t{image}")


if __name__ == "__main__":
    display_docker_images()
