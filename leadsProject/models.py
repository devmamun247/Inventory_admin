from django.db import models

class Customer(models.Model):
    custom_id = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField()
    facebook = models.URLField()
    country = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    image = models.ImageField(upload_to='customer_images/')
    image_many = models.ManyToManyField('CustomerImageMany', blank=True)  # Link to multiple images

class CustomerImageMany(models.Model):
    image_many = models.ImageField(upload_to='multiple_images/')

#=============================================================================================================================================
# class Customer(models.Model):
#     # id = models.IntegerField(primary_key=True)
#     custom_id = models.CharField(max_length=200)
#     name = models.CharField(max_length=200) 
#     designation = models.CharField(max_length=200) 
#     phone = models.CharField(max_length=200) 
#     email = models.EmailField() 
#     linkedin = models.CharField(max_length=200) 
#     facebook = models.CharField(max_length=200) 
#     country = models.CharField(max_length=200) 
#     address = models.CharField(max_length=200) 
#     dob = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='customer_images/') # Here customer_images is a folder name that all image are store and image is a db field name 

#     # Using a separate model to store multiple images
#     image_many = models.ManyToManyField('CustomerImageMany', blank=True)
#     def __str__(self):
#         return self.name

# class CustomerImageMany(models.Model):
#     image_many = models.ImageField(upload_to='customer_images_many/')
    
#     def __str__(self):
#         return str(self.image_many)














