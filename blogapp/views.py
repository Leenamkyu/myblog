from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 새 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 (request 페이즈를 변수에 담아내고) 
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다. 
    posts = paginator.get_page(page)

    return render(request, 'home.html',{'blogs':blogs, 'posts': posts})

def details(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk= blog_id)    
    return render(request, 'details.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')    

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body  = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    #url은 무조건 문자열이여야 한다. blog_id가 기존에 int형이였기에 형변환을 진행함
    
    #render와 redirect의 차이
      #redirect는 인자로 url을 넣는다. => 우리 프로젝트 외의 페이지까지 접근/연결할 수 있다.
      #render는 3번째 인자로 dictionary(키:값)을 받는다 => views의 함수 안에서 지지고 볶은 데이터를
      #우리가 설계한 html 페이지에서 사용하고 싶을 때 사용한다 
      # 즉, 인자에 따라 구분하여 사용 

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit =False) 
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')      
     #2. 빈 페이지를 띄워주는 기능 ->   GET          
    else:
        form = BlogPost()     
        return render(request, 'new.html', {'form':form})        
