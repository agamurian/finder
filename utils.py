import os
import functools
from threading import Timer

sep = "------------------------------------------------------"

root = "C:\\Users\\anastasy\\gits"


def tree_print(path, *args):
    global previous_path
    previous_path = root

    def do_in_dir(path, func, level, *args):
        for root, dirs, files in os.walk(path):
            level = len(dirs)
            for fullname in files:
                path = os.path.join(root, *dirs, fullname)
                name = path.replace(previous_path)
                previous_path = path
                func(name, level)

    def func(name, level):
        print(level)
        print(name)

    do_in_dir(path, func, level, *args)


def find_by_ext(path, *args):
    fullname = os.path.split(path)[-1]
    if len(fullname.split(".")) == 2:
        name, ext = fullname.split(".")
        for arg in args:
            if ext == arg:
                print(sep)
                print(path.replace(fullname, ""))
                print(fullname)
    if len(fullname.split(".")) == 1:
        name = fullname


def find_by_name(path, *args):
    fullname = os.path.split(path)[-1]
    if len(fullname.split(".")) == 2:
        name, ext = fullname.split(".")
        for arg in args:
            if name == arg:
                print(sep)
                print(path.replace(fullname, ""))
                print(fullname)
    if len(fullname.split(".")) == 1:
        name = fullname
        for arg in args:
            if name == arg:
                print(sep)
                print(path.replace(fullname, ""))
                print(fullname)


def find_by_contains(path, *args):
    fullname = os.path.split(path)[-1]
    if len(fullname.split(".")) == 2:
        name, ext = fullname.split(".")
        for arg in args:
            if arg in name:
                print(sep)
                print(path.replace(fullname, ""))
                print(fullname)
    if len(fullname.split(".")) == 1:
        name = fullname


def find_by_ends(path, *args):
    fullname = os.path.split(path)[-1]
    if len(fullname.split(".")) == 2:
        name, ext = fullname.split(".")
        for arg in args:
            if name.endswith(arg):
                print(sep)
                print(path.replace(fullname, ""))
                print(fullname)
    if len(fullname.split(".")) == 1:
        name = fullname


def find_by_begins(path, *args):
    fullname = os.path.split(path)[-1]
    if len(fullname.split(".")) == 2:
        name, ext = fullname.split(".")
        for arg in args:
            if name.endswith(arg):
                print(sep)
                print(path.replace(fullname, ""))
                print(fullname)
    if len(fullname.split(".")) == 1:
        name = fullname


def no_doubles(lst):
    return list(set(lst))


def do_in_list(lst, func, *args):
    for path in lst:
        func(path, *args)


def do_in_dir(path, func, *args):
    for root, dirs, files in os.walk(path):
        for fullname in files:
            path = os.path.join(root, *dirs, fullname)
            func(path, *args)


ignore = ["node_modules", ".npm", ".git"]


def filter(path):
    for word in ignore:
        if word in path:
            return False
    return True


def display_tree(path, *args):
    if filter(path):
        print(path)


def display_only_folders(path, *args):
    array = os.path.split(path)
    for a in array:
        a.pop
    array = list(set(array))
    for a in array:
        print(a)

    if filter(path):
        print(path)


def debounce(timeout: float):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.func.cancel()
            wrapper.func = Timer(timeout, func, args, kwargs)
            wrapper.func.start()

        wrapper.func = Timer(timeout, lambda: None)
        return wrapper

    return decorator
