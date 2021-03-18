from django.shortcuts import render
from blog.models import BlogPost, Tag
from django.http import HttpResponseRedirect
from blog.forms import ContactForm, CommentForm
from config.settings import HCAPTCHA_SECRET_KEY, CONTACT_EMAIL
from django.contrib import messages
from django.core.mail import send_mail
import json, urllib.request

def check_hcaptcha(token):
    """hCaptcha validation"""
    # set API endpoint. this expects a POST request with two parameters:
    # the secret key and the h-captcha-response token.
    VERIFY_URL = "https://hcaptcha.com/siteverify"
    
    # set the secret key
    values = {
        'secret': HCAPTCHA_SECRET_KEY,
        'response': token
    }
    # encode the data as a POST 
    data = urllib.parse.urlencode(values).encode()
    # send the POST request to hcaptcha's api endpoint
    req = urllib.request.Request(VERIFY_URL, data=data)
    # open and parse the response
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    # return the result
    return result


def home(request):
    """
    Render the home page.
    """
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')[:5]

    context = {
        "blog_posts": blog_posts,
    }

    return render(request, 'home.html', context)


def posts(request):
    """
    Render list of all blog posts.
    """
    query = request.GET.get('q')

    if query is not None:
        blog_posts = BlogPost.objects.filter(title__icontains=query).filter(is_published=True)
    else:
        blog_posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')
    
    context = {
        "blog_posts": blog_posts,
    }
    return render(request, 'posts.html', context)


def detail(request, slug):
    """
    Render the content of a blog post.
    """
    post = BlogPost.objects.get(slug=slug)
    comments = post.comment_set.filter(is_approved=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            # get the response token, then check whether it's valid
            token = request.POST.get('h-captcha-response')
            result = check_hcaptcha(token)

            if result['success']:
                # save comment to db
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
                # email contact
                sender = comment_form.cleaned_data['name']
                email = comment_form.cleaned_data['email']
                message = comment_form.cleaned_data['body']
                send_mail(
                    subject="New comment",
                    message=message, 
                    from_email=email,
                    recipient_list=[CONTACT_EMAIL]
                )
                return HttpResponseRedirect('/comment/')

            else:
                messages.error(request, 'Invalid captcha. Please try again.')

        else:
            messages.error(request, 'Sorry, the form is invalid.')

    elif request.method == 'GET':
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        "new_comment": new_comment,
    }

    return render(request, 'detail.html', context)


def tag(request, tag):
    """
    Return all blog posts associated with a given tag.
    """
    blog_posts = BlogPost.objects.filter(
        tags__name = tag
    ).order_by(
        '-published_date'
    )
    tags = Tag.objects.all()
    context = {
        "tag": tag,
        "blog_posts": blog_posts,
    }
    return render(request, "tag.html", context)


def contact(request):
    """
    Render the contact form for GET and POST requests.
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

        if form.is_valid():
            # get the response token, then check whether it's valid
            token = request.POST.get('h-captcha-response')
            result = check_hcaptcha(token)

            if result['success']:

                # process the data in form.cleaned_data as required
                sender = form.cleaned_data['name'] # not used.. TODO: append to message?
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                cc = form.cleaned_data['cc']

                # send to contact email
                send_mail(
                    subject=subject,
                    message=message, 
                    from_email=email,
                    recipient_list=[CONTACT_EMAIL]
                )

                # forward copy to sender if they want                
                if cc: 
                    send_mail(
                        subject="Thanks for contacting heds.nz",
                        message='<p>I will be in touch as soon as possible. Your message is displayed below.</p><p color=#6c757d>' + message + '</p>',
                        from_email=CONTACT_EMAIL,
                        recipient_list=[email]
                    )

                # redirect to a new URL:
                return HttpResponseRedirect('/thanks')

            else:
                messages.error(request, 'Invalid captcha. Please try again.')

    elif request.method == 'GET':
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, 'contact.html', context)


def privacy(request):
    return render(request, 'privacy.html')


def thanks(request):
    return render(request, 'thanks.html')


def comment(request):
    return render(request, 'comment.html')
