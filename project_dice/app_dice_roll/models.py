from django.db import models



class Dice(models.Model):

    id_dice = models.AutoField(primary_key=True)
    sides = models.IntegerField()
    
    

        