import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cv_io", 
    version="1.0.0",
    author="Saeid Hosseinipoor",
    author_email="shossei1@stevens.edu",
    description="A collection of I/O scripts for computer vision formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saeid-h/Computer-Vision-IO.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

# python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/*
