import setuptools

setuptools.setup(
    name='pybtex-apa-style',
    version='0.1',
    author='Chris Proctor',
    author_email='chris@chrisproctor.net',
    description='Pybtex APA7 style',
    url='https://github.com/naeka/pybtex-apa-style',
    py_modules=['formatting.apa', 'labels.apa', 'names.firstlast'],
    entry_points={
        'pybtex.style.formatting': 'apa7 = formatting.apa:APAStyle',
        'pybtex.style.labels': 'apa7 = labels.apa:LabelStyle',
        'pybtex.style.names': 'firstlast = names.firstlast:NameStyle',
    },
    classifiers=(
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Markup',
        'Topic :: Utilities',
    ),
)
