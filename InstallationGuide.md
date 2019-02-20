In this file we will explain how to install pPython and Anaconda for the sessions.

# Python

Python is an interpreter type lanaguage that compiles the code in the run time. 

There are several versions of Python which you may have used or not. Python 2.7 is the most common one, but it is slowly transitioned to Python 3.2 and beyond.

Our sessions are currently run with Python 3.6.2 and beyond.

Current Python is 3.7.2 which you can download via https://www.python.org/downloads/

When you downloaded the program, make sure that you have selected "enable PATH".

When you have downloaded Python, you can run it. You will get an interpreter instead of a blank page or etc. In this interpreter, you can test your one-liner codes. This is not suitable for applicaiton development as its memory will be erased once its closed. To check your version of python open command line (cmd) and type ```python -V``` 
or on your intrepeter

```
>>> from platform import python_version
>>> print(python_version())
```

If you want to write an application, you have to create New File from File tab and save it. 

Python is an indent-sensitive language. 


# Anaconda

Anaconda is a multi-package software that is developed for scientific purposes. It has several python libraries already installed such as numpy, pytorch, sklearn etc.

You can download Anaconda from https://www.anaconda.com/download/

As you can see that there is still Python 2.7 and 3.7 versions which we will choose the latter.

After you have downloaded:

## for Windows Users:

run ```Anaconda prompt```, which has the all packages PATH's inside, and use ```cd``` commands to choose your working directory. Then run your python script with ```python script.py```

## for Linux Users:

use ```cd``` commands to choose your working directory, and run your python scripts with ```python3 script.py```.

## for MacOS users:

_we dont have any mac users, but you can expand it!_
...

# General Info:

to download library in python you have to use ```pip3 install PACKAGENAME```


to download library in Anaconda you have to use ```conda install PACKAGENAME```

you can refer to this as well: https://docs.anaconda.com/_downloads/Anaconda_Starter_Guide_CheatSheet.pdf


If you have any issues, you can message us on Facebook page or open an issue/pull request here.

