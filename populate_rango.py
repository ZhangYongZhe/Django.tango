import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page
def populate():
    # 首先创建一些字典，列出想添加到各分类的网页
    # 然后创建一个嵌套字典，设置各分类
    # 这么做看起来不易理解，但是便于迭代，方便为模型添加数据

    python_pages = [
        {"title": "Offcial Pyton Tutorial",
         "url":"http://docs.python.org/2/tutorial/"},
        {


        }
    ]