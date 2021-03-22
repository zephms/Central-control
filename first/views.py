from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as oriLogin, logout as oriLogout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from first.models import Auth
import first.sk as sk
import first.bsOCR as bsOCR
ocrTool = bsOCR.dyOCR()
sender = sk.Sender(("", 801))

def index(request):
    return render(request, "index.html", {})

def register(request):
    return render(request, "register.html", {})

def login(request):
    return render(request, "login.html", {})

def verification(request):
    if request.method == "POST":
        tempusr = request.POST['usrac']
        temppwd = request.POST['pwdac']
    print(22222222222)
    print(tempusr)
    print(temppwd)
    user = authenticate(request, username=tempusr, password=temppwd)
    if user is not None:
        oriLogin(request, user)
        usrName = request.user.username
        if (usrName=="ad"):
            return HttpResponseRedirect(reverse('centreName'))
        return HttpResponseRedirect(reverse('usrName'))
    else:
        print("登录不成功")
        return HttpResponseRedirect(reverse('loginName'))

def logout(request):
    print("444444444")
    oriLogout(request)
    return HttpResponseRedirect(reverse("loginName"))

def centre(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('loginName'))
    if (request.user.username != "ad"):
        return HttpResponseRedirect(reverse('usrName'))
    auths = Auth.objects.all()
    qunkong = auths.filter(status=True)
    duli = auths.filter(status=False)

    context = {"qunkong": qunkong, "duli":duli}
    return render(request, "centre.html", context)
    
def addusr(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('loginName'))
    if (request.user.username != "ad"):
        return HttpResponseRedirect(reverse('usrName'))
    if request.method == "POST":
        n = request.POST.get("usrName", "err")
        d = request.POST.get("discription", "")
        c = request.POST.get("count", "0")
        try:
            Auth(usrName=n, desc=d, count=c).save()
            return HttpResponseRedirect(reverse("centreName"))
        except:
            content = {"Msg":"建议检查输入格式,包括卡密不可以有空白符,还不能和已有的卡密重复,设备台数得是阿拉伯数字", "red":True}
            return render(request, "aleart.html", content)
    

def usr(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('loginName'))
    if (request.user.username == "ad"):
        return HttpResponseRedirect(reverse("centre"))
    auths = Auth.objects.all()
    auths = [i for i in auths if i.usrName==request.user.username]
    context = {'auths':auths, 'usrName':request.user.username}
    return render(request, "usr.html", context)

def sendcmd(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('loginName'))
    cmd2Send = {}
    try:
        if request.method == "POST":
            cmd2Send["usr"] = request.user.username
            cmd2Send["hongbaoTime"] = request.POST["hongbaoTime"]
            cmd2Send["fudaiCiShu"] = request.POST["fudaiCiShu"]
            cmd2Send["canyvRenShuShangXian"] = request.POST["canyvRenShuShangXian"]
            cmd2Send["kaifangFuDai"] = request.POST["kaifangFuDai"]
            cmd2Send["xiaoYvX"] = request.POST["xiaoYvX"]
            cmd2Send["xiaoYvY"] = request.POST["xiaoYvY"]
            cmd2Send["shouYi"] = request.POST["shouYi"]
            cmd2Send["lianXv"] = request.POST["lianXv"]
            cmd2Send["lianxvzhongxiuxi"] = request.POST["lianxvzhongxiuxi"]
            cmd2Send["lianxvzhongxiuximiao"] = request.POST["lianxvzhongxiuximiao"]
            cmd2Send["lianxvbuzhongxiuxi"] = request.POST["lianxvbuzhongxiuxi"]
            cmd2Send["lianxvbuzhongxiuximiao"] = request.POST["lianxvbuzhongxiuximiao"]
            # cmd2Send[""] = request.POST[""]
            sender.sendMsg(json.dumps(cmd2Send))
    except Exception as e:
        print(e)
        content = {"Msg":"建议检查输入格式,这些空都不能空着嗷", "red":True}
        return render(request, "aleart.html", content)
    content = {"Msg":"三秒后返回发送页面"}  
    return render(request, "aleart.html", content)
        
@csrf_exempt
def imgAnalysis(request):
    result = ""
    if request.method == "POST":
        tempB64 = request.POST.get("b64data", "asdf")
        result = ocrTool.resFromB64(tempB64)
    else:
        print("99999999")
        print("意外发生了")
    respDict = {"result" : result}
    return JsonResponse(respDict)
    


def test(request):
    return render(request, "test.html", {})

def testpost(request):
    if request.method == "POST":
        tempCMD = request.POST["cmd"]
        # 执行发送指令
        sender.sendMsg(tempCMD)
    return HttpResponseRedirect(reverse('testName'))
