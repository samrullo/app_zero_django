# Introduction
This is django app to maintain action items.

*Task*s are linked to a *Task Project* with columns **client**,**project_name**

Each *Task* has **name**, **description**, **deadline**, **status** and **progress** in percentages.

Each *Task* can have comments

# Start django server with custom port number

Run below

```bash
python manage.py runserver 127.0.0.1:<PORT>
```

Example:

```bash
python manage.py runserver 127.0.0.1:7789
```