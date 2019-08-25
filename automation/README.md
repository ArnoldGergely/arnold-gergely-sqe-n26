# Task 3 solution

## NOTE: Due to limited time the instructions are recommended for Linux only, as myself haven't used Windows for development for years, Mac at all.

### Requirements to work with the framework

    * Python 3.6
    * Pip3
    * IDE by preference that support Python (optional)
    
#### Creating new repository (with SSH key)
Create a directory where you want to download and create a project.
Go into the project directory, open the console and type in next commands:

    git clone ssh://git@github.com:ArnoldGergely/arnold-gergely-sqe-n26.git
    
Or by HTTPS using command:

    git clone https://github.com/ArnoldGergely/arnold-gergely-sqe-n26.git


Having the downloaded text file **requirements.txt** install them into venv with command

    pip3 install -r requirements.txt

For any further updates/changes regarding the requirements to update the venv use command:

    pip3 install -r requirements.txt --upgrade
    
### Windows instalation and usage

To setup Python on Windows please follow the official guidelines on the [Official Python website](https://www.python.org/)

Additional useful tutorials for setup:

[How To Install Python, pip, and virtualenv on Windows with PowerShell](http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/)

[Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### MacOS instalation and usage

Never did use Mac, so Google is your best friend here... May the Gods of Internet in your favor...

### Testing framework folder, files hierarchy and usage

Installation of the framework should be done by now from the version control repository README file.
Framework is written in Python language and it has highly advised to follow the coding guides from their ruling:
Folder names, file names and method names are small letters divided with underscore between words. Class name words start with capital letters without underscore. Tests always start
with __test_*__ in order to be recognised by the unittest and pytest libraries that will execute tests.

Folder hierarchy:

    automation/
        src/  
            base/  
                ...
            tests/
            ...
    ...
    
Folder **base/** - to contain all the base files and functionsthat can be inherited on the line for reusability.

Folder **tests/** - to contain all tests grouped by the grouping conventions.

### Test runs from Terminal/Bash/Docker - MAKE SURE YOU ARE IN **automation** folder

To run test first check configuration file at **config.ini**.

Test runs are capable to run in single-sequential or parallel order, packaged into some runner file e.g testrunner.py and the executions can be conducted with various commands:

Run single-sequential, example command:

    ./run_test.py test_runner.py
    
    In case python 3 is not your default python version try
        python3 ./run_test.py test_runner.py

Run parallel with 3 browsers, example command:

    ./run_test.py -n 3 test_runner.py -n 3
    
    In case python 3 is not your default python version try
        python3 ./run_test.py -n 3 test_runner.py -n 3

Run in parallel with HTML report generation at the end, example command:

    ./run_test.py --html test_runner.py -n 3
    
    In case python 3 is not your default python version try
        python3 ./run_test.py --html test_runner.py -n 3

**NOTE:** Combination of commands is possible, the pytest will parse it and work with it accordingly, parallel or single test run. The --html command will create the html report index.html

For more commands run:

    ./run_test.py --help
    
    In case python 3 is not your default python version try
        python3 ./run_test.py --help