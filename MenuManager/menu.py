import os
import platform
from .colors import *
from .exceptions import MenuError


class Menu:
    def __init__(self, name: str, desc: str | None = None):
        """
        :param name: Name of menu
        :param desc: Menu description
        """
        self.data = []
        self.name = name
        self.desc = desc

    def add_option(self, label: str, instance: callable, *args, **kwargs):
        """
        :param label: Label of option
        :param instance: Callable instance
        :param args: Args for instance
        :param kwargs: Kwargs for instance
        :return: None
        """
        self.data.append({
            "label": label,
            "instance": instance,
            "args": args,
            "kwargs": kwargs,
        })

    def show(self):
        self._clear()
        self._print_header()
        self._print_options()

        try:
            res = int(input(f"{YELLOW}#> {RESET}"))

            option = self.data[res]
            instance = option['instance']
            args = option['args']
            kwargs = option['kwargs']

            instance_res = instance(*args, **kwargs)
            return instance_res
        except (ValueError, IndexError) as ex:
            raise MenuError(ex)

    def _print_header(self):
        print(f"{BOLD_RED}{self.name}{RESET}")
        print(f"  {CYAN}{self.desc}{RESET}", end="\n\n")

    def _print_options(self):
        for index, option in enumerate(self.data):
            print(f"{index}) {option['label']}")

    @staticmethod
    def _clear():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
