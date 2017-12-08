import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

faken=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def popular(N=5):
    #get topic for the entry
    for entry in range(N):
        # get topic for the entry
        top=add_topic()
        #create the fake data for that entry
        fake_url= faken.url()
        fake_date= faken.date()
        fake_name=faken.company()

        #create the new webpage entry
        webg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake access record for that webpage
        acc_rec =AccessRecord.objects.get_or_create(name=webg, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    popular(20)
    print('populating complete!')

