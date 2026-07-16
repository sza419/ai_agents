from pydantic import BaseModel
import json
class SnackOrder(BaseModel):
    name: str = Field(min_length=)
    ingredients: list
    minutes: int
    is_hot: bool

raw_data = {
    "name": "тост с сыром", 
    "ingredients": ["хлеб", "сыр"],
    "minutes": 7,
    "is_hot": False
}
order = SnackOrder.model_validate(raw_data)

for i in raw_data:
    print(raw_data[i])

