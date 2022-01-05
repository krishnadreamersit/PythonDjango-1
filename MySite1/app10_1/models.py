from django.db import models

# Create your models here.
class Person(models.Model):
    full_name=models.CharField(max_length=50)
    contact_address = models.CharField(max_length=50)

    class Meta:
        ordering=['full_name','contact_address', '-id']
        # db_table = tbl_persons

    def __str__(self):
        return str(self.id)+"; "+self.full_name+"; "+self.contact_address