from django.db import models
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class Project_Scope(models.Model):
    scope_name = models.CharField(max_length=50)
    scope_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.scope_name}'

    class Meta:
        db_table = 'project_scope_table'
        verbose_name_plural = 'Project Scopes'


class Project_Location(models.Model):
    location_name = models.CharField(max_length=50)
    location_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.location_name}'
    class Meta:
        db_table = 'project_location_table'
        verbose_name_plural = 'Project Locations'


class Project_Decipline(models.Model):
    decipline_name = models.CharField(max_length=50)
    decipline_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.decipline_name}'


    class Meta:
        db_table = 'project_deciple_table'
        verbose_name_plural = 'Project Deciplines'



class Project_Structure(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_code = models.CharField(max_length=10)
    project_scope_election = models.ForeignKey(Project_Scope,on_delete=models.PROTECT,related_name='project_scope_election')
    project_location_election = models.ForeignKey(Project_Location,on_delete=models.PROTECT,related_name='project_location_election')
    project_detail_location = models.CharField(max_length=500,null=True,blank=True)
    project_start_date = models.DateField(null=True,blank=True)
    project_end_date = models.DateField(null=True,blank=True)
    project_deciplines = models.ManyToManyField(Project_Decipline,related_name='project_deciplines')

    def total_project_deciplines(self):
        return '|'.join([obj.decipline_code for obj in self.project_deciplines.all()])


    def __str__(self):
        return f'{self.project_name}'

    class Meta:
        db_table = 'project_structure_table'
        verbose_name_plural = 'Projects'
        ordering = ('project_name',)



class Document_Revision(models.Model):
    revision_name = models.CharField(max_length=200)
    revision_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.revision_name}'

    class Meta:
        db_table = 'document_revision_table'
        verbose_name_plural = 'Document Revisions'

class Document_Type(models.Model):
    document_type_name = models.CharField(max_length=50)
    document_type_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.document_type_name}'

    class Meta:
        db_table = 'document_type_table'
        verbose_name_plural = 'Document Types'



class Issue_Status(models.Model):
    issue_name = models.CharField(max_length=200)
    issue_code = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.issue_name}'

    class Meta:
        db_table = 'issue_status_table'
        verbose_name_plural = 'Issue Status'


class Document_Class(models.Model):
    class_name = models.CharField(max_length=50)
    class_code = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.class_name}'

    class Meta:
        db_table = 'document_class_table'
        verbose_name_plural = 'Document Classes'



class Document(models.Model):
    document_name = models.CharField(max_length=200,null=True)
    project_election = models.ForeignKey(
        Project_Structure,
        on_delete=models.CASCADE,
        related_name='documents',
    )

    document_decipline = ChainedForeignKey(
        Project_Decipline,
        chained_field='project_election',
        chained_model_field='project_deciplines',
        show_all=False,
        auto_choose=False,
        sort=True,
        on_delete=models.PROTECT,
        related_name='documents',
    )

    file = models.FileField(upload_to='documents')
    document_type = models.ForeignKey(Document_Type,on_delete=models.PROTECT,related_name='documents')
    status = models.ForeignKey(Issue_Status,on_delete=models.PROTECT,related_name='documents')
    revision = models.ForeignKey(Document_Revision,on_delete=models.PROTECT,related_name='documents')
    document_class = models.ForeignKey(Document_Class,on_delete=models.PROTECT,related_name='documents')


    def clean(self):
        super().clean()

        if self.project_election_id and self.document_decipline_id:
            belongs_to_project = self.project_election.project_deciplines.filter(
                pk=self.document_decipline_id
            ).exists()

            if not belongs_to_project:
                raise ValidationError({
                    'document_decipline':
                        'project has not this decipline',
                })

    def __str__(self):
        return f'{self.project_election} - {self.document_decipline} - {self.file.name}'







