# -*- encoding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

# https://docs.python.org/3/distutils/setupscript.html
setup(
    name='mixit_365talents',
    version='0.1.0',
    license='None',
    description='',
    author=['Lionel Atty', ],
    author_email=['yoyonel@hotmail.com', ],
    url='https://github.com/yoyonel/mixit_365talents_1',
    packages=['mixit_365talents.{}'.format(x) for x in find_packages('src/mixit_365talents')],
    package_dir={'': 'src'},
    package_data={'': ['data/*.txt']},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[],
    install_requires=[
        "coloredlogs==10.0",
        "gensim==3.8.0",
        "pandas==0.25.0",
        "tqdm==4.33.0",
    ],
    extras_require={},
    entry_points={
        'console_scripts': [
            'starter_mixit = mixit_365talents.starter_mixit:main'
        ]
    },
    python_requires='>=3.6'
)
