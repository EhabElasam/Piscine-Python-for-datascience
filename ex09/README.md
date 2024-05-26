# ft_package

A sample test package for counting occurrences in a list.

## Installation

To install the package, follow these steps:

1. Upgrade the `build` package:
    ```sh
    python3 -m pip install --upgrade build
    ```

2. Build the package:
    ```sh
    python3 -m build
    ```

3. Install the built package:
    ```sh
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl
    ```

## Usage

To use the package, you can import it and call the `count_in_list` function:

```python
from ft_package import count_in_list

print(count_in_list(['toto', 'tata', 'toto'], 'toto'))  # Output: 2
print(count_in_list(['toto', 'tata', 'toto'], 'tutu'))  # Output: 0
```

## Uninstallation

To uninstall the package, use the following command:

```sh
pip uninstall ft-package
```

## Removing and Clean Up Build Artifacts:

```sh
rm -rf build dist ft_package.egg-info
```

## License

This project is licensed under the MIT License.


