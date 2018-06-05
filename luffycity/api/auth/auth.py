from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models

class LuffyAuth(BaseAuthentication):  #定义一个认证的类，继承baseauthentication类

    def authenticate(self, request):  #在类里面第一方法authenticate，必须是这个方法，传入request
        token = request.query_params.get('token')
        obj = models.UserAuthToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({'code':1001,'error':'认证失败'})
        return (obj.user.user,obj)