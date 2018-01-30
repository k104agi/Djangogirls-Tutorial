from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
# 1 브라우저에서 요청
# 2 요청이 runserver로 실행중인 서버로 도착
# 3 runserver는 요청을 Django code로 전달
# 4 Django code 중 config.urls 모듈이 해당 요청을 받음
# 5 config.urls 모듈은 ''(admin/를 제외한 모든 요청)을 blog.urls 모듈로 전달
# 6 blog.urls 모듈은 받은 요청의 url과 일치하는 패턴이 있는지 검사함
# 7 있다면 일치하는 패턴과 연결된 함수(view)를 실행
# 8 함수의 실행 결과(리턴값)을 브라우저로 다시 전달
# HTTP 프로토콜로 텍스트 데이터 응답을 변환
    #return HttpResponse('Post list') 는 아래와 같음
    return render(request, 'blog/post_list.html')
