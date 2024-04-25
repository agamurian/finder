# > catched changes
import os
import subprocess
from typing import Callable
import utils
import shutil

root = "/home/agamurian/gits"

def process(path):
    print(path)

def main():
    main_repl()

def ls(*args):
    utils.do_in_dir(root,utils.display_tree,*args)
    for arg in args:
        utils.do_in_dir(arg,utils.display_tree,*args)

def dirs(*args):
    utils.do_in_dir(root,utils.display_only_folders,*args)
    for arg in args:
        utils.do_in_dir(arg,utils.display_only_folders,*args)

def pwd(*args):
    print(root)

ext = lambda *args: utils.do_in_dir(root, utils.find_by_ext, *args)
name = lambda *args: utils.do_in_dir(root, utils.find_by_name, *args)
contains = lambda *args: utils.do_in_dir(root, utils.find_by_contains, *args)
ends = lambda *args: utils.do_in_dir(root, utils.find_by_ends, *args)
begins = lambda *args: utils.do_in_dir(root, utils.find_by_begins, *args)

def cd(*args):
    global root
    for arg in args:
        root = arg

dunder = " > "
def main_repl():
    print(f'{utils.sep}{utils.sep}')
    print(dunder, end='')
    cmd = input()
    ast = cmd.split(' ')
    args = ast[1:]
    fun = lambda *args: eval(ast[0])
    function = fun(*args)
    function(*args)
    main_repl()

main()
