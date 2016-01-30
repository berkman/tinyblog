tinyblog

A tiny blog written in Python leveraging Django/Bootstrap/Postgres and built to run on Heroku






cli examples:
    from main.models import Post, Comment
    from django.utils import timezone
    from django.contrib.auth.models import User

    u = User.objects.get(pk=1)
    p = Post.objects.get(pk=1)

    p.comment_set.create(comment='you suck!', user=u, comment_pub=timezone.now())
