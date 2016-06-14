# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
#############################################使用生成器作数据准备 #################################3


series_Shares=[]
series_Trade=[]



#整理出DATAFRAME与SERIES的关系，进行图表绘制，图表的绘制基本是根据SERIS来获取

##############################################define route view functions start################################

def ecchart(request):
    context={

    }
    return render(request,'chart_ec.html',context)

def ecchart_trade(request):
    context={

    }
    return render(request,'chart_ec_trade.html',context)
