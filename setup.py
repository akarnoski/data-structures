from setuptools import setup

setup(
    name="data-structures",
    description="Data structures.",
    authors="Adrienne Karnoski & Cody Dibble",
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
    package_dir={"": "data-structures"}
)
