# Django-Auto-Forum
![image](https://img.shields.io/github/followers/jjheffernan.svg?style=social&label=Follow&maxAge=2592000)
## A website for car enthusiast how-tos
Django Based Forum with content hosting to cloud, focused around Auto Enthusiasts

## BEFORE YOU CODE
Install virtual environment `-m venv venv`
Install django `python3 -m pip install django`
Make sure you have a specific version of Python in your virtual environment, 
see `requirements.txt` for the python dependencies and project dependencies.
Use `pip freeze` to check the current virtual environment installs. Refer to previous for matching.

### Getting Started
In terminal within the project root, run `python manage.py runserver`
See the *docs* folder for some extra documentation on the specifics of the program


## Module List
- user_profile (user data is stored here. Groups may be a mix-in of these in the future)
- forum_base (basic django install lives here, might be refactored into django_base)
- projects (this app is to manipulate the projects view.)
- test_page [NOT FOR PRODUCTION] (used for testing and separates redirection  )
- blog (long format posts that are designed as static, only for announcements and configuring advanced views)
- discuss_forum (this is where the forum is held)
### To Do 
- User app (V1)
- Forum App (WIP)
- Subforum App (WIP)
- Post to Forum (WIP)
- Post to Profile
- Comment on Post
- Interact with Post/Comment
- Basic Upload File 
- Change Function Based Views to Class based views (WIP)
### Future Features
- Profile Page (WIP)
- Private Posts (V0)
- Garage on Profile
- Groups
- Chats
- Private Messages
- Group Permissions
- Group Chats
- Dev Blog (V1)
- Front Page 
- Add in JS Front End Framework
- Image host to Cloud
- Archive
- 

## Tech Stack (as)
- Django Package List:
  - Added Pillow to venv (8/30)
  - Added gunicorn (9/1)
  - Added django-heroku (9/2)
  - Added django storages (9/2)
  - Added django crispy forms (9/2)
  - Added boto3 for storage (9/2)
  - Added django hitcount (9/2)
  - Added django storages (9/2)
  - Added django tinymce (9/2)
  - Added django taggit (9/2)
  




