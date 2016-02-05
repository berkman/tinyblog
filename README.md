# tinyblog

A tiny blog written in Python leveraging Django/Bootstrap/Postgres and built to run on Heroku


cli examples:
<pre><code>from tinyblog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User

u = User.objects.get(pk=1)
p = Post.objects.get(pk=1)

p.comment_set.create(comment='you suck!', user=u, comment_pub=timezone.now())</code></pre>

Database:
edit the DATABASE_URL variable in .env to point to your local Postgres DB
<pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

Start the local webserver:
<pre><code>heroku local web</code></pre>

### Create an admin user
<pre><code>python manage.py createsuperuser</code></pre>
