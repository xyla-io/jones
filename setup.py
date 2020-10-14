from setuptools import setup, find_packages

setup(name='jones',
      version='0.0.1',
      description='Xyla\'s Python Fixer API client.',
      url='https://github.com/xyla-io/jones',
      author='Gregory Klein',
      author_email='gklei89@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'pandas',
        'requests',
        'furl',
      ],
      zip_safe=False)
