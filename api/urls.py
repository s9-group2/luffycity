from django.urls import path, include
from api.views import course
from api.views import article
from api.views import account

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('course/',course.CourseModelView.as_view({"get":"list","post":"create"})),
    # path('course/',course.CourseView.as_view()),
    path('course/<int:pk>/',course.CourseModelView.as_view({"get":"retrieve"})),
    path('article/',article.ArticleModelView.as_view({"get":"list","post":"create"})),
    path('article/<int:pk>/',article.ArticleModelView.as_view({"get":"retrieve","post":"update"})),
    path('auth/',account.AuthView.as_view()),
    
]
