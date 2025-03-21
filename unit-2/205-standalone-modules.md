{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5ba438f8",
   "metadata": {},
   "source": [
    "# Standalone Python Modules\n",
    "\n",
    "So far, we've been writing our code all in Jupyter.  But when it comes time to write code that we want to reuse, we want to put it into a standalone `*.py` file.\n",
    "\n",
    "Then we can load it on in python (or Jupyter) and use the capabilities it provides or make it a standalone program that can be run from the command line.\n",
    "\n",
    "## Editors\n",
    "\n",
    "There are a number of popular editors for writing python source.  Some\n",
    "popular ones include:\n",
    "\n",
    "* spyder: https://www.spyder-ide.org/\n",
    "\n",
    "* VS Code: https://code.visualstudio.com/\n",
    "\n",
    "* emacs / nano / vi / vim / gedit"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80583c68",
   "metadata": {},
   "source": [
    "\n",
    "## Basic module:\n",
    "\n",
    "Here's a very simply module (lets call it `hello.py`):\n",
    "\n",
    "```python\n",
    "def hello():\n",
    "    print(\"hello\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    hello()\n",
    "```\n",
    "\n",
    "There are two ways we can use this.\n",
    "\n",
    "* Inside of python (or IPython), we can do:\n",
    "\n",
    "  ```\n",
    "  import hello\n",
    "  hello.hello()\n",
    "  ```\n",
    "\n",
    "* From the command line, we can do:\n",
    "\n",
    "  ```\n",
    "  python hello.py\n",
    "  ```\n",
    "\n",
    "Additionally, on a Unix system, we can add:\n",
    "\n",
    "```python\n",
    "#!/usr/bin/env python3\n",
    "```\n",
    "\n",
    "to the top and then mark the file as executable, via:\n",
    "\n",
    "```\n",
    "chmod a+x hello.py\n",
    "```\n",
    "\n",
    "allowing us to execute it simply as:\n",
    "\n",
    "```\n",
    "./hello.py\n",
    "\n",
    "```\n",
    "\n",
    "https://linuxhint.com/linux_chmod_command_tutorial_beginners/\n",
    "\n",
    "Here we see how the `__name__` variable is treated by python:\n",
    "\n",
    "* If we import our module into python, then `__name__` is set to the module name\n",
    "\n",
    "* If we run the module from the command line, then `__name__` is set to `__main__`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "abb2383a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      " David\n"
     ]
    }
   ],
   "source": [
    "import importlib\n",
    "import hello as hl\n",
    "hl.hello()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0ab96d16",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      " David\n"
     ]
    }
   ],
   "source": [
    "hl=importlib.reload(hl)\n",
    "hl=hl.hello()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c8c4e9c",
   "metadata": {},
   "source": [
    "## Changing module contents\n",
    "\n",
    "If we make changes to our module file, then we need to re-import it.  This can be done as:\n",
    "\n",
    "```python\n",
    "import importlib\n",
    "example = importlib.reload(example)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17302efd",
   "metadata": {},
   "source": [
    "# The Argparse Library (Command line arguments):\n",
    "\n",
    "The argparse module makes it easy to write user-friendly command-line interfaces.\n",
    "\n",
    "\n",
    "The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.\n",
    "\n",
    "\n",
    "The argparse module also automatically generates help and usage messages.\n",
    "\n",
    "\n",
    "The module will also issue errors when users give the program invalid arguments.\n",
    "\n",
    "#### Reference:\n",
    "https://docs.python.org/3/library/argparse.html\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4772561a",
   "metadata": {},
   "source": [
    "## Core Functionality\n",
    "\n",
    "The argparse module’s support for command-line interfaces is built around an instance of **argparse.ArgumentParser.**\n",
    "\n",
    "\n",
    "It is a container for argument specifications and has options that apply the parser as whole:\n",
    "\n",
    "```python\n",
    "parser = argparse.ArgumentParser(\n",
    "                    prog = 'ProgramName',\n",
    "                    description = 'What the program does',\n",
    "                    epilog = 'Text at the bottom of help')\n",
    "```\n",
    "\n",
    "The **ArgumentParser.add_argument()** method attaches individual argument specifications to the parser. It supports positional arguments, options that accept values, and on/off flags:\n",
    "\n",
    "```python\n",
    "parser.add_argument('filename')    # positional argument\n",
    "parser.add_argument('-c', '--count') # option that takes a value\n",
    "parser.add_argument('-v', '--verbose', action='store_true') # on/off flag\n",
    "```\n",
    "\n",
    "The **ArgumentParser.parse_args()** method runs the parser and places the extracted data in a **argparse.Namespace object**:\n",
    "\n",
    "```\n",
    "args = parser.parse_args()\n",
    "print(args.filename, args.count, args.verbose)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9484b62",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "f2140796",
   "metadata": {},
   "source": [
    "### Example 1:\n",
    "\n",
    "The following code is a Python program that takes a list of integers and produces either the sum or the max:\n",
    "\n",
    "```python\n",
    "import argparse\n",
    "\n",
    "parser = argparse.ArgumentParser(description='Process some integers.')\n",
    "\n",
    "parser.add_argument('integers', metavar='N', type=int, nargs='+',\n",
    "                    help='an integer for the accumulator')\n",
    "\n",
    "parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')\n",
    "\n",
    "args = parser.parse_args()\n",
    "\n",
    "print(args.accumulate(args.integers))\n",
    "```\n",
    "\n",
    "Assuming the above Python code is saved into a file called prog.py, it can be run at the command line and it provides useful help messages:\n",
    "\n",
    "```\n",
    "python prog.py -h\n",
    "usage: prog.py [-h] [--sum] N [N ...]\n",
    "\n",
    "Process some integers.\n",
    "\n",
    "positional arguments:\n",
    " N           an integer for the accumulator\n",
    "\n",
    "options:\n",
    " -h, --help  show this help message and exit\n",
    " --sum       sum the integers (default: find the max)\n",
    " \n",
    "```\n",
    "\n",
    "When run with the appropriate arguments, it prints either the sum or the max of the command-line integers:\n",
    "\n",
    "```\n",
    "python prog.py 1 2 3 4\n",
    "4\n",
    "```\n",
    "\n",
    "```\n",
    "python prog.py 1 2 3 4 --sum\n",
    "10\n",
    "```\n",
    "\n",
    "If invalid arguments are passed in, an error will be displayed:\n",
    "\n",
    "```\n",
    "python prog.py a b c\n",
    "usage: prog.py [-h] [--sum] N [N ...]\n",
    "prog.py: error: argument N: invalid int value: 'a'\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb2304b1",
   "metadata": {},
   "source": [
    "### Example 2:\n",
    "\n",
    "For standalone programs, we often want to have our program take command line arguments that affect the runtime behavior of our program.\n",
    "There are a variety of mechanisms to do this in python, but the best option is the [argparse module](https://docs.python.org/3/library/argparse.html).\n",
    "\n",
    "Here's an example of using `argparse` to take a variety of options:\n",
    "\n",
    "```python\n",
    "#!/usr/bin/env python3\n",
    "\n",
    "# to get usage: use -h\n",
    "import argparse\n",
    "\n",
    "# simple example of argparse\n",
    "\n",
    "parser = argparse.ArgumentParser()\n",
    "parser.add_argument(\"-a\", help=\"the -a option\", action=\"store_true\")\n",
    "parser.add_argument(\"-b\", help=\"-b takes a number\", type=int, default=0)\n",
    "parser.add_argument(\"-c\", help=\"-c takes a string\", type=str, default=None)\n",
    "parser.add_argument(\"--darg\", help=\"the --darg option\", action=\"store_true\")\n",
    "parser.add_argument(\"--earg\", help=\"--earg takes a string\", type=str, metavar=\"test\", default=\"example string\")\n",
    "\n",
    "# extra arguments (positional)\n",
    "parser.add_argument(\"extras\", metavar=\"extra\", type=str, nargs=\"*\",\n",
    "                    help=\"optional positional arguments\")\n",
    "\n",
    "args = parser.parse_args()\n",
    "\n",
    "if args.a:\n",
    "    print(\"-a set\")\n",
    "print(f\"-b = {args.b}\")\n",
    "print(f\"-c = {args.c}\")\n",
    "if args.darg:\n",
    "    print(\"--dargs set\")\n",
    "print(f\"--earg value = {args.earg}\")\n",
    "\n",
    "print(\" \")\n",
    "print(\"extra positional arguments: \")\n",
    "if len(args.extras) > 0:\n",
    "    for e in args.extras:\n",
    "        print(e)\n",
    "```\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21ca34a9",
   "metadata": {},
   "source": [
    "### Execution:\n",
    "\n",
    "```python prog2.py -a -b 3 -c \"hola\" --darg --earg \"chao\" \"regreso\"```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2c93aa8",
   "metadata": {},
   "source": [
    "### sys module vs. argparse:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f944927",
   "metadata": {},
   "source": [
    "### Example 3:\n",
    "\n",
    "You can use **sys.argv** to provide input/output directories for multi-file codes. Let's create the beginning of such code:\n",
    "\n",
    "```\n",
    "vim custom_folders.py\n",
    "```\n",
    "\n",
    "Copy the following lines: \n",
    "\n",
    "```\n",
    "#!/usr/bin/env python\n",
    "\n",
    "import sys\n",
    "\n",
    "inputfolder  = sys.argv[1]\n",
    "outputfolder = sys.argv[2]\n",
    "\n",
    "print('Input folder is: ' + inputfolder, 'Output folder is: ' + outputfolder)\n",
    "\n",
    "print('Now provide number please:')\n",
    "\n",
    "inputnumber = input()\n",
    "\n",
    "print('Thanks, the number provided is: ' + inputnumber)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "83adffe2",
   "metadata": {},
   "source": [
    "## Module Paths\n",
    "\n",
    "How does python find modules? It has a search order:\n",
    "\n",
    "1. current directory\n",
    "\n",
    "\n",
    "2. **PYTHONPATH** environment variable\n",
    "\n",
    "\n",
    "3. System-wide python installation default path\n",
    "\n",
    "We can look at the path via sys.path. On my machine I get:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16b8d5e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d46bc518",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['/Users/wladimir/Dropbox/Yachay_Tech/Semestre4_2023/computational-physics-2/unit-2', '/Users/wladimir/Dropbox/Yachay_Tech/Semestre2_2022/Docencia/Fisica_Computacional_2/Lectures/computational-physics-2/unit-5', '/opt/anaconda3/envs/py37/lib/python37.zip', '/opt/anaconda3/envs/py37/lib/python3.7', '/opt/anaconda3/envs/py37/lib/python3.7/lib-dynload', '', '/opt/anaconda3/envs/py37/lib/python3.7/site-packages', '/opt/anaconda3/envs/py37/lib/python3.7/site-packages/IPython/extensions', '/Users/wladimir/.ipython']\n"
     ]
    }
   ],
   "source": [
    "print(sys.path)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "445ac492",
   "metadata": {},
   "source": [
    "Some of these are packages that I explicited added to my **PYTHONPATH** shell variable.\n",
    "\n",
    "You can find your user-specific path via:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c62f6c65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/Users/wladimir/.local/lib/python3.7/site-packages\r\n"
     ]
    }
   ],
   "source": [
    "!python3 -m site --user-site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67a4c2d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "!python --version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "717382e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import mymodule"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1f9864c5",
   "metadata": {},
   "source": [
    "## PATH on Linux:\n",
    "\n",
    "$PATH contains binaries, i.e. executables.\n",
    "\n",
    "```\n",
    "echo $PATH\n",
    "```\n",
    "\n",
    "```\n",
    "echo $PYTHONPATH\n",
    "```\n",
    "\n",
    "**export** can be used to add additional binaries to a specific $PATH:\n",
    "\n",
    "```\n",
    "export /new-bin/:$PATH\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89a07f5f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "comp_Physics",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
