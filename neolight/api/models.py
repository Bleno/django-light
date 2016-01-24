from django.db import models

# Create your models here.


class LBBase(models.Model):
    """
        Armazena a estrutura de dados das bases
    """

    #__tablename__ = 'lb_base'

    id_base = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=120, unique=True)

    struct = models.CharField(max_length=120)

    dt_base = models.DateTimeField()

    idx_exp = models.BooleanField()

    idx_exp_url = models.CharField(max_length=120, null=True)

    idx_exp_time = models.IntegerField()

    file_ext = models.BooleanField()

    file_ext_time = models.IntegerField(null=True)

    txt_mapping = models.CharField(max_length=120, null=True)

    class Meta:
        """docstring for Meta"""
        db_table = 'lb_base'
        #fields = ('id_base', 'struct',)
