# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from ldaplogin import LDAPLogin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext


# Create your views here.
#############################################使用生成器作数据准备 #################################3


series_Shares=[]
series_Trade=[]



#整理出DATAFRAME与SERIES的关系，进行图表绘制，图表的绘制基本是根据SERIS来获取

##############################################define route view functions start################################
@login_required
def ecchart(request):
    context={

    }
    return render(request,'chart_ec.html',context)

@login_required
def ecchart_trade(request):

    context={'host':request.GET.get('host',None)
    }
    return render(request,'chart_ec_trade.html',context)

def login(request):
    if request.method == 'GET':
        next = request.GET.get('next', '').strip()
        return render_to_response('login.html', RequestContext(request, {'next': next}))
    if request.method=='POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        next = request.POST.get('next', '').strip()
        print next
        user = auth.authenticate(username=username, password=password)
        if user is not None :
        # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            if len(next)> 0:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect('/ecreport/')
        elif LDAPLogin(username,password):
            #如果修改域密码，则需要更新密码，存新用户插入，老用户则更新密码
            user_new = User.objects.create_user(username=username,password=password)
            user_new.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            # Redirect to a success page.
            if len(next)> 0:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect('/ecreport/')
        else:
            return HttpResponseRedirect("/account/invalid/")
    return render(request,'login.html')


