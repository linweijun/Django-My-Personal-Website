# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse
from .models import About
from django.db import connection

# Create your views here.
def about(request):
    try:
        #获取id
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM About_about")
        about_id = cursor.fetchall()[0]

        #查询详细信息
        cursor.execute("SELECT Introduction FROM About_about WHERE id=%s", [about_id])
        about_info = cursor.fetchall()[0]
        #创建时间
        cursor.execute("SELECT Create_time FROM About_about WHERE id=%s",[about_id])
        about_create = cursor.fetchall()[0]
        #编辑时间
        cursor.execute("SELECT Edit_time FROM About_about WHERE id=%s", [about_id])
        about_edit = cursor.fetchall()[0]
        return render(request, 'about.html', {'about_info': about_info[0], \
                                          'about_edit':about_edit[0], \
                                          'about_create':about_create[0]})
    except:
        #数据库未创建时数据填充
        about_info = "未修改，初始化状态…………"
        about_edit = "0000-00-00"
        about_create = "0000-00-00"
        return render(request, 'about.html',{'about_info': about_info, \
                                          'about_edit':about_edit, \
                                          'about_create':about_create})
