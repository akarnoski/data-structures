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
        'hash_table',
        'linked_list',
        'priorityq',
        'que_',
        'stack',
        'trie_tree',
        'bubble_sort',
        'insertion_sort',
        'merge_sort',
        'quick_sort',
        'radix_sort'
        ],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    package_dir={"": "src"}
)
