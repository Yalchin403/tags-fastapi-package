from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.strip() for line in lines if not line.startswith("#")]


setup(
    name="core_api",
    version="0.0.1",
    author="Yalchin Mammadli",
    author_email="yalchinmammadli@outlook.com",
    description="This core API provides TAGS API with CRUD functionality",
    packages=find_packages(),
    install_requires=parse_requirements("requirements/requirements.txt"),
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.11.0",
)
