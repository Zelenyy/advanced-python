from typing import Iterable

my_global_dict: dict[int, float] = {}


def greeting_1(name):
    return 'Hello ' + name


def greeting_2(name: str) -> str:
    return 'Hello ' + name


def greet_all_1(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)


def greet_all_2(names: Iterable[str]) -> None:
    for name in names:
        print('Hello ' + name)


if __name__ == '__main__':
    greeting_1(3)
    greeting_1("Name")

    greeting_2(3)
    greeting_2("Name")
    greeting_2(b"aasdfsda")

    a = greeting_2("Name")
    greeting_2(a)
    a = 1
    greeting_2(a)