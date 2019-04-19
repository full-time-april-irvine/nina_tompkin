from django.db import models
from datetime import datetime

# Create your models here.

class ShowManager(models.Manager):
    
    def validate(self, form):
        errors = []

        if len(form["show_title"]) < 2:
            errors.append("Title must be at least two characters.")
        if Shows.objects.get(title=form["show_title"]):
            errors.append("Show already exists in database.")
        if len(form["show_network"]) < 3:
            errors.append("Network must be at least 3 characters.")
        if not form["show_release"]:
            errors.append("You must enter in a show release date.")
        else:
            if datetime.strptime(form["show_release"], '%Y-%m-%d') > datetime.now():
                errors.append("The show release date must be in the past.")
        #     print("*"*50)
        if form["show_desc"] and len(form["show_desc"]) < 10:
            errors.append("Description should be at least 10 characters.")
            
        return errors

    def easy_create(self,form):
        # Returns the entire object for the new show
        show = Shows.objects.create(title=form["show_title"], network=form["show_network"], release_date=form["show_release"],description=form["show_desc"])
        return show.id

    def get_this_show(self,show_id):
        this_show = Shows.objects.get(id=show_id)
        return this_show

    def update_this_show(self, show_id, form):
        this_show = Shows.objects.get(id=show_id)
        
        this_show.title=form["show_title"]
        this_show.network=form["show_network"]
        this_show.release_date=form["show_release"]
        this_show.description=form["show_desc"]
        this_show.save()

        return this_show
    
    def pull_all_shows(self):
        shows = Shows.objects.all()
        return shows

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()