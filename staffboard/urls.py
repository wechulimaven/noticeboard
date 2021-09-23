from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from staffboard import HodViews, StaffViews, StudentViews
from staffboard.EditResultVIewClass import EditResultViewClass
from noticeboard import settings



urlpatterns = [


    # path('admin_home',HodViews.admin_home,name="admin_home"),
    # path('add_staff',HodViews.add_staff,name="add_staff"),
    # path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    # path('add_course/', HodViews.add_course,name="add_course"),
    # path('add_course_save', HodViews.add_course_save,name="add_course_save"),
    # path('add_student', HodViews.add_student,name="add_student"),
    # path('add_student_save', HodViews.add_student_save,name="add_student_save"),
    # path('add_subject', HodViews.add_subject,name="add_subject"),
    # path('add_subject_save', HodViews.add_subject_save,name="add_subject_save"),
    # path('manage_staff', HodViews.manage_staff,name="manage_staff"),
    # path('manage_student', HodViews.manage_student,name="manage_student"),
    # path('manage_course', HodViews.manage_course,name="manage_course"),
    # path('manage_subject', HodViews.manage_subject,name="manage_subject"),
    # path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    # path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    # path('edit_student/<str:student_id>', HodViews.edit_student,name="edit_student"),
    # path('edit_student_save', HodViews.edit_student_save,name="edit_student_save"),
    # path('edit_subject/<str:subject_id>', HodViews.edit_subject,name="edit_subject"),
    # path('edit_subject_save', HodViews.edit_subject_save,name="edit_subject_save"),
    # path('edit_course/<str:course_id>', HodViews.edit_course,name="edit_course"),
    # path('edit_course_save', HodViews.edit_course_save,name="edit_course_save"),
    # path('manage_session', HodViews.manage_session,name="manage_session"),
    # path('add_session_save', HodViews.add_session_save,name="add_session_save"),
    # path('check_email_exist', HodViews.check_email_exist,name="check_email_exist"),
    # path('check_username_exist', HodViews.check_username_exist,name="check_username_exist"),
    # path('student_feedback_message', HodViews.student_feedback_message,name="student_feedback_message"),
    # path('student_feedback_message_replied', HodViews.student_feedback_message_replied,name="student_feedback_message_replied"),
    # path('staff_feedback_message', HodViews.staff_feedback_message,name="staff_feedback_message"),
    # path('staff_feedback_message_replied', HodViews.staff_feedback_message_replied,name="staff_feedback_message_replied"),
    # path('student_leave_view', HodViews.student_leave_view,name="student_leave_view"),
    # path('staff_leave_view', HodViews.staff_leave_view,name="staff_leave_view"),
    # path('student_approve_leave/<str:leave_id>', HodViews.student_approve_leave,name="student_approve_leave"),
    # path('student_disapprove_leave/<str:leave_id>', HodViews.student_disapprove_leave,name="student_disapprove_leave"),
    # path('staff_disapprove_leave/<str:leave_id>', HodViews.staff_disapprove_leave,name="staff_disapprove_leave"),
    # path('staff_approve_leave/<str:leave_id>', HodViews.staff_approve_leave,name="staff_approve_leave"),
    # path('admin_view_attendance', HodViews.admin_view_attendance,name="admin_view_attendance"),
    # path('admin_get_attendance_dates', HodViews.admin_get_attendance_dates,name="admin_get_attendance_dates"),
    # path('admin_get_attendance_student', HodViews.admin_get_attendance_student,name="admin_get_attendance_student"),
    # path('admin_profile', HodViews.admin_profile,name="admin_profile"),
    # path('admin_profile_save', HodViews.admin_profile_save,name="admin_profile_save"),
    # path('admin_send_notification_staff', HodViews.admin_send_notification_staff,name="admin_send_notification_staff"),
    # path('admin_send_notification_student', HodViews.admin_send_notification_student,name="admin_send_notification_student"),
    # path('send_student_notification', HodViews.send_student_notification,name="send_student_notification"),
    # path('send_staff_notification', HodViews.send_staff_notification,name="send_staff_notification"),


]