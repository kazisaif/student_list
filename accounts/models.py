from django.db import models

# Create your models here.
class student_list(models.Model):
    student_id=models.IntegerField()
    student_name=models.CharField(max_length=30)
    student_department=models.CharField(max_length=50)
    student_email=models.EmailField()
    student_mobile=models.IntegerField()
    student_address=models.CharField(max_length=50,null=True)

    class Meta:
        db_table='student_list'

    def __str__(self):
        return self.student_id