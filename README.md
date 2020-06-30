<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/find-python-packages.svg?maxAge=3600)](https://pypi.org/project/find-python-packages/)
[![](https://img.shields.io/npm/v/find-python-packages.svg?maxAge=3600)](https://www.npmjs.com/package/find-python-packages)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/find-python-packages/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/find-python-packages/actions)

### Installation
```bash
$ [sudo] pip install find-python-packages
```

```bash
$ [sudo] npm i -g find-python-packages
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>