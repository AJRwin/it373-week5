from django.contrib import admin
from pages.models import Post, Comment, Student, Course, Enrollment
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=("title", "body", "created_at")
    inline = [CommentInline]
    search_fields=("title", "body")
    list_filter=("created_at",)
    ordering=("-created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_at")
    search_fields = ("author", "text")
    list_filter = ("created_at",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title")
    search_fields = ("code", "title")

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "grade")
    list_filter = ("course", "grade")
    search_fields = ("student__first_name", "student__last_name", "course__code")
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display=("author", "post", "created_at")
#     search_fields=("author", "text")
#     list_filter=("created_at",)

# @admin.register(Student)

# @admin.register(Course)

# @admin.register(Enrollment)

# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Student)
# admin.site.register(Course)
# admin.site.register(Enrollment)