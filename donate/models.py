from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey


class GivePage(Page):
    give_statement = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('give_statement')
    ]
class InvestPage(Page):
    invest_statement = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('invest_statement')
    ]

class SocialPage(Page):
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class SocialPageGalleryImage(Orderable):
    page = ParentalKey(SocialPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class EntrepreneurPage(Page):
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class EntrepreneurPageGalleryImage(Orderable):
    page = ParentalKey(EntrepreneurPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]