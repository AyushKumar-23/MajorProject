from django.db import models

# Create your models here.
class PublishStateOptions(models.TextChoices):
        #CONSTANT = DB_VALUE, USER_DIAPLSY_VALUE
        PUBLISH = 'PU','Publish'
        DRAFT = "DR", "Draft"