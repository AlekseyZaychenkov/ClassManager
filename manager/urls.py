from django.urls import path

from manager.views import home


urlpatterns = [
    path('home', home, name="home"),
    path('home?current_group=<int:current_group_id>', home,
         name="home_current_group"),
    path('home?current_group_id=<int:current_group_id>?current_student_id=<int:current_student_id>?context_action=<str:context_action>',
         home, name="home_with_action"),
    path(
        'home?current_group_id=<int:current_group_id>?context_action=<str:context_action>',
        home, name="home_group_with_action"),
    path(
        'home?current_student_id=<int:current_student_id>?context_action=<str:context_action>',
        home, name="home_student_with_action"),
    # path('home?current_group_id=<int:current_group_id>?group_to_delete_id=<int:group_to_delete_id>', home,
    #      name="home_current_group_group_to_delete"),

    # path('home?image_id=<int:selected_image_id>', home_image_id, name="home_image_by_id"),
    # path('home?image_id=<int:selected_image_id>?image_action=<str:image_action>',
    #      home_image_id_action, name="home_image_by_id_by_action"),
]
