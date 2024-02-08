import sys,os
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import WeaponData, ItemType



def item_list(request, wd_type=None):
    # WeaponData을 통해 ItemType에 연결된 모든 항목 가져오기
    weapon = WeaponData.objects.select_related('it_pk').get(pk=3)
    item_type = weapon.it_pk
    print(item_type.query)# WeaponData와 연결된 ItemType 객체
    print(item_type)
    wd_type = '검'
    if wd_type is None:
        # wd_type이 제공되지 않은 경우 모든 무기를 가져옵니다.
        weapon_list = WeaponData.objects.all()
    else:
        # wd_type에 해당하는 무기만 가져옵니다.
        weapon_list = WeaponData.objects.filter(wd_type=wd_type)

    context = {'weapon_list': weapon_list}
    return render(request, 'asfo/item_list.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

