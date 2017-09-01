from blog.models import Blog,Book,File
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
#首页
def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('blog/index.html', {'blogs':blog_list})

#登录
def login(request):
    blog_list = Blog.objects.all()
    username = request.POST.get('username',' ')
    password = request.POST.get('password',' ')
    users_ = [username]
    user = auth.authenticate(username = username,password = password)

    #if username == 'user' and password == '123456':
        #return HttpResponse('登录成功')
    #使用cookie保存信息
        # respone =HttpResponseRedirect('/blog/login_ok/')
        # respone.set_cookie('username',username,3600)#用户名cookie
        # return respone
    if user is not None:
        auth.login(request,user)#验证登录
    #使用session保存信息
        respone = HttpResponseRedirect('/blog/login_ok/')
        request.session['username'] = users_#username #将session信息写到服务器
        return respone
    else:
        return render_to_response('blog/index.html',{'error':'账号或密码错误','blogs':blog_list})

#登录成功
@login_required
def login_ok(request):
    blog_list = Blog.objects.all()
    #username = request.COOKIES.get('username',' ')#读取浏览器cookie

    username = request.session.get('username',' ') #读取用户session
    user = username[0]
    return render_to_response('blog/login_ok.html',{'user':user,'blog_list':blog_list})

#退出登录
@login_required
def logout(request):
    respone = HttpResponseRedirect('/blog/index/')#返回首页
    #respone.delete_cookie('username')#清理cookie里保存的username

    del request.session['username'] #清理用户session
    return respone

#学生表
def student(request):
    student = {
                'jack':[22,'boy','programmer'],
                'Haae': [17, 'girl', 'Designer'],
                'Brrs': [29, 'boy', 'Teacher'],
                'Kipp': [28, 'girl', 'Tester'],
                'Onsn': [20, 'boy', 'Fuck'],
    }
    return render_to_response('student/student.html', {'student_list':student})

#图书表
def SBook(request):
    books = Book.objects.all()
    return render_to_response('blog/book.html', {'book_list':books})

#分页
def page(request):
    file_list = Book.objects.all()
    paginator = Paginator(file_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('blog/book_page.html',{'pages':contacts})

#上传文件功能
def upload(request):
    files = File.objects.all()
    return render_to_response('blog/upload.html',{'file_list':files})

#执行文件上传
def upload_save(request):
    files = File.objects.all()
    filename = request.POST.get('filename','')
    fileing = request.FILES.get('fileing','')
    if filename==''or fileing=='':
        error = '文件与文件描述不能为空'
        return  render_to_response('blog/upload.html',{'error':error,'file_list':files})
    else:
        upload = File()
        upload.filename = filename
        upload.fileway = fileing
        upload.save()
        return render_to_response('blog/upload.html',{'upload_success':'上传文件成功','file_list':files})