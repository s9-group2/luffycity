from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import
from rest_framework import viewsets
from rest_framework.viewsets import ViewSetMixin
from ..models import *
from api.serializer.course import *
from api.serializer.article import *
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
# class CourseView(APIView):
#     def get(self, request, *args, **kwargs):
#         print(request.version)
#         ret = {'code':1000, 'data':None}
#         try:
#
#             course_list = Course.objects.all()
#             course_list = CourseModelSerializers(course_list,many=True)  #记得queryset用many=True
#             print(course_list.data)
#             ret['data'] = course_list.data
#         except Exception as e:
#             ret['code'] = 1001
#             ret['error'] = '获取数据失败'
#
#         return Response(ret)

class CourseModelView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class =CourseModelSerializers

    def list(self, request, *args, **kwargs):
        ret = {'code':1000, 'data':None}
        try:

            course_list = Course.objects.all()
            course_list = CourseModelSerializers(course_list,many=True)  #记得queryset用many=True
            print(course_list.data)
            ret['data'] = course_list.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取数据失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):

        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')

            obj = CourseDetail.objects.filter(course_id=pk).first()

            obj_ser = CourseDetailModelSerializers(obj)
            print(obj_ser.data)
            ret['data'] = obj_ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取数据失败'

        return Response(ret)


