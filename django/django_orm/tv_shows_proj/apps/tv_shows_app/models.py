from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    
    def easy_create(self,form):
        # Returns the entire object for the new show
        show = Shows.objects.create(title=form["show_title"], network=form["show_network"], release_date=form["show_release"],description=form["show_desc"])
        return show.id

    def get_this_show(self,show_id):
        this_show = Shows.objects.get(id=show_id)
        return this_show

    def update_this_show(self, show_id, form):
        this_show = Shows.objects.get(id=show_id)
        if form["show_title"]:
            this_show.title=form["show_title"]
            this_show.save()
        if form["show_network"]:
            this_show.network=form["show_network"]
            this_show.save()
        if form["show_release"]:
            this_show.release_date=form["show_release"]
            this_show.save()
        if form["show_desc"]:
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