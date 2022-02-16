import setuptools

with open("README.md", "r") as fh:
        long_description= fh.read()
        setuptools.setup(
        name="pandas",
        version="1.1.0",
        author="Sample Project Author",
        author_email="author@sample.com",
        description="A sample python project",
        long_description=long_description,
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
    )