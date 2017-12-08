import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

faker=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics)[0])
    t.save()
    return t

def popular(N=5):
    #get topic for the entry
    for entry in range(N):
        # get topic for the entry
        top=add_topic()
        #create the fake data for that entry

