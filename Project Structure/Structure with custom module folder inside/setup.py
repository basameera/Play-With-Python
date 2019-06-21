from setuptools import setup
# from setuptools import setup, find_packages
# https://python-packaging.readthedocs.io/en/latest/index.html
'''
1. Install custom package

`pip install .` - install the package locally (for use on our system)

2. Test by `import custom_package`
3. Uninstall script
'''

# Create proper setup to be used by pip
setup(name='SkunkWork',
      version='0.0.1',
      description='Neural Network Trainer Package for Pytorch.',
      author='basameera',
      packages=['SkunkWork']
      )


# setup(
#     name="SkunkWork",
#     version="0.0.1",
#     description="Neural Network Trainer Package for Pytorch",
#     url="https://github.com/basameera/Play-With-Python/tree/master/Project%20Structure/Structure%20with%20custom%20module%20folder%20inside",
#     author="Sameera Sandaruwan @bassandaruwan",
#     author_email="basameera@pm.me",
#     packages=["SkunkWork"],
# )
