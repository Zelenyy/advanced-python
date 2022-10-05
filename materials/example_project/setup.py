from setuptools import setup, find_packages

setup(
    name="spc",
    version="3.1415.92653589793",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "secure-contain-project = spc.run:run_print"
        ],
        "gui_scripts": [
            "secure-contain-project-gui = sdp.run:run_print"
        ]
    }
)