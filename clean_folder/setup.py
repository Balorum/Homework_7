from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="3",
    description="Code that cleans up your folder and sorts your files into folders",
    url="https://github.com/Balorum/Homework_6",
    license="No license",
    author="Balorum",
    author_email="remeshevskyi.nikita03@gmail.com",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["clean-folder = clean_folder.clean:run"]},
)
