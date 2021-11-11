from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth  # 계정에 대한 권한


# 회원가입 기능
def signup(request):
    # POST 요청이 왔을 때, 입력한 두 비밀번호가 같으면 새로운 USER 만듦
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            )
            # 소셜로그인으로 가져온 정보를 다른 곳에 저장한다면 맨 뒤의 ModelBackend 부분을 수정
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # auth.login(request, user)  # 새 USER 생성하면 자동 로그인
            return redirect('/')
        else:  # 비밀번호 2개가 같지 않으면
            return render(request, 'accounts/signup.html')  # {% url 'signup' %}

    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'accounts/signup.html')

    '''
    form = UserCreationForm
    return render(request, 'signup.html', {'form':form})
    '''


# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 한다.
    if request.method == "POST":
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST["username"]
        password = request.POST["password"]

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:  # 존재X => 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})

    else:  # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
        return render(request, 'accounts/login.html')


# 로그아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃한다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'login.html')
