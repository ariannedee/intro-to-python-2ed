# Python on Windows

## Install configurations
If running the [Python.org](https://www.python.org/downloads/) installer in windows, the default options will:
- Save **python.exe** to Python to `C:\Users\<username>\Appdata\Local\Programs\Python\Python312\`
- Only install Python for your user
- Install the Python Launcher
- Not add **python.exe** to your `PATH` (i.e. you can't use the basic `$ python` command in PowerShell)

You can customize any of these settings. 

Some recommendations:
- Select "Add python.exe to PATH" so you can use the `$ python` command
- On a personal computer, select "Use admin privileges when installing py.exe"
- Select "Customize installation"
- Select "Install Python 3.1X for all users" (this will change the installation location to `C:\ProgramFiles\Python31X\`)
- Or, if you don't want to install for all users, you can still customize where Python is being installed, like `C:\Python312\`

## Running the Python Launcher

Most tutorials will run Python using the `$ python` or `$ python3` commands.
On Windows, if you install Python with the official 
[Python.org](https://www.python.org/downloads/) 
installer and use the default configuration,
those commands will not be available.

Instead, use `$ py` to run Python using the Python Launcher with 
the latest version of Python that you have installed.

`$ py` will launch the Python Console

`$ py <filename>.py` will run a Python (.py) file

`$ py -3.X` will run the specified version if it's installed on your machine (e.g. `$ py -3.11`).  