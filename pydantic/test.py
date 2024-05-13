from datetime import datetime
import json

from pydantic import BaseModel, ValidationError


class Settler(BaseModel):
    id: int
    name: str
    lastname: str

class Village(BaseModel):
    id: int
    title: str
    foundation_date: datetime | None = None
    settlers: list[Settler] | None 


def main():
    external_data = {
        'id': 1,
        'title': 'Aculovka',
        'foundation_date': '1911-04-22 00:00',
        'settlers': [ 
            {
                'id': 1,
                'name': 'Vasia',
                'lastname': 'Petrov'
            },
            {
                'id': 2,
                'name': 'Maria',
                'lastname': 'Semenova'
            }
        ]
    }
    try:
        village = Village(**external_data)
        with open('village.json', 'w') as file:
            file.write(village.json())
        with open('village.json', 'r') as file:
            json_data = json.load(file)
            village_info = Village(**json_data)
            print(village_info)

    except ValidationError as e:
        print(e.json())


if __name__ == '__main__':
    main()

