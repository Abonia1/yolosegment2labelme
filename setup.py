from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Yolo segmentation prediction to labelme json'
LONG_DESCRIPTION = 'A package that allows generating JSON from YOLO prediction results, compatible with LabelMe/any labeling annotation tool'

# Setting up
setup(
    name="yolosegment2labelme",
    version=VERSION,
    author="Abonia Sojasingarayar",
    author_email="aboniaa@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url = 'https://github.com/Abonia1/yolosegment2labelme', 
    download_url = 'https://github.com/Abonia1/yolosegment2labelme/archive/refs/tags/v0.3.zip',  
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'pillow',
        'ultralytics'
    ],
    entry_points={
        'console_scripts': [
            'yolosegment2labelme = yolosegment2labelme.yolosegment2labelme:main'
        ]
    },
    keywords=['python', 'yolo', 'segmentation', 'json', 'labelme', 'anylabeling'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)