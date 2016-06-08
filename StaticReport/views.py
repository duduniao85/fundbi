# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
#############################################define data generators start #################################3


series_Shares=[]
series_Trade=[]



#整理出DATAFRAME与SERIES的关系，进行图表绘制，图表的绘制基本是根据SERIS来获取

##############################################define route view functions start################################

def chart2(request):
    context = {
        '':series_Shares
    }
