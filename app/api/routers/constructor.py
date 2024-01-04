from app.core.database import FormulaOneDatabase
from fastapi import APIRouter, HTTPException
from app.api.models.constructor import ConstructorModel, ConstructorUpdateModel
from pymongo.errors import DuplicateKeyError

# Constant for the name of the constructor collection on formulaone database
CONTRUCTORS_COLLECTION = 'constructors'

router = APIRouter()
formula_one = FormulaOneDatabase()

@router.get('/api/v1/constructors/', response_model=list[ConstructorModel])
def get_constructors():
    """
    Retrieve a list of F1 constructors.

    Returns:
    - List[ConstructorModel]: A list of F1 constructors.
    """
    
    constructors = formula_one.db[CONTRUCTORS_COLLECTION].find()

    return constructors

@router.get('/api/v1/constructors/{constructor_id}', response_model=ConstructorModel)
def get_constructor(constructor_id: int):
    """
    Retrieve information about a specific F1 constructor.

    Parameters:
    - constructor_id (int): The ID of the F1 constructor.

    Returns:
    - ConstructorModel: Information about the specified F1 constructor.

    Raises:
    - HTTPException: If the F1 constructor is not found (HTTP 404).
    """
    constructor = formula_one.db[CONTRUCTORS_COLLECTION].find_one({'constructorId': constructor_id})

    if not constructor:
        raise HTTPException(status_code=404, detail='Constructor not found')
    
    return constructor

@router.post('/api/v1/constructors/')
def create_constructor(constructor: ConstructorModel):
    """
    Create a new F1 constructor.

    Parameters:
    - constructor (ConstructorModel): The data for creating a new F1 constructor.

    Returns:
    - dict: The created F1 constructor.

    Raises:
    - HTTPException: If a duplicate key violation occurs (HTTP 400).
    """
    try:
        result = formula_one.db[CONTRUCTORS_COLLECTION].insert_one(constructor.model_dump())
        created_constructor = formula_one.db[CONTRUCTORS_COLLECTION].find_one({'_id': result.inserted_id}, {'_id': 0})

        return created_constructor

    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail='Duplicate key for "constructorId" violation')
    
@router.put('/api/v1/constructors/{constructor_id}')
def update_constructor(constructor_id: int, constructorModel: ConstructorUpdateModel):
    """
    Update information about a specific F1 constructor.

    Parameters:
    - constructor_id (int): The ID of the F1 constructor to be updated.
    - constructorModel (ConstructorUpdateModel): The data for updating the F1 constructor.

    Returns:
    - dict: The updated F1 constructor.

    Raises:
    - HTTPException: If the F1 constructor is not found (HTTP 404).
    """
    result = formula_one.db[CONTRUCTORS_COLLECTION].update_one({'constructorId': constructor_id}, {"$set": constructorModel.model_dump()})

    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail='Constructor not found')
    
    updated_constructor = formula_one.db[CONTRUCTORS_COLLECTION].find_one({'constructorId': constructor_id}, {'_id': 0})

    return updated_constructor

@router.delete('/api/v1/constructors/{constructor_id}')
def delete_item(constructor_id: int):
    """
    Delete a specific constructor.

    Parameters:
    - constructor_id (int): The ID of the constructor F1 to be deleted.

    Returns:
    - dict: A message indicating the success of the deletion.

    Raises:
    - HTTPException: If the F1 constructor is not found (HTTP 404).
    """
    result = formula_one.db[CONTRUCTORS_COLLECTION].delete_one({"constructorId": constructor_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Constructor not found')
    return {"message": "Constructor deleted successfully"}