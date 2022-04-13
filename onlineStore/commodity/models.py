from django.db import models

"""
1. model need inherit models.Model
2. system will auto add first primary key - id
3. variable(字段)
    variable = model.type(option)
    
    variable is the table's variable
    variable can not use key world like 'mysql' 'python'
    
    char(M)
    varchar(M)
    M is the option
"""
# Create your models here.
class BookInfo(models.Model):
    # id
    name =  models.CharField(max_length=10)

    # rewrite str method let admin show the name of the book
    def __str__(self):
        return self.name



    # human
    # Model class for preparing person list information
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # Foreign key constraints: which book a character belongs to
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    # rewrite str method let admin show the name of the people
    def __str__(self):
        return self.name