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
    slug = models.SlugField(max_length=200, unique=True)
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

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(blogpost_connected=self).count()


class Customer(models.Model):
    username = models.CharField(max_length=50, default=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' - ' + self.last_name

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False


class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(News.title) + ', ' + self.blogpost_connected.title[:40]
