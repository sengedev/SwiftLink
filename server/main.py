from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.requests import Request
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from database import crud, models
from database.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
# app = FastAPI()
app = FastAPI(docs_url=None, redoc_url=None)

# Secure Authorization support
security = HTTPBasic()


# Database Depends
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/user', status_code=status.HTTP_200_OK)
async def authenticate_user(auth: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):
    result = crud.auth(db=db, username=auth.username, password=auth.password)
    """
    User Authentication
    :param auth: HTTPBasicCredentials
    :param db: Session
    :return: JSONResponse
    """
    if result is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not exists.")
    elif not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect.")
    else:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": f"Hello, {auth.username}"})


@app.post('/user', status_code=status.HTTP_200_OK)
async def create_user(auth: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):
    """
    User registration, only one user can be created.
    :param auth: HTTPBasicCredentials
    :param db: Session
    :return: JSONResponse
    """
    result = crud.create_user(db=db, username=auth.username, password=auth.password)
    status_code = result['code']
    if status_code == 200:
        return JSONResponse(status_code=status_code, content={"message": result['message']})
    elif status_code == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result['message'])
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=result['message'])


@app.put('/user', status_code=status.HTTP_200_OK)
async def update_user(auth: Annotated[HTTPBasicCredentials, Depends(security)], request: Request,
                db: Session = Depends(get_db)):
    """
    Change user password
    :param auth: HTTPBasicCredentials
    :param request: Request
    :param db: Session
    :return: JSONResponse
    """
    new_password = request.headers.get('new-password')
    result = crud.change_password(db=db, username=auth.username, password=auth.password, new_password=new_password)
    status_code = result['code']
    if status_code == 200:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": result['message']})
    elif status_code == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result['message'])
    elif status_code == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result['message'])
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=result['message'])


@app.post('/shortlink', status_code=status.HTTP_200_OK)
async def create_short_link(auth: Annotated[HTTPBasicCredentials, Depends(security)], route: str, url: str,
                      db: Session = Depends(get_db)):
    """
    Create a short link
    :param auth: HTTPBasicCredentials
    :param route: str
    :param url: str
    :param db: Session
    :return: JSONResponse
    """
    result = crud.new_short_link(db=db, username=auth.username, password=auth.password, route=route, url=url)
    if result['code'] == 200:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": result['message']})
    elif result['code'] == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result['message'])
    elif result['code'] == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result['message'])
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=result['message'])


@app.put('/shortlink', status_code=status.HTTP_200_OK)
async def update_short_link(auth: Annotated[HTTPBasicCredentials, Depends(security)], route: str, new_route: str = False,
                      new_url: str = False, db: Session = Depends(get_db)):
    """
    Update a short link
    :param auth: HTTPBasicCredentials
    :param route: str
    :param new_route: str
    :param new_url: str
    :param db: Session
    :return: JSONResponse
    """
    result = crud.update_short_link(db=db, username=auth.username, password=auth.password, route=route,
                                    new_route=new_route, new_url=new_url)
    if result['code'] == 200:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": result['message']})
    elif result['code'] == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result['message'])
    elif result['code'] == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result['message'])
    elif result['code'] == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result['message'])
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=result['message'])


@app.delete('/shortlink', status_code=status.HTTP_200_OK)
async def delete_short_link(auth: Annotated[HTTPBasicCredentials, Depends(security)], route: str,
                      db: Session = Depends(get_db)):
    """
    Delete a short link
    :param auth: HTTPBasicCredentials
    :param route: str
    :param db: Session
    :return: JSONResponse
    """
    result = crud.delete_short_link(db=db, username=auth.username, password=auth.password, route=route)
    if result['code'] == 200:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": result['message']})
    elif result['code'] == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result['message'])
    elif result['code'] == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result['message'])
    elif result['code'] == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result['message'])
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=result['message'])


@app.get('/shortlinks', status_code=status.HTTP_200_OK)
async def get_shortlinks(auth: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):
    """
    Get all short links
    :param auth: HTTPBasicCredentials
    :param db: Session
    :return: JSONResponse
    """
    result = crud.get_all_links(db=db, username=auth.username, password=auth.password)
    if result['code'] == 200:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": result['message'], "short_links": result['data']})
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result['message'])


@app.get('/{route}', status_code=status.HTTP_301_MOVED_PERMANENTLY, include_in_schema=False)
async def redirect_short_link(route: str, db: Session = Depends(get_db)):
    """
    Redirect to the original link
    :param route: str
    :param db: Session
    :return: RedirectResponse
    """
    result = crud.get_short_link(db=db, route=route)
    if result:
        return RedirectResponse(status_code=status.HTTP_301_MOVED_PERMANENTLY, url=result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short link not found")
