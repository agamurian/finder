# finder
functional repl-based python file finder

----------------------------------------

you will command promt:

will find all files in current folder:
----------------------------------------
> ext html


to change folder:
----------------------------------------
> cd /your/folder


to change folder:
----------------------------------------
> cd /your/folder


to display all files in folder (recursievly):
----------------------------------------
> ls

and non-recursively folders in current folder:
> dirs

ext can take multiple arguments
> ext html blend txt

and any function can:
---------------------------------------
> cmd arg arg arg

in fact this is python interpreter:
it will be converted to:
(via eval and lambdas)

cmd("arg","arg","arg","arg")

wich is just long to type

so to extend it you just define functions:

def ls(*args):
  for arg in args:
    ...

functions you above are here in code in 
utils.py for utility functions
