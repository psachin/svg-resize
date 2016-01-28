# setup.py for svg-resize
from setuptools import setup


setup(name='svg-resize',
      version='1.0',
      description='Resizes and frames an SVG image',
      long_description=open('README.md').read(),
      author='Ilya Zverev',
      author_email='ilya@zverev.info',
      maintainer='Zverik',
      maintainer_email='ilya@zverev.info',
      url='https://github.com/Zverik/svg-resize',
      license='WTFPL',
      package_dir={'svgresize': 'src'},
      packages=['svgresize'],
      install_requires=['lxml'],
      entry_points={
          'console_scripts': [
              'svg-resize=svgresize:main',
          ],
      },
      zip_safe=False,
      keywords='svg resize image manipulation',
      platforms=['Linux', 'OSX'],
      classifiers=[
          'Intended Audience :: End Users',
          'Topic :: Image Manipulation :: Build Tools',
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: Implementation :: PyPy",
      ]
)
