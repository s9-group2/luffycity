from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from django.shortcuts import HttpResponse
from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from django.contrib.contenttypes.models import ContentType


class ArticleSerializer(serializers.ModelSerializer):
    article = serializers.CharField(source='get_article_type_display')
    source = serializers.CharField(source='source.name')
    status = serializers.CharField(source='get_status_display')
    position = serializers.CharField(source='get_position_display')

    class Meta:
        model = models.Article
        fields = ['title', 'article', 'source', 'brief', 'head_img', 'content', 'pub_date', 'offline_date',
                  'order', 'source', 'vid', 'comment_num', 'agree_num', 'view_num', 'collect_num', 'date',
                  'position', 'status']


class ArticlesSerializer(serializers.ModelSerializer):
    article = serializers.CharField(source='get_article_type_display')
    source = serializers.CharField(source='source.name')
    status = serializers.CharField(source='get_status_display')
    position = serializers.CharField(source='get_position_display')

    art_com = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = ['title', 'article', 'source', 'brief', 'head_img', 'content', 'pub_date', 'offline_date',
                  'order', 'source', 'vid', 'comment_num', 'agree_num', 'view_num', 'collect_num', 'date',
                  'position', 'status', 'art_com']

    def get_art_com(self, obj):
        queryset = obj.comment.all()
        return [{'id': i.pk, 'comment': i.content}for i in queryset]


class CommentSerializer(serializers.ModelSerializer):
    content_pk = serializers.CharField(source='content_object.pk')
    b = serializers.CharField(source='content_type')
    b_id = serializers.CharField(source='content_type_id')

    class Meta:
        model = models.Comment
        fields = ['content_pk', 'p_node', 'content', 'account', 'disagree_number', 'agree_number', 'date',
                  'b', 'b_id']

class CollectionSerializer(serializers.ModelSerializer):
    content_pk = serializers.CharField(source='content_object.pk')
    b = serializers.CharField(source='content_type')
    b_id = serializers.CharField(source='content_type_id')
    account_id = serializers.CharField(source='account.pk')

    class Meta:
        model = models.Collection
        fields = ['date', 'content_pk', 'b', 'account_id', 'b_id']








class NewsView(ViewSetMixin,APIView):

    def list(self, request, *args, **kwargs):
        '''
        文章列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        ret = {'code': 1000, 'data': None}

        try:
            queryset = models.Article.objects.all()
            ser = ArticleSerializer(instance=queryset, many=True)

            ret['data'] = ser.data

        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取新闻失败'
        # print(type(ret))

        return Response(ret)

    def create(self, request, *args, **kwargs):
        '''
        增加新闻
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        '''
        {
		"title": "aaa",
        "article": "1",
        "source": "1",
        "brief": "ZY1",
        "head_img": "TX.jpg",
        "content": "ZW1",
        "pub_date": "2018-06-01T07:14:51Z",
        "offline_date": "2018-06-01T07:14:55Z",
        "order": 0,
        "vid": null,
        "comment_num": 0,
        "agree_num": 0,
        "view_num": 0,
        "collect_num": 0,
        "date": "2018-06-01T07:15:24.453612Z",
        "position": "1",
        "art_com": [
            {
                "id": 1,
                "comment": "PL1"
            }
        ]
}
        '''

        ret = {'code': 1000, 'data': None}

        title = request.data.get('title')
        # print(title)
        article = request.data.get('article')
        source = request.data.get('source')
        print(source)
        brief = request.data.get('brief')
        head_img = request.data.get('head_img')
        content = request.data.get('content')
        pub_date = request.data.get('pub_date')
        offline_date = request.data.get('offline_date')
        order = request.data.get('order')
        vid = request.data.get('vid')
        position = request.data.get('position')

        obj = models.Article.objects.create(title=title, article_type=article, source_id=source, brief=brief, head_img=head_img,
                                      content=content, pub_date=pub_date, offline_date=offline_date, order=order,
                                      vid=vid, position=position)

        ret['data'] = request.data
        return Response(ret)


    def new(self, request, *args, **kwargs):
        '''
        新闻详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        ret = {'code': 1000, 'data': None}

        try:
            # 课程ID=2
            pk = kwargs.get('pk')

            # 课程详细对象
            obj = models.Article.objects.filter(pk=pk).first()
            # print(obj)

            ser = ArticlesSerializer(instance=obj)

            ret['data'] = ser.data

        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取新闻失败'
        # print(type(ret))

        return Response(ret)

    def delete(self, request, *args, **kwargs):
        '''
        删除新闻
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {'code': 1000, 'data': None}

        try:
            pk = kwargs.get('pk')
            obj = models.Article.objects.filter(pk=pk).delete()

            # ser = ArticlesSerializer(instance=obj)

            # ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '删除新闻失败'
        # print(type(ret))

        return Response(ret)

    def pu(self, request, *args, **kwargs):
        '''
        更新新闻
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {'code': 1000, 'data': None}

        try:

            title = request.data.get('title')
            # print(title)
            article = request.data.get('article')
            source = request.data.get('source')
            print(source)
            brief = request.data.get('brief')
            head_img = request.data.get('head_img')
            content = request.data.get('content')
            pub_date = request.data.get('pub_date')
            offline_date = request.data.get('offline_date')
            order = request.data.get('order')
            vid = request.data.get('vid')
            position = request.data.get('position')
            pk = kwargs.get('pk')
            obj = models.Article.objects.filter(pk=pk)

            obj.update(title=title, article_type=article, source_id=source, brief=brief,
                                                head_img=head_img,
                                                content=content, pub_date=pub_date, offline_date=offline_date,
                                                order=order,
                                                vid=vid, position=position)
            # obj.save()

            # ser = ArticlesSerializer(instance=obj)

            ret['data'] = request.data
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '更新新闻失败'
        # print(type(ret))

        return Response(ret)



class CommentView(ViewSetMixin, APIView):
    def comment(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}

        try:
            pk = kwargs.get('pk')
            obj = models.Comment.objects.filter(pk=pk).first()

            ser = CommentSerializer(instance=obj)

            ret['data'] = ser.data

        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取评论失败'
        # print(type(ret))

        return Response(ret)

    def create(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        '''
         {
        "p_node": null,
        "content": "PL1",
        "account": 1,
        "disagree_number": 0,
        "agree_number": 0,
        "date": "2018-06-01T09:16:54.762973Z",
        "content_type_id": 21,
        "object_id": 1
    }
        '''

        try:
            content_pk = request
            # pk = kwargs.get('pk')
            # obj = models.Comment.objects.filter(pk=pk).first()

            # ser = CommentSerializer(instance=obj)

            p_node = request.data.get("p_node")
            content = request.data.get("content")
            account_id = request.data.get("account")
            # print(account)
            disagree_number = request.data.get("disagree_number")
            agree_number = request.data.get("agree_number")
            date = request.data.get("date")
            content_type_id = request.data.get("content_type_id")
            object_id = request.data.get("object_id")

            models.Comment.objects.create(p_node=p_node, content=content,
                                          account_id=account_id, disagree_number=disagree_number,
                                          agree_number=agree_number, date=date,
                                          content_type_id=content_type_id, object_id=object_id)

            ret['data'] = request.data
            return Response(ret)

        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '添加评论失败'
        # print(type(ret))

        return Response(ret)




class CollectionView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = models.Collection.objects.filter(pk=pk).first()

            ser = CollectionSerializer(instance=obj)

            ret['data'] = ser.data

        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取收藏失败'
        # print(type(ret))

        return Response(ret)


