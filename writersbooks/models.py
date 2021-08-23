from django.db import models


class Writer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}
