# -*- coding: utf-8 -*-
# Create your views here.
#from django.template.loader import get_template
#from django.template import Template, Context
#from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.utils import timezone
from board.models import DjangoBoard
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.db.models import Q
# from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

# from board.pagingHelper import pagingHelper
#from django.core.urlresolvers import reverse

# 한글!!
#===========================================================================================
rowsPerPage = 6


def home(request):
    #OK
    #url = '/listSpecificPageWork?current_page=1'
    #return HttpResponseRedirect(url)

    boardList = DjangoBoard.objects.order_by('-id')[0:10]
    current_page =1
    totalCnt = DjangoBoard.objects.all().count()

    # pagingHelperIns = pagingHelper();
    # totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)
    # print('totalPageList', totalPageList)

    # return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
    #                                                     'current_page':current_page ,'totalPageList':totalPageList} )
    craftposts = DjangoBoard.objects.filter(
        created_date__lte=timezone.now()).order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(craftposts, 6)
    try:
        craftposts = paginator.page(page)
    except PageNotAnInteger:
        craftposts = paginator.page(1)
    except EmptyPage:
        craftposts = paginator.page(paginator.num_pages)

    boardList1 = DjangoBoard.objects.active()
    query = request.GET.get("searchStr")
    if query:
        boardList = boardList1.filter(Q(subject__icontains=query) | Q(name__icontains=query) | Q(memo__icontains=query)).distinct()
    paginator = Paginator(boardList1, 2)
    return render(request, 'listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                                        'current_page':current_page,'craftposts': craftposts} )

#===========================================================================================
def show_write_form(request):
    return render(request, 'writeBoard.html')

#===========================================================================================
@csrf_exempt
def DoWriteBoard(request):
    br = DjangoBoard (subject = request.POST['subject'],
                      name = request.POST['name'],
                      mail = request.POST['email'],
                      memo = request.POST['memo'],
                      created_date = timezone.now(),
                      hits = 0
                     )
    br.save()

    # 다시 조회
    url = '/board?current_page=1'
    return HttpResponseRedirect(url)


#===========================================================================================
def viewWork(request):
    pk= request.GET['memo_id']
    #print 'pk='+ pk
    boardData = DjangoBoard.objects.get(id=pk)
    #print boardData.memo

    # Update DataBase
    print('boardData.hits', boardData.hits)
    DjangoBoard.objects.filter(id=pk).update(hits = boardData.hits + 1)

    return render(request, 'viewMemo.html', {'memo_id': request.GET['memo_id'],
                                                'current_page':request.GET['current_page'],
                                                'searchStr': request.GET['searchStr'],
                                                'boardData': boardData } )

#===========================================================================================
# def listSpecificPageWork(request):
#     current_page = request.GET['current_page']
#     totalCnt = DjangoBoard.objects.all().count()
#
#     print('current_page=', current_page)
#
#     # 페이지를 가지고 범위 데이터를 조회한다 => raw SQL 사용함
#     boardList = DjangoBoard.objects.raw('SELECT Z.* FROM(SELECT X.*, ceil( rownum / %s ) as page FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS \
#                                         FROM BOARD_DJANGOBOARD  ORDER BY ID DESC ) X ) Z WHERE page = %s', [rowsPerPage, current_page])
#
#     print('boardList=',boardList, 'count()=', totalCnt)

    # 전체 페이지를 구해서 전달...
    # pagingHelperIns = pagingHelper();
    #
    # totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)

    # print('totalPageList', totalPageList)
    #
    # return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
    #                                                     'current_page':int(current_page)} )

#===========================================================================================

def listSpecificPageWork_to_update(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    searchStr = request.GET['searchStr']

    #totalCnt = DjangoBoard.objects.all().count()
    print('memo_id', memo_id)
    print('current_page', current_page)
    print('searchStr', searchStr)

    boardData = DjangoBoard.objects.get(id=memo_id)

    return render(request, 'viewForUpdate.html', {'memo_id': request.GET['memo_id'],
                                                'current_page':request.GET['current_page'],
                                                'searchStr': request.GET['searchStr'],
                                                'boardData': boardData } )

#===========================================================================================
@csrf_exempt
def updateBoard(request):
    memo_id = request.POST['memo_id']
    current_page = request.POST['current_page']
    searchStr = request.POST['searchStr']

    print('#### updateBoard ######')
    print('memo_id', memo_id)
    print('current_page', current_page)
    print('searchStr', searchStr)

    # Update DataBase
    DjangoBoard.objects.filter(id=memo_id).update(
                                                  mail= request.POST['mail'],
                                                  subject= request.POST['subject'],
                                                  memo= request.POST['memo']
                                                  )

    # Display Page => POST 요청은 redirection!
    url = '/board?current_page=' + str(current_page)
    return HttpResponseRedirect(url)


#===========================================================================================
def DeleteSpecificRow(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    print('#### DeleteSpecificRow ######')
    print('memo_id', memo_id)
    print('current_page', current_page)

    p = DjangoBoard.objects.get(id=memo_id)
    p.delete()

    # Display Page
    # 마지막 메모를 삭제하는 경우, 페이지를 하나 줄임.
    # totalCnt = DjangoBoard.objects.all().count()
    # pagingHelperIns = pagingHelper();
    #
    # totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
    # print('totalPages', totalPageList)

    # if( int(current_page) in totalPageList):
    #     print('current_page No Change')
    #     current_page=current_page
    # else:
    #     current_page= int(current_page)-1
    #     print('current_page--')

    url = '/board?current_page=' + str(current_page)
    return HttpResponseRedirect(url)

#===========================================================================================
@csrf_exempt
def searchWithSubject(request):
    searchStr = request.POST['searchStr']
    print('searchStr', searchStr)

    url = '/board?searchStr=' + searchStr +'&pageForView=1'
    return HttpResponseRedirect(url)



def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'list.html', {'contacts': contacts})

#===========================================================================================
# def listSearchedSpecificPageWork(request):
#     searchStr = request.GET['searchStr']
#     pageForView = request.GET['pageForView']
#     print('listSearchedSpecificPageWork:searchStr', searchStr, 'pageForView=', pageForView)
#
#     #boardList = DjangoBoard.objects.filter(subject__contains=searchStr)
#     #print  'boardList=',boardList
#
#     totalCnt = DjangoBoard.objects.filter(subject__contains=searchStr).count()
#     print('totalCnt=',totalCnt)
#
#     # pagingHelperIns = pagingHelper();
#     # totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
#
#     # like 구문 적용방법
#     boardList = DjangoBoard.objects.raw("""SELECT Z.* FROM ( SELECT X.*, ceil(rownum / %s) as page \
#         FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS FROM BOARD_DJANGOBOARD \
#         WHERE SUBJECT LIKE '%%'||%s||'%%' ORDER BY ID DESC) X ) Z WHERE page = %s""", [rowsPerPage, searchStr, pageForView])
#
#     print('boardList=',boardList)
#
#     return render_to_response('listSearchedSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
#                                                         'pageForView':int(pageForView) ,'searchStr':searchStr} )

#===========================================================================================
