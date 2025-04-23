
from pydantic import BaseModel

class StudentInsertDTO(BaseModel):
    name: str
    apelido: str
    
    



    