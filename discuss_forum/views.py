# discuss_forum/views.py

# django imports
from django.shortcuts import render, redirect, get_object_or_404

# local namespace imports
from discuss_forum.models import Author, Post, Comment, Reply
from blog.models import Category
# Create your views here.
