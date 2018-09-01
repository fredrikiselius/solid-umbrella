from setuptools import setup

def readme():
      with open('README.rst') as f:
            return f.read()

setup(name='solid-umbrella',
      version='0.1',
      description='Smart mirror program',
      url='https://github.com/fredrikiselius/solid-umbrella',
      author='Fredrik Iselius',
      author_email='fredrik.iselius@gmail.com',
      license='MIT',
      packages=['smartmirror'],
      install_requires=[
          'pygame',
          'pyowm'
      ],
      zip_safe=False)