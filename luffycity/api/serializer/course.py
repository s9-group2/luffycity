from rest_framework import serializers
from ..models import *
class CourseModelSerializers(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')  # 当在视图中序列化的时候，
    # 先从自定义的字段中取值，自定义字段中没有再从model中找
    video_brief_link = serializers.CharField(source='detail.video_brief_link')
    # video_brief_link = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', "name", "course_img", 'level','video_brief_link']  #需要序列化的字段，存在data中


class CourseDetailModelSerializers(serializers.ModelSerializer):  #序列化组件怎样个运行的过程
    # one2one,forenkey,choice   自定义serialezer字段实现跨表
    title = serializers.CharField(source='course.name')  #即使不取这里面的字段，也不能写错,定义了必须要取这些值
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')
    brief = serializers.CharField(source='course.brief')
    # many2many
    recommends = serializers.SerializerMethodField()  #获取多个值的字段
    comment = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()
    asked_question = serializers.SerializerMethodField()
    pricepolicy = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = CourseDetail
        fields = ['course_slogan', 'why_study','title','img','level','recommends','chapter',
                  'what_to_study_brief','career_improvement','comment','asked_question',
                  'brief','pricepolicy','prerequisite','teachers']
        # depth = 0
    #内置的获取字段的方法
    def get_recommends(self,obj):
        queryset = obj.recommend_courses.all()
        print(queryset)
        return [{'id':row.id, 'title':row.name} for row in queryset]

    def get_chapter(self,obj):

        queryset = obj.course.coursechapters.all()
        return [{'id':row.id, 'name':row.name} for row in queryset]

    def get_comment(self,obj):

        queryset = obj.course.comment.all()
        return [{'id':row.id, 'account':row.account.username,'content':row.content} for row in queryset]

    def get_asked_question(self,obj):

        queryset = obj.course.asked_question.all()
        return [{'id':row.id, 'account':row.question,'content':row.answer} for row in queryset]

    def get_pricepolicy(self,obj):

        queryset = obj.course.price_policy.all()
        return [{'id':row.id, 'account':row.valid_period,'content':row.price} for row in queryset]

    def get_teachers(self,obj):

        queryset = obj.teachers.all()
        return [{'id':row.id, 'name':row.name,'title':row.title,'signature':row.signature,'brief':row.brief} for row in queryset]