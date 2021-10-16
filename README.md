# Directory Structure and Files
- main.py: runs the server creating the website
- website: contains the website
- website/static: contains non-html files that don't change (css, js, images, etc)
- website/templates: contains html code for the website
- website/__init__.py: has function for creating website and databse
- website/views.py: has server response for different URL endpoints
- website/auth.py (only necessary if we have a login system): handles login server requests
- website/models.py: contains python classes outlining the things stored in the database

## Cloning the Repo
NOTE: You must have git and github CLI installed to perform this.
```
gh auth login
git clone https://github.com/nathan-abraham/FlaskPractice
cd FlaskPractice
```

## Running the Website
In the main directory, run ```main.py```. Either:
- Run in terminal: ```python main.py```
- Run in an IDE

On the console, you should see ```Running on http://.../```.
Copy paste the URL into a web browser. To stop running,
press ```Ctrl + C``` (if using terminal), stop the execution
of the program in your IDE, or stop the execution of python in
Task Manager (or other OS equivalent programs).

