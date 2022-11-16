import os

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from class_manager.settings import MEDIA_ROOT
from manager.forms import *
# from manager.models import Gallery

log = logging.getLogger(__name__)


# @login_required
def home(request, current_group_id=None, current_student_id=None, group_to_delete_id=None, student_to_delete_id=None,
         context_action=None):
    # TODO: fix authorization
    # direction = DirectionOfTraining(curator=request.user)
    direction = DirectionOfTraining(id=1)

    if not StudyGroup.objects.filter(id=current_group_id).exists() \
            or (not current_group_id and StudyGroup.objects.filter(direction=direction).exists()):
        current_group_id = StudyGroup.objects.filter(direction=direction).first().id

    if request.POST:
        context_action = __student_request_handler(request, current_group_id)
        context_action = __group_request_handler(request)

    context = __get_basic_home_context(direction,
                                       current_group_id=current_group_id,
                                       current_student_id=current_student_id,
                                       group_to_delete_id=group_to_delete_id,
                                       student_to_delete_id=student_to_delete_id,
                                       context_action=context_action)

    return render(request, "home.html", context)


def __group_request_handler(request):
    if request.POST['action'] == "create_group":
        form = StudyGroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            log.error(form.errors.as_data())

    elif request.POST['action'] == "edit_group":
        form = StudyGroupeEditForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            log.error(form.errors.as_data())

    elif request.POST['action'] == "delete_group":
        form = StudyGroupDeleteForm(request.POST)
        if form.is_valid():
            form.delete()
        else:
            log.error(form.errors.as_data())


def __student_request_handler(request, current_group_id=None):
    if request.POST['action'] == "create_student":
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            log.error(form.errors.as_data())

    elif request.POST['action'] == "edit_student":
        form = StudentEditForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            log.error(form.errors.as_data())

    elif request.POST['action'] == "student_add_to_group":
        form = StudentAddToGroupForm(request.POST)
        if form.is_valid():
            form.add(group_id=current_group_id)
        else:
            log.error(form.errors.as_data())

    elif request.POST['action'] == "student_exclude_from_group":
        form = StudentAddToGroupForm(request.POST)
        if form.is_valid():
            form.add(group_id=None)
        else:
            log.error(form.errors.as_data())

    elif request.POST['action'] == "delete_student":
        form = StudentDeleteForm(request.POST)
        if form.is_valid():
            form.delete()
        else:
            log.error(form.errors.as_data())


def __get_basic_home_context(direction, current_group_id=None, current_student_id=None,
                             group_to_delete_id=None, student_to_delete_id=None, context_action=None):
    context = dict()

    context["context_action"] = context_action

    context["direction_id"] = direction.id
    context["unassigned_students"] = Student.objects.filter(Q(study_group=None) & Q(direction=direction)).values()

    context["current_group_id"] = int(current_group_id)
    context["current_student_id"] = current_student_id

    groups_to_numbers = dict()
    groups = StudyGroup.objects.filter(direction=direction)
    for group in groups:
        groups_to_numbers[group] = Student.objects.filter(study_group=group.id).count()
    context["groups_to_numbers"] = groups_to_numbers

    context["group_create_form"] = StudyGroupCreateForm()
    if current_group_id and StudyGroup.objects.filter(id=current_group_id).exists():
        group = StudyGroup.objects.get(id=current_group_id)
        context["group_edit_form"] = StudyGroupeEditForm(initial={'number': group.number})
        context["current_group"] = StudyGroup.objects.get(id=current_group_id)
        context["current_group_students"] = Student.objects.filter(study_group=current_group_id)
    context["group_delete_form"] = StudyGroupDeleteForm()
    context["group_to_delete_id"] = int(group_to_delete_id) if group_to_delete_id else None

    context["student_create_form"] = StudentCreateForm()
    if current_student_id and Student.objects.filter(id=current_student_id).exists():
        student = Student.objects.get(id=current_student_id)
        context["student_edit_form"] = StudentEditForm(initial={'name': student.name,
                                                                "last_name": student.last_name,
                                                                "middle_name": student.middle_name,
                                                                "phone_number": student.phone_number,
                                                                "gender": student.gender})
    context["student_add_to_group"] = StudentAddToGroupForm()
    context["student_delete_form"] = StudentDeleteForm()
    context["student_to_delete_id"] = student_to_delete_id if student_to_delete_id else None

    return context
