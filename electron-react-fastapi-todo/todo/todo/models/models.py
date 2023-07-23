from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Todo(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    completed = fields.BooleanField(default=False)


TodoPydantic = pydantic_model_creator(Todo, name="Todo")
TodoInPydantic = pydantic_model_creator(Todo, name="TodoIn", exclude_readonly=False)