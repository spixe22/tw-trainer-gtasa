from setuptools import setup, find_packages

setup(
    name='tw-trainer-gtasas',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "trainer_gtasa=src.main:main",
        ],
    },
)
