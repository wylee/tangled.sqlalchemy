from setuptools import setup, find_packages


setup(
    name='tangled.sqlalchemy',
    version='0.1.dev0',
    description='Tangled SQLAlchemy integration',
    packages=find_packages(),
    install_requires=(
        'tangled>=0.1.dev0',
        'SQLAlchemy',
    ),
    extras_require={
        'dev': (
            'tangled[dev]',
        ),
    },
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)