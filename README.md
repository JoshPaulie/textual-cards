# textual-cards

<!-- [![PyPI - Version](https://img.shields.io/pypi/v/textual-cards.svg)](https://pypi.org/project/textual-cards)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textual-cards.svg)](https://pypi.org/project/textual-cards) -->
[![Made With Textual](https://img.shields.io/badge/Made%20With%20Textual%20♥️-2c292d.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIEFkb2JlIElsbHVzdHJhdG9yIDI0LjIuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzJfMV8iIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHdpZHRoPSI0NTYuNHB4IiBoZWlnaHQ9IjQ1Ny44cHgiIHZpZXdCb3g9IjAgMCA0NTYuNCA0NTcuOCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNDU2LjQgNDU3Ljg7IiB4bWw6c3BhY2U9InByZXNlcnZlIgoJPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgoJLnN0MHtmaWxsOnVybCgjU1ZHSURfMV8pO30KCS5zdDF7ZmlsbDp1cmwoI1NWR0lEXzJfKTt9Cgkuc3Qye2ZpbGw6dXJsKCNTVkdJRF8zXyk7fQo8L3N0eWxlPgo8Zz4KCQoJCTxsaW5lYXJHcmFkaWVudCBpZD0iU1ZHSURfMV8iIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iNjM5LjgyIiB5MT0iNTg3LjkxIiB4Mj0iNzI0Ljg1IiB5Mj0iNTg3LjkxIiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KDYuMTIzMjM0ZS0xNyAxIDEgLTYuMTIzMjM0ZS0xNyAtNDMwLjY1IC01MDUuNTEpIj4KCQk8c3RvcCAgb2Zmc2V0PSIwIiBzdHlsZT0ic3RvcC1jb2xvcjojRjE4RjM0Ii8+CgkJPHN0b3AgIG9mZnNldD0iMC42MSIgc3R5bGU9InN0b3AtY29sb3I6I0U5NUYzMiIvPgoJCTxzdG9wICBvZmZzZXQ9IjEiIHN0eWxlPSJzdG9wLWNvbG9yOiNFMzMxMkQiLz4KCTwvbGluZWFyR3JhZGllbnQ+Cgk8cGF0aCBjbGFzcz0ic3QwIiBkPSJNMTU0LjYsMjE5LjNsLTYwLjEtODVoNDIuNGMxNC40LDAsMjcuOCw2LjcsMzUuNywxNy44bDQ3LjUsNjcuMkgxNTQuNnoiLz4KCQoJCTxsaW5lYXJHcmFkaWVudCBpZD0iU1ZHSURfMl8iIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iODA5LjQ5IiB5MT0iOTY2LjI1IiB4Mj0iNzI0Ljg1IiB5Mj0iOTY2LjI1IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KDAgMSAtMSAwIDExMjMuNTEgLTUwNS41MSkiPgoJCTxzdG9wICBvZmZzZXQ9IjAiIHN0eWxlPSJzdG9wLWNvbG9yOiNGRkVGMjYiLz4KCQk8c3RvcCAgb2Zmc2V0PSIyLjAwMDAwMGUtMDIiIHN0eWxlPSJzdG9wLWNvbG9yOiNGRkVBMjEiLz4KCQk8c3RvcCAgb2Zmc2V0PSIwLjE0IiBzdHlsZT0ic3RvcC1jb2xvcjojRkVENzBGIi8+CgkJPHN0b3AgIG9mZnNldD0iMC4yNSIgc3R5bGU9InN0b3AtY29sb3I6I0ZEQ0MwNCIvPgoJCTxzdG9wICBvZmZzZXQ9IjAuMzgiIHN0eWxlPSJzdG9wLWNvbG9yOiNGREM4MDAiLz4KCQk8c3RvcCAgb2Zmc2V0PSIxIiBzdHlsZT0ic3RvcC1jb2xvcjojRjE4RjM0Ii8+Cgk8L2xpbmVhckdyYWRpZW50PgoJPHBhdGggY2xhc3M9InN0MSIgZD0iTTE3NS40LDI4Mi4xbDQ0LjYtNjIuOGgtNjUuNEw5NC41LDMwNGgzNy4xQzE0OS4zLDMwNCwxNjUuOCwyOTUuOCwxNzUuNCwyODIuMXoiLz4KCQoJCTxsaW5lYXJHcmFkaWVudCBpZD0iU1ZHSURfM18iIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMjA4LjI3IiB5MT0iMTY3LjE3IiB4Mj0iMzUwLjMyIiB5Mj0iMTY3LjE3IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KDEgMCAwIC0xIDExLjU5IDQ4MS4wMykiPgoJCTxzdG9wICBvZmZzZXQ9IjAiIHN0eWxlPSJzdG9wLWNvbG9yOiNGRkVGMjYiLz4KCQk8c3RvcCAgb2Zmc2V0PSIyLjAwMDAwMGUtMDIiIHN0eWxlPSJzdG9wLWNvbG9yOiNGRkVBMjEiLz4KCQk8c3RvcCAgb2Zmc2V0PSIwLjE0IiBzdHlsZT0ic3RvcC1jb2xvcjojRkVENzBGIi8+CgkJPHN0b3AgIG9mZnNldD0iMC4yNSIgc3R5bGU9InN0b3AtY29sb3I6I0ZEQ0MwNCIvPgoJCTxzdG9wICBvZmZzZXQ9IjAuMzgiIHN0eWxlPSJzdG9wLWNvbG9yOiNGREM4MDAiLz4KCQk8c3RvcCAgb2Zmc2V0PSIxIiBzdHlsZT0ic3RvcC1jb2xvcjojRjE4RjM0Ii8+Cgk8L2xpbmVhckdyYWRpZW50PgoJPHJlY3QgeD0iMjE5LjkiIHk9IjMwNC4yIiBjbGFzcz0ic3QyIiB3aWR0aD0iMTQyLjEiIGhlaWdodD0iMTkuMyIvPgo8L2c+Cjwvc3ZnPgo=)](https://github.com/Textualize/textual)

**Table of Contents**

- [textual-cards](#textual-cards)
  - [Installation](#installation)
    - [`pipx`](#pipx)
    - [Manual](#manual)
  - [License](#license)

## Installation

This is not a published package.

### `pipx`
> After publishing, this will be the preferred method
```console
pipx install <TBD>
```

### Manual
> If you, for whatever reason, want to use it *now*, follow these steps
```console
git clone https://github.com/joshpaulie/textual-cards
cd textual-cards
python -m venv .venv
<activate venv>
python -m pip -e install .
python -m textual_cards
```

## License
`textual-cards` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
