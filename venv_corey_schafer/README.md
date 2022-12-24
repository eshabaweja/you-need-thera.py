# Virtual Environments - Need

- Python virtual environments are, in simple terms, **a contained environment** for separate pythons to live on your computer.
- dependency management: different versions of packages for different projects
- project isolation: `pip freeze --local > requirements.txt` only gives local site-packages
- keep global `site-packages/` clean by installing site packages (third party libraries) locally in an isolated directory for a particular project

# But WHAT is a virtual environment?
Just a directory with three important components:

- a `site-packages/` folder where third party libraries are installed.
- **symlinks** to Python executables installed on your system.
- **scripts** that ensure executed Python code uses the Python interpreter and site **packages installed inside** the given virtual environment.
- ⚠️ don't put your project files in the venv

# How the heck do you KNOW all this?
- https://towardsdatascience.com/virtual-environments-104c62d48c54
- https://www.youtube.com/watch?v=N5vscPTWKOk

# Terminal Code Snippets
- to install venv library
```pip install virtualenv```
- list global site-packages
```pip list```
- make a virtual environment
```virtualenv project1_env```
- to activate above environment (once you press Enter and the venv activates, it's name gets added to your prompt!)
```source project1_env/bin/activate```
- to demo that we're in a venv, perform `which python` or `which pip` and the output path will be the path to the python **inside the venv**
- ⚠️ **fun part ahead!!!** Now, run `pip list` again. This time, it only lists the packages local to the venv.
- now you can easily ```pip freeze --local > requirements.txt``` to get a list of local site-packages and the versions used in our project.
- to get out of venv, write ```deactivate```
- to get rid of the venv, simply delete it like ```rm -rf project1_env/```

# Now what do I do with the requirements.txt?
- ⚠️ don't put your project files in the venv
- make new venv ```virtualenv -p /usr/bin/python2.7 project2_env```
- activate the new venv
- to install everything from `requirements.txt`, write ```pip install -r requirements.txt```
- check using `pip list`