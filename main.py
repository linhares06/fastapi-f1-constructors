from fastapi import FastAPI
from app.api.routers import constructor

"""
Initialize the FormulaOneAPI application.
Creates a FastAPI instance and includes the 'constructor' router.
"""
app = FastAPI()
app.include_router(constructor.router)

"""
Run the FormulaOneAPI application.
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)