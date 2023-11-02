from setuptools import setup, find_packages

setup(
    name="Flask_AJ",
    version="0.0.1",
    description="ForestFire-main",
    author="abhishekjadhav3470",
    author_email="abhishekjadhav3470@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "numpy",
        "pandas",
        "scikit-learn",
    ],
)
