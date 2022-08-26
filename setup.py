from setuptools import setup

setup(
    name='textra',
    version='0.4',
    description='Machine translation for Everyone',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GitHub30/textra',
    project_urls={ 'Bug Tracker': 'https://github.com/GitHub30/textra/issues' },
    author='TexTra',
    author_email='funaox@gmail.com',
    platforms="any",
    license='MIT',
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="TexTra translation python",
    install_requires=['requests', 'requests-oauthlib'],
    py_modules=['textra'],
    entry_points={
        'console_scripts': [
            'trans = textra:trans'
        ]
    }
)

# Publish commands
# https://packaging.python.org/tutorials/packaging-projects/
#pip install --upgrade pip build twine
#python3 -m build
#python3 -m twine upload dist/*
