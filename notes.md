# Auto Forum Notes
This is where notes, research links, and things not for the readme live:

### Research Links
http://cisyst.com/Documents/Library/Design%20and%20Implementation%20Of%20A%20Web%20Forum.pdf
https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/
https://realpython.com/get-started-with-django-1/
https://www.dennisivy.com/post/django-class-based-views/
https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog


An inspirational forum app(s):
https://djangopackages.org/grids/g/forum/
https://spirit-project.com
https://github.com/vitorfs/bootcamp


### What makes a Django App?
Django apps have separated logic. 
The code pattern is Model-View-Controller
#### What does each one do?
- Model Defines the Data Structure. (Often times the DB base layer)
- View displays some or all of the data to the user using HTML and CSS
- Controller handles how the database and view interact
See how they interact [here](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/)

#### What makes django different?
Django handles the controller part within it's engine
- The specific pattern Django uses is the Model-View-Template pattern


### Planned Features
- User Database
- Vehicle Database
- Forum Database
- User Management: (Profiles, Privacy, etc.)
- Image Feed
- Private Messaging

### To Do

### In Progress

### Completed


The model you’ll create will be called Project and will have the following fields:

title will be a short string field to hold the name of your project.
description will be a larger string field to hold a longer piece of text.
technology will be a string field, but its contents will be limited to a select number of choices.
image will be an image field that holds the file path where the image is stored.

