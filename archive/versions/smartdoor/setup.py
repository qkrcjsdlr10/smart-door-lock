from setuptools import setup

with open('README.md', 'r', encoding="utf-8") as f:
    readme = f.read()
with open("requirement.txt", 'r', encoding="utf-8") as f:
    requires = f.read().splitlines()
with open("test_requirement.txt", 'r', encoding="utf-8") as f:
    test_requires = f.read().splitlines()

setup(
   name='foo',
   version='2.0',
   description='Something different',
   packages=['foo'],  # would be the same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages acting as dependencies
)
