from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Honbab ,Like



@login_required
def resturant_like(request,pk):
    resturant = get_object_or_404(Honbab, pk=pk)
  # 중간자 모델 Like 를 사용하여, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다.
    resturant_like, resturant_like_created = resturant.like_set.get_or_create(user=request.user)

    if not resturant_like_created:
        resturant_like.delete()

    return redirect('Honbab:main') 

def index(request):
    sort = request.GET.get('sort','')
    if sort == 'Likes':
        honbab = Honbab.objects.order_by('-like_user_set')
        return render(request, 'Honbab/Honbab.html', {'Honbab' : honbab})
    else:
        honbab = Honbab.objects.order_by('level')
        return render(request, 'Honbab/Honbab.html', {'Honbab' : honbab})