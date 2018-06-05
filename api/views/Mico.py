from rest_framework.views import APIView
from rest_framework.response import Response
from ..auth.auth import *


class MicroView(APIView):  #当进入视图类的时候，如果需要认证组件认证是否登录，则需要添加‘认证类组’的属性
    authentication_classes = [LuffyAuth,]

    def get(self,request,*args,**kwargs):
        ret = {'code':1000,'title':'微职位'}
        return Response(ret)