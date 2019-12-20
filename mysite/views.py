# -*- coding: utf-8 -*-
"""
@File    :   views.py
@Author  :   Li Changtai
@E-mail  :   lichangtai17@gmail.com
@Date    :   2019/11/29 12:05
@Software:   PyCharm
"""
from django.shortcuts import render_to_response


def home(requst):
    context = {}
    return render_to_response('home.html', context)
