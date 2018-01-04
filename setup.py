from setuptools import setup, find_packages

#bring in __version__ from sourcecode
#per https://stackoverflow.com/a/17626524
#and https://stackoverflow.com/a/2073599

with open('lineman/version.py') as ver:
    exec(ver.read())

setup(name='lineman',
      version=__version__,
      description='Lineman fixes data problems that will keep your data from going into redcap.',
      url='http://github.com/ctsit/lineman',
      author='Patrick White',
      author_email='pfwhite9@gmail.com',
      license='Apache License 2.0',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'lineman = lineman.__main__:cli_run',
          ],
      },
      install_requires=['cappy', 'docopt', 'pyyaml', 'python-dateutil'],
      zip_safe=False)
