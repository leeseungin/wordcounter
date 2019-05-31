from django.shortcuts import render
import random
import string

# Create your views here.
def home(request):
    return render(request, 'home.html') 
# home.html을 렌더링을 부탁하는 것.
def about(request):
    return render(request, 'about.html') 

def count(request):
    full_text = request.GET['fulltext']
#숫자 카운팅하는 코드를 다음과 같이 작성한다. 
    word_list = full_text.split()#전체 텍스트를 스페이스로 나눔
    word_dic = {}#사전형 변수에 해당

    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1

        else :
            word_dic[word] = 1   

# 위에 fulltext라는 이름의  home.html 에서 넘어오는 데이터를 받는 명령어에 해당한다.  get 방식은 str형식으로 받는다. 
    return render(request, 'count.html', {'fulltext' : full_text,
                                            'total' : len(word_list),
                                            'dictionary' : word_dic.items()}) 
# 위 명령어를 통해서 다시 count.html 로 데이터를 쏴주는 명령어에 해당한다. 
# (3) html쪽으로 보내야 할 정보들, => 딕셔너리 자료형으로 보내야 한다. 

def select(request):
    #로또 번호 추출하는 코드
    lotterynumbers = []
    x = 0

    while x < 6:
        lotterynumbers.append(random.randint(1, 45))
        x += 1

    lotterynumbers.sort()
    print(lotterynumbers)

    _LENGTH = 10 # 10자리
    string_pool = string.ascii_lowercase # 소문자
    result = "" # 결과 값
    for i in range(_LENGTH) :
        result += random.choice(string_pool) # 랜덤한 문자열 하나 선택
    print(result)

    return render(request, 'home.html', {'lotterynumbers':lotterynumbers, 'result':result})
# (3) lotterynumbers의 값을 lotterynumbers라는 이름으로 보낸다. 


# def home(request):
#     blogs = Blog.objects.all().order_by(-)
#해당 명령어를 통해서 불러올 때 --순으로 정렬하여 가져온다. 




# #C - new
# def new(request):
#     return render(request, )


# # C - create
# def create(request):
#     blog = Blog()
# # 다음과 같은 변수에 다음 객체를 담아오겠다.
#     blog.title = request.GET['title']
# # request.GET 명령어로 해당 파일에 특정 내용을 가져오는 것이 가능하다. , title의 내용을 가져온다ㅏ. 
#     blog.body = request.GET['body']
#     blog.pub_date = timezone.datetime.now()
# #붕어빵 속을 다 채웠다. 
#     blog.save()

#     return redirect('/blog/' + str(blog.id))
# #redirenct : url 을 만들어서 해당 url로 페이지를 돌려보낸다.  기본 함수가 아니라서 import를 해줘야 함을 유의한다. 







# #U - edit
# def edit(request,blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)#블로그라는 객체를 가져온다. 
#     return render(request, 'edit.html', {'blog':blog})
#     #해당 요청이 들어오면 render라는 함수를 통해서 edit.html 파일을 띄워줘라.     
# #d이후 url.py에서 변수를 지정하여 준다. 
# #->path('blog/edit/<int:blog_id>', blog.views.edit, name="eidt")
# #<int:blog_id> 는 일종의 매게변수....



# # C - update : 글이 업데이트 되는 동작
# def create(request):
#     blog = get_object_or_404(Blog, pk=blog_id) ->pk는 primary key...
# # 다음과 같은 변수에 다음 객체를 담아오겠다.
#     blog.title = request.GET['title']
# # request.GET 명령어로 해당 파일에 특정 내용을 가져오는 것이 가능하다. , title의 내용을 가져온다ㅏ. 
#     blog.body = request.GET['body']
#     blog.pub_date = timezone.datetime.now()
# #붕어빵 속을 다 채웠다. 
#     blog.save()

#     return redirect('/blog/' + str(blog.id))
# #redirenct : url 을 만들어서 해당 url로 페이지를 돌려보낸다.  기본 함수가 아니라서 import를 해줘야 함을 유의한다. 


