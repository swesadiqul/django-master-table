from django.db import models

# Create your models here.
class Business(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=150)
    founded_year = models.PositiveIntegerField()
    industry = models.CharField(max_length=50)
    website = models.URLField()
    contact_email = models.EmailField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    social_media_facebook = models.URLField(blank=True, null=True)
    social_media_twitter = models.URLField(blank=True, null=True)
    social_media_linkedin = models.URLField(blank=True, null=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employee_count = models.PositiveIntegerField(blank=True, null=True)
    headquarters_address = models.CharField(max_length=200, blank=True, null=True)
    ceo_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            last_business = Business.objects.last()
            if last_business:
                self.id = last_business.id + 1
            else:
                self.id = 1000
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    # class Meta:
    #     unique_together = ('xtype', 'xname')



class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name  


class UniversalEntities(models.Model):
    xtype = models.ForeignKey('Type', on_delete=models.CASCADE)
    xname = models.CharField(max_length=100)
    xdescription = models.TextField(blank=True)
    xcode = models.CharField(max_length=20, blank=True)
    xlatitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    xlongitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    xcreated_at = models.DateTimeField(auto_now_add=True)
    xupdated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.xname
    
    class Meta:
        unique_together = ('xtype', 'xname')
