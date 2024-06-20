from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from database import crud, models, schemas
from database.db import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url=None, redoc_url=None)


# 依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/user', status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    result = crud.create_user(db=db, user=user)
    if isinstance(result, str):
        return_result = {"password": result}
    elif result:
        return_result = {"message": "User created successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Create User Failed.")
    return JSONResponse(return_result)


@app.put('/user', status_code=status.HTTP_200_OK)
def update_user(user: schemas.UserUpdate, db: Session = Depends(get_db)):
    result = crud.change_password(db=db, user=user)
    if isinstance(result, str):
        return_result = {"message": "Password changed successfully", "password": result}
    elif result:
        return_result = {"message": "Password changed successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Update User Failed.")
    return JSONResponse(return_result)


@app.get('/{route}', status_code=status.HTTP_301_MOVED_PERMANENTLY, include_in_schema=False)
def redirect(route: str, db: Session = Depends(get_db)):
    link_schema = schemas.ShortLinkBase(route=route)
    result = crud.get_short_link(db=db, link=link_schema)
    if result:
        return RedirectResponse(result.url)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found.")


@app.get('/shortlinks', status_code=status.HTTP_200_OK)
def get_short_links(user: schemas.UserAuth, db: Session = Depends(get_db)):
    result = crud.get_all_links(db=db, user=user)
    if result:
        return_result = {"short_links": result}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Get Short Links Failed.")
    return JSONResponse(return_result)


@app.post('/shortlink', status_code=status.HTTP_201_CREATED)
def create_short_link(link: schemas.ShortLinkCreate, db: Session = Depends(get_db)):
    result = crud.new_short_link(db=db, link=link)
    if result:
        return_result = {"message": "Short Link created successfully", "short_link": result}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Create Short Link Failed.")
    return JSONResponse(return_result)


@app.put('/shortlink', status_code=status.HTTP_200_OK)
def update_short_link(link: schemas.ShortLinkUpdate, db: Session = Depends(get_db)):
    result = crud.update_short_link(db=db, link=link)
    if result:
        return_result = {"message": "Short Link changed successfully", "short_link": result}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Update Short Link Failed.")
    return JSONResponse(return_result)


@app.delete('/shortlink', status_code=status.HTTP_200_OK)
def delete_short_link(link: schemas.ShortLinkBaseWithAuth, db: Session = Depends(get_db)):
    result = crud.delete_short_link(db=db, link=link)
    if result:
        return_result = {"message": "Short Link deleted successfully", "short_link": result}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Delete Short Link Failed.")
    return JSONResponse(return_result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
