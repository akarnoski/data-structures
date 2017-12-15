from setuptools import setup

setup(
    name="data-structures",
    version='0.0',
    description="Data structures.",
    author="Adrienne Karnoski & Cody Dibble",
    author_email="adrienne.j.karnoski@gmail.com",
    py_modules=[
        'binheadp',
        'bst',
        'deque',
        'doubly_linked_list',
        'graph',
        'linked_list',
        'priorityq',
        'que_',
        'stack',
        ],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    package_dir={"": "src"}
)
