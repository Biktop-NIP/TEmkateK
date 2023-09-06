from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import Video, Genre, TegType, Tag, Comment
from .forms import SearchForm, CommentCreateForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


class Genre_list(ListView):
    model = Genre
    template_name = 'videos/genres.html'
    context_object_name = 'genres'
    

class Teg_list(ListView):
    model = TegType
    template_name = 'videos/tegs.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querySet = []
        teg_types = TegType.objects.all()
        for teg_type in teg_types:
            tags = Tag.objects.filter(tag_type_id=teg_type.pk)
            querySet.append((teg_type.name,tags))
        context['teg_types'] = querySet
        return context
    
    
class Video_detail(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    extra_context = {'form': CommentCreateForm()}
    context_object_name = 'video'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video'].views += 1
        context['video'].save()
        context['comments'] = Comment.objects.filter(video_id=self.kwargs['pk'])
        return context


@login_required
def dislike_video(request, pk):
    try:
        video = Video.objects.get(pk=pk)
        if request.user not in video.users_disliked.all():
            video.users_disliked.add(request.user)
            video.dis_likes += 1
            video.save()
        else:
            video.users_disliked.remove(request.user)
            video.dis_likes -= 1
            video.save()
        return JsonResponse({'status': '200', 'ok': True})
    except:
        return JsonResponse({'status': '505'})

@login_required
def like_video(request, pk):
    try:
        video = Video.objects.get(pk=pk)
        if request.user not in video.users_liked.all():
            video.users_liked.add(request.user)
            video.likes += 1
            video.save()
        else:
            video.users_liked.remove(request.user)
            video.likes -= 1
            video.save()
        return JsonResponse({'status': '200', 'ok': True})
    except:
        return JsonResponse({'status': '505'})
    
@login_required
def dislike_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
        if request.user not in comment.users_disliked.all():
            comment.users_disliked.add(request.user)
            comment.dis_likes += 1
            comment.save()
        else:
            comment.users_disliked.remove(request.user)
            comment.dis_likes -= 1
            comment.save()
        return JsonResponse({'status': '200', 'ok': True})
    except:
        return JsonResponse({'status': '505'})

@login_required
def like_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
        if request.user not in comment.users_liked.all():
            comment.users_liked.add(request.user)
            comment.likes += 1
            comment.save()
        else:
            comment.users_liked.remove(request.user)
            comment.likes -= 1
            comment.save()
        return JsonResponse({'status': '200', 'ok': True})
    except:
        return JsonResponse({'status': '505'})

@login_required
def add_comment(request, pk):
    form = CommentCreateForm({'text': request.GET['text'], 'video':pk, 'user':request.user.pk})
    if form.is_valid():
        form.save()
        return JsonResponse({'status': '200', 'ok': True})
    else:
        return JsonResponse({'status': '505'})


class Video_list(ListView):
    model = Video
    paginate_by = 10
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context
    
    def get_queryset(self):
        querySet = Video.objects.all()
        
        if self.request.method == 'GET':
            data = self.request.GET
            if 'search_text' in data and data['search_text'] != '':
                querySet = querySet.filter(Q(description__icontains=data['search_text']) | Q(name__icontains=data['search_text']))
            if 'sort_type' in data and data['sort_type'] != '':
                if data['sort_type'] == 'date':
                    querySet = querySet.order_by('data_add')
                elif data['sort_type'] == 'views':
                    querySet = querySet.order_by('-views')
                elif data['sort_type'] == 'rating':
                    querySet = querySet.extra(
                        select={'rating':'likes * 100 / (likes + dis_likes)'},
                        order_by=('-rating',)
                    )
            if 'tag' in data and data['tag'] != 'null':
                querySet = querySet.filter(tags=int(data['tag']))
                
            if 'genres' in data and data['genres'] != 'null':
                genres = data['genres']
                genres = genres.replace('[', '').replace(']', '').replace(' ', '').split(',')
                genres = list(map(int, genres))
                
                querySet = querySet.filter(genres__in=genres).distinct()
        
        
        return querySet

def cr():
    all = Video.objects.all()
    for v in all:
        v.pk = None
        v.save()