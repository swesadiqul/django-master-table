from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the custom user model


# Create your models here.
class Business(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=150)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    industry = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField()
    email = models.EmailField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    social_media_facebook = models.URLField(blank=True, null=True)
    social_media_twitter = models.URLField(blank=True, null=True)
    social_media_linkedin = models.URLField(blank=True, null=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employee_count = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    ceo_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=False)
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

        # if not User.objects.filter(business=self).exists():
        #     user = User.objects.create(
        #         email="{}".format(self.email),  # Set an email for the user
        #         username=f"{self.name}{self.id}".replace(" ", ""),  # Set a username for the user
        #         password="Usc-123!@#",  # You can set the initial password or handle it separately
        #         business=self,  # Associate the user with the business
        #         is_active=True,  # Set the user as active if needed
        #         is_staff=True,  # Grant staff privileges if needed
        #     )
        #     user.set_password("password")  # Set the user's password
        #     user.save()


    def __str__(self):
        return self.name
    
    # class Meta:
    #     unique_together = ('xtype', 'xname')



class Type(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



# class UniversalEntities(models.Model):
#     xbusiness = models.ForeignKey(Business, on_delete=models.CASCADE)
#     xtype = models.ForeignKey('Type', on_delete=models.CASCADE)
#     xname = models.CharField(max_length=100)
#     xdescription = models.TextField(blank=True)
#     xcode = models.CharField(max_length=20, blank=True)
#     xlatitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
#     xlongitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     status = models.BooleanField(default=True)
#     xcreated_at = models.DateTimeField(auto_now_add=True)
#     xupdated_at = models.DateTimeField(auto_now=True)                                      

#     def __str__(self):
#         return self.xname
    
    # class Meta:
    #     unique_together = ('xtype', 'xname')


class Table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Button(models.Model):
    name = models.CharField(max_length=100)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AccessControl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)  # You'll need to define the 'Table' model
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  # You'll need to define the 'Menu' model
    page = models.ForeignKey(Page, on_delete=models.CASCADE)  # You'll need to define the 'Page' model
    button = models.ForeignKey(Button, on_delete=models.CASCADE)  # You'll need to define the 'Button' model
    can_view = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'business', 'table', 'menu', 'page', 'button')
