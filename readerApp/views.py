from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .models import Recommendation

from django.template import RequestContext, loader
# Create your views here.

def landingPage(request):
    article_list = Article.objects.order_by('pub_date')
    rangeForLoop = range(4)
    template = loader.get_template('readerApp/landingPage.html')
    context = RequestContext(request,{'article_list':article_list,'range':rangeForLoop})
    return HttpResponse(template.render(context))

def articlePage(request, article_id):
    
    #getting article details
    
    article = Article.objects.get(pk=article_id)
    title = article.title
    author = article.author
    pub_date = article.pub_date
    category = article.category
    text = article.text
    imageMain=article.imageMain
    rangeForLoop = range(4)
    
    #getting recommendations
    
    recommendations = Recommendation.objects.filter(ref_article=article_id).order_by('timestamp')[:4]
    recommendations_ids=[one_recommendation.recommendation_id for one_recommendation in recommendations]
    recommendedArticles = Article.objects.filter(pk__in=recommendations_ids)
    
    #setting context and rendering
    
    context = RequestContext(request,{'imageMain':imageMain,'title':title,'author':author,'pub_date':pub_date,'category':category,'text':text,'recommendations':recommendedArticles,'range':rangeForLoop})
    template = loader.get_template('readerApp/article.html')
    return HttpResponse(template.render(context))

