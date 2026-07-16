from pydantic import BaseModel, Field
import json
from pydantic import ValidationError

class SnackOrder(BaseModel):
    name: str = Field(min_length=1)
    ingredients: list = Field(min_length=1)
    minutes: int = Field(ge=1, le=60)
    is_hot: bool

normal_order = {
    "name": "тост с сыром",
    "ingredients": ["хлеб", "сыр"],
    "minutes": 7,
    "is_hot": True
}
SnackOrder.model_validate(normal_order)

empty_order = {
    "name": "",
    "ingredients": [],
    "minutes": ...,
    "is_hot": ...
}
'''
Данные не прошли проверку
String should have at least 1 character [type=string_too_short, input_value='', input_type=str]
ingredients
  List should have at least 1 item after validation, not 0 [type=too_short, input_value=[], input_type=list
minutes
  Input should be a valid integer [type=int_type, input_value=Ellipsis, input_type=ellipsis
is_hot
  Input should be a valid boolean [type=bool_type, input_value=Ellipsis, input_type=ellipsis]
'''
SnackOrder.model_validate(empty_order)
big_order = {
    "name": "тост с сыром",
    "ingredients": ["хлеб", "сыр"],
    "minutes": 500,
    "is_hot": True
}
SnackOrder.model_validate(big_order)
'''
Данные не прошли проверку
minutes
  Input should be less than or equal to 60 [type=less_than_equal, input_value=500, input_type=int]
'''