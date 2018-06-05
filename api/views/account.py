from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from api import models
import uuid


class AuthView(APIView):
    """
    核心是当用户登录的时候，后端生成一个随机字符串，传给前端，
    并更新用户认证表中的随机字符串数据
    """

    def post(self,request,*args,**kwargs):
        """
        用户登录认证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        ret = {'code':1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')

        user = models.Account.objects.filter(username=user,password=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserAuthToken.objects.update_or_create(user=user,defaults={'token':uid})
            ret['token'] = uid
        return Response(ret)