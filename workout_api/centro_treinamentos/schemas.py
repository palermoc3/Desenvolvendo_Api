from typing import Annotated
from pydantic import Field

from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example ='maracana', max_length=20)]
    endereco: Annotated[str, Field(description='Nome do endereco', example ='rua dos bobos', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario', example ='adriano', max_length=30)]