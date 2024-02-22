from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import Optional
from . import schemas, models, database
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db 
    finally:
        db.close()


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# request params
@app.get("/users/{id}")
def show(id: int, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"User with the id {id} is not available"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available"
        )
    return user

#request body
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name, 
        gender=request.gender, 
        age=request.age,
        city=request.city
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.id == id).delete(
        synchronize_session=False
    )
    db.commit()
    return 'Deleted Successfully'

@app.put("/users/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.User, db: Session = Depends(get_db)):
    blog = db.query(models.User).filter(models.User.id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available"
        )
    blog.update(request, synchronize_session=False)
    db.commit()
    return 'Updated Successfully'