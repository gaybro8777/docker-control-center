from setuptools import setup, find_packages

setup(
    name="docker_compose_control_center",
    use_describe_version=True,
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/usnistgov/docker-control-center",
    license="Public domain",
    author="Center for Nanoscale Science and Technology",
    author_email="CNSTapplications@nist.gov",
    description="Docker Compose Control Center is a small utility web application. It allows for control of docker containers, and specifically services created with docker-compose",
    long_description="Find out more about Docker Compose Control Center on the Github project page https://github.com/usnistgov/docker-control-center",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=[
        "docker==3.7.0",
        "django==2.1.8",
        "PyYAML==4.2b4",
        "docker-compose==1.24.0",
        "whitenoise==4.1.2",
        "requests==2.20.0",
        "ldap3==2.5.1",
        "pytz==2018.9",
        "python-dateutil==2.7.3",
        "djangorestframework==3.9.2"
    ],
)
