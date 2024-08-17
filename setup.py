from setuptools import setup


def parse_requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    requires = []

    for line in lines:
        if "http" in line:
            pkg_name_with_version = line.split("/")[-1].split("-")[0]
            requires.append(pkg_name_with_version)
        else:
            requires.append(line)

    return requires


requires = parse_requirements("requirements.txt")

setup(
    name="neu_scraper",
    version="0.1",
    install_requires=requires,
    python_requires=">=3.9.7",
    zip_safe=False,
)