import setuptools

setuptools.setup(
    name="UpKit",
    version="1.1",
    author="Unknown",
    description="A simple Telegram Bot written in Python to save files to Telegram",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ReverSEcodeMod/UpKit",
    project_urls={
        "Bug Tracker": "https://github.com/ReverSEcodeMod/UpKit/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable"
    ],
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt', 'r', encoding='utf-8').read().split('\n'),
    scripts=['start.sh'],
    python_requires=">=3.8",
)
