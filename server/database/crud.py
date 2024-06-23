from sqlalchemy.orm import Session
from database import models
from security.password import Password


def create_user(db: Session, username: str, password: str = None):
    # 判断是否有用户（只允许一个用户）
    user_count = db.query(models.User).count()
    if user_count > 0:
        return {
            "code": 400,
            "message": "Only one user is allowed."
        }
    p = Password()
    message = "User created successfully."
    if not password:
        password = p.generate(length=16)
        message = f"User created successfully, your password is {password}."
    hashed = p.calculate(password)
    new_user = models.User(username=username, password=hashed)
    try:
        db.add(new_user)
    except:
        db.rollback()
        return {
            "code": 500,
            "message": "Create user failed."
        }
    db.commit()
    return {
        "code": 200,
        "message": message
    }


def auth(db: Session, username: str, password: str):
    user_data = db.query(models.User).filter(models.User.username == username).first()
    if not user_data:
        return None
    p = Password()
    if not p.verify(hashed=user_data.password, password=password):
        return False
    return True


def change_password(db: Session, username: str, password: str, new_password: str = None):
    if not auth(db=db, username=username, password=password):
        return {
            "code": 401,
            "message": "Authentication failed."
        }
    if new_password == password:
        return {
            "code": 400,
            "message": "New password cannot be the same as the old one."
        }
    p = Password()
    user_data = db.query(models.User).filter(models.User.username == username).first()
    message = "Password changed successfully."
    if not new_password:
        new_password = p.generate(length=16)
        message = f"Password changed successfully, your new password is {new_password}."
    hashed = p.calculate(password=new_password)
    try:
        user_data.password = hashed
    except:
        db.rollback()
        return {
            "code": 500,
            "message": "Change password failed."
        }
    db.commit()
    return {
        "code": 200,
        "message": message
    }


def get_short_link(db: Session, route: str):
    url = db.query(models.ShortLink).filter(models.ShortLink.route == route).first()
    if url:
        return url.url
    else:
        return None


def new_short_link(db: Session, username: str, password: str, route: str, url: str):
    DISALLOWED_ROUTE = {'favicon.ico', 'index.html', 'robots.txt', 'sitemap.xml', 'docs', 'redoc', 'user', 'shortlinks', 'shortlink'}
    if route in DISALLOWED_ROUTE:
        return {
            "code": 400,
            "message": "Route is not allowed."
        }
    if not auth(db=db, username=username, password=password):
        return {
            "code": 401,
            "message": "Authentication failed."
        }
    if get_short_link(db=db, route=route):
        return {
            "code": 400,
            "message": "Short link already exists."
        }
    new_link = models.ShortLink(route=route, url=url)
    try:
        db.add(new_link)
    except:
        db.rollback()
        return {
            "code": 500,
            "message": "Create short link failed."
        }
    db.commit()
    return {
        "code": 200,
        "message": "Short link created successfully.",
    }


def delete_short_link(db: Session, username: str, password: str, route: str):
    if not auth(db=db, username=username, password=password):
        return {
            "code": 401,
            "message": "Authentication failed."
        }
    url = db.query(models.ShortLink).filter(models.ShortLink.route == route).first()
    if not url:
        return {
            "code": 404,
            "message": "Short link not found."
        }
    try:
        db.delete(url)
    except:
        db.rollback()
        return {
            "code": 500,
            "message": "Delete short link failed."
        }
    db.commit()
    return {
        "code": 200,
        "message": "Short link deleted successfully."
    }


def update_short_link(db: Session, username: str, password: str, route: str, new_route: str = False, new_url: str = False):
    DISALLOWED_ROUTE = {'favicon.ico', 'index.html', 'robots.txt', 'sitemap.xml', 'docs', 'redoc', 'user',
                        'shortlink', 'shortlinks'}
    if new_route in DISALLOWED_ROUTE:
        return {
            "code": 400,
            "message": "Route is not allowed."
        }
    if not new_url and not new_route:
        return {
            "code": 400,
            "message": "No data need to update."
        }
    if not auth(db=db, username=username, password=password):
        return {
            "code": 401,
            "message": "Authentication failed."
        }
    url = db.query(models.ShortLink).filter(models.ShortLink.route == route).first()

    if not url:
        return {
            "code": 404,
            "message": "Short link not found."
        }
    try:
        if new_url:
            url.url = new_url
        if new_route:
            url.route = new_route
    except:
        db.rollback()
        return {
            "code": 500,
            "message": "Update short link failed."
        }
    db.commit()
    return {
        "code": 200,
        "message": "Short link updated successfully.",
    }


def get_all_links(db: Session, username: str, password: str):
    if not auth(db=db, username=username, password=password):
        return {
            "code": 401,
            "message": "Authentication failed."
        }
    links = db.query(models.ShortLink).all()
    urls = []
    for link in links:
        urls.append(
            {
                "route": link.route,
                "url": link.url
            }
        )
    return {
        "code": 200,
        "message": "Get short links successfully.",
        "data": urls
    }
