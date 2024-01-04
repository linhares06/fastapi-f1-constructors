from pydantic import BaseModel

class ConstructorModel(BaseModel):
    """
    Pydantic model for representing an F1 constructor.

    Attributes:
    - _id (str): The unique identifier for the constructor.
    - constructorId (int): The constructor ID.
    - constructorRef (str): The reference name of the constructor.
    - name (str): The name of the constructor.
    - nationality (str): The nationality of the constructor.
    - url (str): The URL associated with the constructor.
    """
    _id: str
    constructorId: int
    constructorRef: str
    name: str
    nationality: str
    url: str

class ConstructorUpdateModel(BaseModel):
    """
    Pydantic model for updating an F1 constructor.

    Attributes:
    - _id (str): The unique identifier for the constructor.
    - constructorRef (str): The reference name of the constructor.
    - name (str): The updated name of the constructor.
    - nationality (str): The updated nationality of the constructor.
    - url (str): The updated URL associated with the constructor (optional).
    """
    _id: str
    constructorRef: str
    name: str
    nationality: str
    url: str