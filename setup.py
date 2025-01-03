import setuptools

setuptools.setup(
    name="pybtex-apa7-style",
    version="0.1.3",
    description="Provides APA7 style for Pybtex",
    packages=["formatting", "labels", "names"],
    python_requires=">=3.9",
    install_requires=[
        "pybtex>=0.24.0",
    ],
    entry_points={
        "pybtex.style.formatting": [
            "apa7 = formatting.apa:APAStyle",
        ],
        "pybtex.style.labels": [
            "apa7 = labels.apa:LabelStyle",
        ],
        "pybtex.style.names": [
            "firstlast = names.firstlast:NameStyle",
        ],
    },
)
