from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse


class PostSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.8

	def items(self):
		return Post.objects.filter(status=1)

	def lastmod(self, obj):
		return obj.updated_on

	#def location(self, item):
	#	return reverse(item)