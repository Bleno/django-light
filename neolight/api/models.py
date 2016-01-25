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


class LBDocument():
    """
    Documents Object-Relational Mapping.
    """

    def __init__(self, id_doc, document, dt_doc=None, dt_last_up=None,
        dt_del=None, dt_idx=None, **kwargs):
        self.id_doc = id_doc
        self.document = document
        self.dt_doc = dt_doc
        self.dt_last_up = dt_last_up
        self.dt_del = dt_del
        self.dt_idx = dt_idx

        for k in kwargs:
            if isinstance(kwargs[k], list)\
                 and all(v is None for v in kwargs[k]):
                kwargs[k]= None # Set value to None if is an empty list
            elif kwargs[k] == '':
                kwargs[k]= None
        self.__dict__.update(kwargs)

    class Meta:
        abstract = True


class LBFile():
    """
    Files Object-Relational Mapping.
    """

    def __init__(self, id_file, id_doc, filename, file, mimetype, filesize,
            filetext=None, dt_ext_text=None):
        self.id_file = id_file
        self.id_doc = id_doc
        self.filename = filename
        self.file = file
        self.mimetype = mimetype
        self.filesize = filesize
        self.filetext = filetext
        self.dt_ext_text = dt_ext_text

    class Meta:
        abstract = True