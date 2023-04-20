import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dash_component_editor",                     # This is the name of the package
    version="0.0.6",                        # The release version
    author="Zhuowen (Kevin) Zhao, Ronald Pandolfi",                     # Full name of the author
    author_email='zwenzhao11@gmail.com',
    description="",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    license_files = ('LICENSE.txt',),                                     # Information to filter the project on PyPi website
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Dash',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],\
    project_urls={
        'Source': 'https://github.com/mlexchange/mlex_dash_component_editor.git'
    },
    python_requires='>=3.0',                # Minimum version requirement of the package
    py_modules=["dash_component_editor"],             # Name of the python package
    package_dir={'':'src'},     # Directory of the source code of the package
    install_requires=['dash>=2.9.0',
                      'dash_bootstrap_components>=1.0.0',
                      'dash_daq>=0.1.0',
                    ]                     # Install other dependencies if any
)
