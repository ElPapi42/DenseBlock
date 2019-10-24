import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="denseblock",
	version="1.0",
	author="Whitman Bohorquez",
	author_email="whitman-2@hotmail.com",
	description="Keras Extended Dense Layer",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ElPapi42/DenseBlock-KerasPlugNPlay",
	packages=setuptools.find_packages(),
	install_requires=[
		"tensorflow-gpu"
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)