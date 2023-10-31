from pydantic import BaseModel, EmailStr

# defining schemas for validations
class user(BaseModel):
    name:str
    email:EmailStr
    phone:str
    issuperuser:bool
    password: str