# Appreciation-Daily
This is a desktop app written in Python. The goal of this program is to encourage people to list three things they are thankful for daily. The feeling of gratitude can lead to feeling more positive emotions and having better overall health.

This program has been written using the import of tkinter, tkcalendar, and sqlite3. When the code is run, the UI of a calendar appears with each day being selectable.

![Calendar_UI (2)](https://user-images.githubusercontent.com/44219118/71773899-3a2e7600-2f1a-11ea-9281-81c7631424e2.png)

After selecting a certain day, a new window appears that requests the user to fill in three things they are thankful for today. After filling in the three entry boxes, clicking submit will save the entries with the date to a database named Thanks.db. Then, by using DB Browser for SQLite, the user can access the information from the database to see their progress.
