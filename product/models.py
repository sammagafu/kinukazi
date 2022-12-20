from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from django_resized import ResizedImageField

class Product(models.Model):
    productName = models.CharField(_("Product Name"),max_length=160)
    brand = models.CharField(_("Product Brand"),max_length=160,default="Caterpillar")
    slug = models.SlugField(_("slug"),editable=False,unique=True,null=False)
    industry = models.ForeignKey("industry.ProuctIndusty", verbose_name=_("Industry"), on_delete=models.SET_NULL,null=True,blank=True)
    subindustry = models.ManyToManyField("industry.ProductSemiIndusry")
    terms = models.TextField(_("Renting Terms"))
    descripton = models.TextField(_("Product description"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Daily Renting Price")
    created_at = models.DateTimeField(default=timezone.now,editable=False)
    modified_at = models.DateTimeField(blank=True,null=True)
    approved = models.BooleanField(default=False,verbose_name="Available for renting")

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.productName

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified_at = timezone.now()
        if not self.slug:
            self.slug = slugify(self.productName)
        self.slug = slugify(self.productName)
        return super().save()
        
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE,related_name="images")
    images = ResizedImageField(upload_to = 'product/images/%Y/%m/%d',verbose_name=_("Other Product Images"),size=[800, 900], crop=['middle', 'center'])
    cover = models.BooleanField(_("Set as cover"),default=False)

    def get_images(self):
        if self.images:
            return '' + self.images.url
        return ''

class ProductReview(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE)
    review = models.TextField(_("Product Review"))
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)

    class Meta:
        verbose_name = _("Product Review")
        verbose_name_plural = _("Product Reviews")

    def __str__(self):
        return self.name

class ProductRating(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("Product"), on_delete=models.CASCADE)
    rating = models.IntegerField()
    rater = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)

    class Meta:
        verbose_name = _("Product Rating")
        verbose_name_plural = _("Product Ratings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductRating_detail", kwargs={"pk": self.pk})

class ProductFeatures(models.Model):
    produtct = models.ForeignKey(Product, verbose_name=_(""), on_delete=models.CASCADE)
    specification = models.CharField(_("Specification"), max_length=160)
    value = models.CharField(_("Specification"), max_length=120)