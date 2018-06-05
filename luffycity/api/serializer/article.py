from rest_framework import serializers
from ..models import *


class ArticleModelSerializers(serializers.ModelSerializer):
    source = serializers.CharField(source='source.name')

    class Meta:
        model = Article
        fields = ['id', "title", "source", 'brief','head_img','content',
                  'pub_date','comment_num','agree_num','view_num','collect_num'
                  ]  #需要序列化的字段，存在data中
