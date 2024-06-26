import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = None

    def __dict__(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'update_at': self.update_at.isoformat(),
            'amenity name': None,
            'amenity descritpion': None,
        }

    def assign_id(self, id):
        id = self.id
        return id

    def __str__(self):
            return f"<{self.__class__.__name__} (id: {self.id} {self.__dict__})>"

    def save(self):
        self.updated_at = datetime.now()
        BaseModel.__dict__[self.id] = self

    def delete(self):
        if self.id in BaseModel.__dict__[self.id]:
            del BaseModel.__dict__[self.id]

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key is not "__class__":
                self.__dict__[key] = value
            self.save

    @classmethod
    def get_instances(cls):
        return [instance for instance in cls.__dict__ if isinstance(instance, cls)]