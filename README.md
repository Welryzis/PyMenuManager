# PyMenuManager
**PyMenuManager** - is a simple Python package for creating and managing console menus. Its provides easy-to-use interface for developers.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Notice](#notice)
- [Disclaimer](#disclaimer)
- [Contacts](#contacts)


## Installation
Requirements: `Python >= 3.5`

Note: For Linux use `python3` and `pip3`

```bash
pip install git+https://github.com/Welryzis/PyMenuManager.git
```


## Usage
```python
from MenuManager import Menu  # Imports
from MenuManager.exceptions import MenuError


def add(x, y):  # First instance with args
    print("Added", x, y)


def remove(pk: int = 0):  # Second instance with kwargs
    print("Removed", pk)
    return "returned: removed"


try:
    # Menu object initialization
    menu = Menu("Test Menu", "Test description for menu.")

    # Creating menu option
    menu.add_option("Add", add, 1, 2)
    menu.add_option("Remove", remove, pk=3)
    menu.add_option("Quit", quit)

    # Show menu and print instance result
    result = menu.show()
    print("Result:", result)
except MenuError:  # Exception handler
    print("Menu error.")
```

![screen_1](Files/screen_1.png)
![screen_2](Files/screen_2.png)


## Features
- Easy-to-use
- Colored
- Supports args/kwargs
- Returns object results


## Contributing
Before you begin contributing to our project, it is important to familiarize yourself with and agree to the following documents:

1. **License**: By contributing, you agree to your code being licensed under the project's license. Please review the [LICENSE](LICENSE) for details.

2. **Disclaimer**: Please read and understand our project's disclaimer, which can be found in [DISCLAIMER.md](DISCLAIMER.md). 

3. **Notice**: Our project may include third-party components or dependencies that require compliance with the Apache License Version 2.0. Make sure to read and adhere to the terms outlined in the [NOTICE.md](NOTICE.md) to comply with Apache License Version 2.0 requirements.

We appreciate your willingness to contribute to our project. Follow these guidelines to ensure a smooth and collaborative contribution process:


### Reporting Issues
If you encounter a bug, have a suggestion, or want to request a new feature, please check if there's already an existing issue related to it in our issue tracker. If not, feel free to create a new issue, providing as much detail as possible, including:

- A clear and descriptive title.
- Steps to reproduce the issue.
- Expected and actual behavior.
- Your environment (OS, browser, version, etc.).


### Making Changes
If you want to work on an existing issue or implement a new feature, follow these steps:

1. Fork the repository to your GitHub/GitLab account.
2. Create a new branch for your changes: `git checkout -b feature/your-feature-name`.
3. Make your changes, ensuring that your code follows our coding standards and conventions.
4. Test your changes thoroughly.
5. Commit your changes with a clear and concise commit message.
6. Push your changes to your fork on GitHub: `git push origin feature/your-feature-name`.
7. Create a Pull Request (PR) in our repository, describing the changes you've made and referencing any related issues.
8. We'll review your PR, provide feedback, and work with you to address any concerns or suggestions.

We appreciate your contributions, and thank you for helping us improve our project. Your efforts make a difference, and we're grateful for your support.


## License
This project uses the license [Apache License, Version 2.0](LICENSE). Please read the license file carefully before using the project.


## Notice
Our project may include third-party components or dependencies that require compliance with the Apache License Version 2.0. Make sure to read and adhere to the terms outlined in the [NOTICE.md](NOTICE.md) to comply with Apache License Version 2.0 requirements.


## Disclaimer
This project uses a disclaimer. Please, before starting to use this project, carefully read the file: [DISCLAIMER.md](DISCLAIMER.md). By using this project you agree with all points in this file.


## Contacts
Email: welryzis.public@gmail.com


##
Copyright (c) 2023 Welryzis

Licensed under the Apache License, Version 2.0 (the "License");
