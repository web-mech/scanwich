from setuptools import setup, find_packages
import os

setup(
    name="scanwich",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "psutil>=5.9.0",
        "openai>=1.0.0",
        "pygments>=2.15.0",
        "markdown>=3.5.0",
        "pywebview>=3.0.0",
    ],
    entry_points={
        'console_scripts': [
            'scanwich=scanwich.main:main',
        ],
    },
    author="PriceLove, LLC",
    author_email="hello@pricelove.co",
    description="An AI-powered system monitoring tool. Served fresh, packed with vulnerability findings.",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    keywords="system monitor, AI, process monitoring",
    python_requires=">=3.8",
)