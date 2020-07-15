from django.shortcuts import render
posts = [
    {
        'organization': 'analog',
        'agenda': 'Notes 1',
        'author': 'CoreyMS',
        'attendance': 'All',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'organization': 'analog',
        'agenda': 'Notes 2',
        'author': 'Jane Doe',
        'attendance': 'Viv, Mike, Kim',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'Mynotes/home.html', context)


def about(request):
    return render(request, 'Mynotes/about.html', {'title': 'About'})