# Directory Structure and Files

- main.py: runs the server creating the website
- website: contains the website
- website/static: contains non-html files that don't change (css, js, images, etc)
- website/templates: contains html code for the website
- website/__init\_\_.py: has function for creating website and databse
- website/views.py: has server response for different URL endpoints
- website/auth.py (only necessary if we have a login system): handles login server requests
- website/models.py: contains python classes outlining the things stored in the database

## Installing Dependencies

On MacOS & Linux,

```bash
python3 -m pip install -r requirements.txt
```

On Windows,

```bash
py -m pip install -r requirements.txt
```

## Running the Website

In the main directory, run ```main.py```.

- macOS, Linux: `python3 main.py`
- Windows: `py main.py`

On the console, you should see ```Running on http://.../```.
Copy paste the URL into a web browser. To stop running,
press ```Ctrl + C``` (if using terminal), stop the execution
of the program in your IDE, or stop the execution of python in
Task Manager (or other OS equivalent programs).

