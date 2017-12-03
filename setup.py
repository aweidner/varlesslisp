from setuptools import setup, find_packages

setup(
    name="varlesslisp",
    description="A simple lisp interpreter with no variable bindings",
    author="Adam Weidner",
    packages=find_packages(exclude=["tests"])
)
