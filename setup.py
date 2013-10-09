import os
from distutils.core import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="sy_template",
    version="0.1",
    author="",
    author_email="",
    description="sy_template, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="geonode django",
    url='https://github.com/simod/sy_template',
    packages=['sy_template'],
    install_requires=[
        "geonode==2.0b63",
        "psycopg2",
        "geonode_formhub>=0.1"
    ],
    dependency_links = [
        "https://github.com/simod/geonode_formhub/archive/no-project.zip#egg=geonode_formhub-0.1"
    ],
    include_package_data=True,
    zip_safe=False,
)
