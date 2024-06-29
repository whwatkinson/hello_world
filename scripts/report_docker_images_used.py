from os import listdir
from re import compile

from scripts import skips, get_project_root

IMAGE_PATTERN = compile(r"FROM\s(?P<image_name>[\w:\d\.\/\-]+)")
GOAL_BASE_IMAGE = "ubuntu:22.04"
DISPLAY_ESO_LANGS = False

# https://pypi.org/project/docker/


def display_docker_images(display_eso_langs: bool = True) -> None:
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
    projects_checked = 0
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
            docker_image = IMAGE_PATTERN.findall(file.read())[0]
            projects_checked += 1

            if not docker_image:
                raise Exception(f"Image not found in {project}")

            if "esolang" in docker_image:
                eso_langs_count += 1
                if not display_eso_langs:
                    continue

            if docker_image in docker_images:
                docker_images[docker_image] += 1
            else:
                docker_images[docker_image] = 1

    if projects_checked != len(projects):
        raise Exception("Not all projects checked")

    # Sort by count then image name
    docker_images_sorted = dict(
        sorted(docker_images.items(), key=lambda item: (item[1], item[0]), reverse=True)
    )

    display_results(
        docker_images_sorted, eso_langs_count, projects_checked, display_eso_langs
    )


def display_results(
    docker_images_sorted: dict,
    eso_langs_count: int,
    total_projects: int,
    display_eso_langs: bool,
) -> None:

    print(
        f"\nIdeally for each project we should use the {GOAL_BASE_IMAGE} base image...\n"
    )
    print(
        f"Number of different images: \t{len(docker_images_sorted.keys()) + eso_langs_count}"
    )
    if display_eso_langs:
        print(f"Esolangs count: \t\t\t\t{eso_langs_count}")
    print(
        f"Percent towards goal: \t\t\t{(docker_images_sorted[GOAL_BASE_IMAGE] / total_projects) * 100:.1f}%\n"
    )
    print("Count\t\tDocker Image")

    # Inelegant way to display the results...
    docker_images_sorted_list = list(docker_images_sorted.items())
    print(f"{docker_images_sorted_list[0][1]} \t\t{docker_images_sorted_list[0][0]}")
    for image, count in docker_images_sorted_list[1:]:
        print(f"{count} \t\t\t{image}")


if __name__ == "__main__":
    display_docker_images(display_eso_langs=True)
