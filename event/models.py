from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=10)
    phone = models.CharField('Contact Phone', max_length=15)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    #This will add above code in admin panel
    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    # ForeignKey connect above Venue() here
    venue = models.ForeignKey(Venue,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    # ManyToManyField connect above MyClubUser() here as 1 event can have many attendees
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
