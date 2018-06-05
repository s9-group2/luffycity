from django.contrib import admin
from api import models
# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.CourseDetail)
admin.site.register(models.CourseCategory)
admin.site.register(models.CourseSubCategory)
admin.site.register(models.CourseOutline)
admin.site.register(models.CourseChapter)
admin.site.register(models.CourseSection)
admin.site.register(models.Article)
admin.site.register(models.ArticleSource)

# admin.site.register(models)