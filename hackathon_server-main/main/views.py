from django.shortcuts import render
# View에 Model(Post 게시글) 가져오기
from .api import check_space

# index.html 페이지를 부르는 index 함수
def index(request):
    #t1 = check_space()
    
    datas = check_space()
    context = {"datas": list(datas.values())}
    return render(request, 'main/index.html', context)

