from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_category():
        return Category.objects.all()


class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    @staticmethod
    def get_all_news():
        return News.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return News.objects.filter(category=category_id)
        else:
            return News.get_all_news()
