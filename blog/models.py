from django.db import models

from django.forms import ModelForm
# Create your models here.

class Tag(models.Model):
    title    = models.CharField(max_length=200, unique=True)
    slug     = models.SlugField(max_length=200, unique=True)
    weight   = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title

class Article(models.Model):
    title    = models.CharField(max_length=200)
    content  = models.TextField()
    tags     = models.ManyToManyField(Tag, blank=True, null=True, related_name="tags")
    datetime = models.DateTimeField()
    
    def get_tags(self):
        return "\n".join([t.title for t in self.tags.all()])
    
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    user       = models.CharField(max_length=200)
    email      = models.EmailField(blank=True)
    website    = models.URLField(max_length=200, blank=True)
    ip         = models.IPAddressField(blank=True)
    content    = models.TextField()
    to_article = models.ForeignKey(Article, blank=True, null=True)
    to_comment = models.ForeignKey('self',  blank=True, null=True, limit_choices_to={'to_comment__isnull':True,
                                                                                     })
    datetime   = models.DateTimeField(blank=True)
    approved   = models.BooleanField(blank=True, default=True)
    
    def __unicode__(self):
        if self.to_comment == None:
            return u"[%s] to article [%s]" % (self.user, self.to_article)
        else:
            return u"[%s] to comment {%s}" % (self.user, self.to_comment)



class CommentForm(ModelForm):
    class Meta:
        model  = Comment
        fields = ['user', 'email', 'website', 'ip', 'content', 'to_article', 'to_comment', 'datetime']















