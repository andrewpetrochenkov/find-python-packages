<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/find-python-packages.svg?maxAge=3600)](https://pypi.org/project/find-python-packages/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/find-python-packages.svg?branch=master)](https://travis-ci.org/andrewp-as-is/find-python-packages/)

#### Installation
```bash
$ [sudo] pip install find-python-packages
```

#### Scripts usage
command|`usage`
-|-
`find-python-packages` |`usage: find-python-packages path`

#### Examples
```
apps/__init__.py
apps/app1/__init__.py
apps/app2/__init__.py
settings/__init__.py
```

```bash
$ find-python-packages . | grep apps
apps
apps.app1
apps.app2
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>