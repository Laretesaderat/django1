import re

from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from .models import Book

def books_list(request):
    books=Book.objects.order_by('date')
    return render(request, 'books/books_list.html', {'books': books})

class SearchView(View):
    template_name='books/search.html'
    def get(self,request):
        context={}
        q=request.GET.get('q')
        lines_raw=str({q})[2:-2]
        lines=lines_raw.split()
        if q:
            query=[]
            books=Book.objects.order_by('date')
            for book in books:
                for line in lines:
                    for genre in book.genres.all():
                        if re.search(line, str(genre)):
                            query.append(book)
                            break
                    for author in book.authors.all():
                        if re.search(line, str(author)):
                            query.append(book)
                            break
            query_new=[]
            for i in query:
                if i not in query_new:
                    query_new.append(i)
            context['last_question'] = '?q=%s' % q
            current_page = Paginator(query_new, 10)

            page = request.GET.get('page')
            try:
                context['object_list'] = current_page.page(page)
            except PageNotAnInteger:
                context['object_list'] = current_page.page(1)
            except EmptyPage:
                context['object_list'] = current_page.page(current_page.num_pages)
        return render(request=request, template_name=self.template_name, context=context)

