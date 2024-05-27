from setuptools import setup, find_packages


def main():
    """
    Main function to handle the setup of the package.
    """
    setup(
        name='ft_package',
        version='0.0.1',
        packages=find_packages(),
        license='MIT',
        description='A sample test package',
        author='eelasam',
        author_email='eelasam@student.42vienna.com',
        url='https://github.com/EhabElasam/Python-for-datascience/ft_package',
    )


if __name__ == "__main__":
    main()
