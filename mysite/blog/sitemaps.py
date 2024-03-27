from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'  # each of this property can be a function
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated

    # def location(self, obj):
    #     return obj.get_absolute_url() calls get_absolute_url() by default