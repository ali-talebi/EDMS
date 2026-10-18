from django.contrib import admin
from .models import Project_Scope,Project_Location,Project_Decipline,Project_Structure,Document_Revision,Issue_Status,Document_Type
from .models import Document_Class,Document
# Register your models here.


@admin.register(Project_Scope)
class Project_Scop_Admin(admin.ModelAdmin):
    list_display = ('scope_name','scope_code')
    search_fields = ('scope_name','scope_code')

@admin.register(Project_Location)
class Project_Location_Admin(admin.ModelAdmin):
    list_display = ('location_name','location_code')
    search_fields = ('location_name','location_code')

@admin.register(Project_Decipline)
class Project_Decipline_Admin(admin.ModelAdmin):
    list_display = ('decipline_name','decipline_code')
    search_fields = ('decipline_name','decipline_code')

@admin.register(Project_Structure)
class Project_Structure_Admin(admin.ModelAdmin):
    list_display = ('project_name','project_code','project_scope_election','project_location_election','total_project_deciplines')
    # search_fields = ('project_name','project_code','project_location_election')
    # list_editable = ('project_code','project_scope_election')

@admin.register(Issue_Status)
class Issue_Status_Admin(admin.ModelAdmin):
    list_display = ('issue_name','issue_code')
    search_fields = ('issue_name','issue_code')

@admin.register(Document_Revision)
class Document_Revision_Admin(admin.ModelAdmin):
    list_display = ('revision_name','revision_code')
    search_fields = ('revision_name','revision_code')


@admin.register(Document_Type)
class Document_Type_Admin(admin.ModelAdmin):
    list_display = ('document_type_name','document_type_code')
    search_fields = ('document_type_name','document_type_code')

@admin.register(Document_Class)
class Document_Class_Admin(admin.ModelAdmin):
    list_display = ('class_name','class_code')
    search_fields = ('class_name','class_code')

@admin.register(Document)
class Document_Admin(admin.ModelAdmin):
    list_display = ('document_name','project_election','document_decipline','document_type','status','revision')
