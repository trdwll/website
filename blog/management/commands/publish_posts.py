from django.core.management.base import BaseCommand, CommandError
from blog.models import Post

from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Updates the visibility of posts on the day that it should be public.'

    def handle(self, *args, **options):
        hours_behind = datetime.now() - timedelta(hours=5)
        hours_ahead = datetime.now() + timedelta(hours=5)

        # print('Current time: ', datetime.now())
        # print('Hours behind: ', hours_behind, '\nHours ahead: ', hours_ahead)

        posts = Post.objects.filter(is_published=False, published_date__gt=hours_behind, published_date__lt=hours_ahead)
        
        # print(posts)
        
        for post in posts:
            if post.published_date <= datetime.now():
                print('The post goes live!!!!!')

                post.is_published = True
                post.save()
            # else:
            #     print('The published_date of post is: ', post.published_date, ' the current time is: ', datetime.now())
