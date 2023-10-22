from datetime import datetime
from mongoengine import Document, StringField, DateTimeField



class Task(Document):
    key = StringField(required=True, max_length=50)
    value = StringField(required=True, max_length=100)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)


    def save(self, *args, **kwargs):
        # Set created_at and updated_at timestamps
        if not self.created_at:
            self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        super(Task, self).save(*args, **kwargs)