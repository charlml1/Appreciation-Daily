# Appreciation-Today
This is a desktop app written in Python. The goal of this program is to encourage people to list three things they are thankful for daily. The feeling of gratitude can lead to experiencing more positive emotions and having better overall health.

This program has been written using the import of tkinter, tkcalendar, and sqlite3. When the code is run, the UI of a calendar appears with each day being selectable.

![Calendar_UI (2)](https://user-images.githubusercontent.com/44219118/71773899-3a2e7600-2f1a-11ea-9281-81c7631424e2.png)

After selecting a certain day, a new window appears that requests the user to fill in three things they are thankful for today. After filling in the three entry boxes, clicking submit will save the entries with the date to a database named Thanks.db. Then, by using DB Browser for SQLite, the user can access the information from the database to see their progress.

In the examples folder, there is a video showing how the application works and how to access the database with the information.

## Installation
The python file, tkinter_project.py, uses Python 3.7 to run.
The code imports from the module, TkCalendar, which is not automatically downloaded as a part of python. Here is a link to a page that will help with the installation of TkCalendar https://pypi.org/project/tkcalendar/#installation.
Finally, to access the database, you must download DB Browser for SQLite at https://sqlitebrowser.org/dl/. 

After running the program and saving the information to Thanks.db,
  1. Open DB Browser for SQLite
  2. Select "Open Database" at the top
  3. Find and select the file, Thanks.db, which should be saved in the same directory as the Python file, tkinter_project.py.
  4. Select the "Browse Data" tab at the top to view all of your data
