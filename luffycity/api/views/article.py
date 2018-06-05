from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.viewsets import ViewSetMixin
from ..models import *

from api.serializer.course import *
from api.serializer.article import *
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning



class ArticleModelView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializers

    def list(self, request, *args, **kwargs):
        ret = {'code':1000, 'data':None}
        try:
            article_list = Article.objects.all()
            article_list = ArticleModelSerializers(article_list,many=True)  #记得queryset用many=True
            print(article_list.data)
            ret['data'] = article_list.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取数据失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):

        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')

            obj = Article.objects.filter(course_id=pk).first()

            obj_ser = CourseDetailModelSerializers(obj)
            print(obj_ser.data)
            ret['data'] = obj_ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取数据失败'

        return Response(ret)