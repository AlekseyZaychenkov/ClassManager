from django.contrib import admin
from django_object_actions import DjangoObjectActions

from manager.models import DirectionOfTraining, AcademicDiscipline, Curator
from account.models import Account


class AcademicDisciplineAdmin(admin.ModelAdmin):
    list_display = ('title', 'direction_of_training')


class CuratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'middle_name', 'gender', 'phone_number', 'direction_of_training')


class DirectionOfTrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'curator')


class AccountAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('email', 'nick_name',)

    def form_report(self, request, account):
        # TODO: implement method for forming a report
        pass

    form_report.label = "Form new report"
    form_report.short_description = "Forms new report from db"

    change_actions = ('form_report',)


admin.site.register(AcademicDiscipline, AcademicDisciplineAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(DirectionOfTraining, DirectionOfTrainingAdmin)
admin.site.register(Account, AccountAdmin)