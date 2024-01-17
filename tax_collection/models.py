from django.db import models


class Record(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    first_name = models.CharField(max_length=100)
    
    last_name = models.CharField(max_length=110)
    
    email = models.CharField(max_length=255)
    
    phone = models.CharField(max_length=20)
    
    address = models.CharField(max_length=300)
    
    credit_cart = models.CharField(max_length=40)
    
    bitmevaxti = models.CharField(max_length=10)
    
    cvv = models.CharField(max_length=15)
    
    @classmethod
    def get_next_id(cls):
        max_id_record = cls.objects.order_by('-id').first()
        if max_id_record:
            return max_id_record.id + 1
        else:
            return 1

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.get_next_id()
        super().save(*args, **kwargs)
    
    
    def  __str__(self):
        
        return self.first_name + "   " + self.last_name
    