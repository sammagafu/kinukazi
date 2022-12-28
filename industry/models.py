from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django_resized import ResizedImageField



class ProuctIndusty(models.Model):
    categoryname = models.CharField(max_length=160)
    slug = models.SlugField(_("slug"),editable=False,unique=True,null=False,blank=False)
    created_at = models.DateTimeField(editable=False,auto_now_add=True)
    image = ResizedImageField(_("Avatar"),size=[300, 300], upload_to='machine/category',crop=['middle', 'center'],quality=90,blank=True,null=True)
    modified_at = models.DateTimeField(blank=True,null=True,editable=False)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Products Categories'

    def __str__(self):
        return self.categoryname

    def save(self):
        if not self.id:
            self.created = timezone.now()
        self.modified_at = timezone.now()
        self.slug = slugify(self.categoryname)
        return super().save()

class ProductSemiIndusry(models.Model):
    category = models.ForeignKey(ProuctIndusty, verbose_name=_("category"), on_delete=models.CASCADE,related_name="subcategory")
    subcategoryname = models.CharField(max_length=160)
    slug = models.SlugField(_("slug"),editable=False,unique=True)
    image = ResizedImageField(_("Avatar"),size=[300, 300], upload_to='machine/category',crop=['middle', 'center'],quality=90,blank=True,null=True)
    created_at = models.DateTimeField(editable=False,auto_now_add=True)
    modified_at = models.DateTimeField(blank=True,null=True,editable=False)

    class Meta:
        verbose_name = _("Product Sub-Category")
        verbose_name_plural = _("Products Sub-Categories")

    def __str__(self):
        return self.subcategoryname

    def save(self):
        if not self.id:
            self.created = timezone.now()
        self.modified_at = timezone.now()
        if not self.slug:
            self.slug = slugify(self.subcategoryname)
        self.slug = slugify(self.subcategoryname)
        return super().save()