from setuptools import setup, find_packages

setup(
    name="legal_doc_extractor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'spacy',
        'scikit-learn',
    ],
    tests_require=[
        'unittest',
    ],
    include_package_data=True,
    zip_safe=False,
)
