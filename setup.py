from setuptools import setup,find_packages

hyphen="-e ."
def Requirements(filename):
    with open("requirements.txt","r") as f:
        req=f.readlines()
        req=[i.replace("\n","") for i in req]
        if hyphen in req:
            req.remove(hyphen)
    return req


setup(
    name="Patato-disease-classification-deep-learning-project",
    author="Gajender",
    version="0.1",
    author_email="iamsanju0707@gmail.com",
    description="Patato-disease-classification-deep-learning-project ",
    packages=find_packages(),
    install_requires=Requirements("requirements.txt")
)
