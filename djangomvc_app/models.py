from django.db import models

class Message(models.Model):
    content = models.TextField()
    
    @classmethod
    def get_default_message(cls):
        return cls.objects.first() or cls.objects.create(content="""Hi! My name is Maxie, 224205379.
The page you are seeing is a simple Django app, serving static content.
I have implemented this in Django's MVC Architecture, you can access the project here:
 https://github.com/maxwellc21/sit727_djangomvc.git""")

    def __str__(self):
        return self.content[:50] + "..." if len(self.content) > 50 else self.content