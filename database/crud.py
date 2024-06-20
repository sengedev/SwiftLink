from sqlalchemy.orm import Session
from database import models, schemas
from security.password import Password
import datetime


def create_user(db: Session, user: schemas.UserCreate):
    # 判断是否有用户（只允许一个用户）
    user_count = db.query(models.User).count()
    if user_count > 0:
        return None
    username = user.username
    password = user.password
    p = Password()
    no_password = False
    if not password:
        password = p.generate(length=16)
        no_password = True
    hashed = p.calculate(password)
    new_user = models.User(username=username, password=hashed)
    try:
        db.add(new_user)
    except:
        db.rollback()
        return None
    db.commit()
    return password if no_password else True


def auth(db: Session, user: schemas.UserAuth):
    user_data = db.query(models.User).filter(models.User.username == user.username).first()
    if not user_data:
        return False
    p = Password()
    if not p.verify(hashed=user_data.password, password=user.password):
        return False
    return True


def change_password(db: Session, user: schemas.UserUpdate):
    user_schema = schemas.UserAuth(username=user.username, password=user.password)
    if not auth(db=db, user=user_schema):
        return False
    if user.new_password == user.password:
        return False
    p = Password()
    user_data = db.query(models.User).filter(models.User.username == user.username).first()
    password = user.new_password
    no_password = False
    if not password:
        password = p.generate(length=16)
        no_password = True
    hashed = p.calculate(password=password)
    try:
        user_data.password = hashed
    except:
        db.rollback()
        return False
    db.commit()
    return password if no_password else True


def get_short_link(db: Session, link: schemas.ShortLinkBase):
    url = db.query(models.ShortLink).filter(models.ShortLink.route == link.route).first()
    return url


def new_short_link(db: Session, link: schemas.ShortLinkCreate):
    DISALLOWED_ROUTE = {'favicon.ico', 'index.html', 'robots.txt', 'sitemap.xml', 'docs', 'redoc', 'user', 'shortlinks', 'shortlink'}
    if link.route in DISALLOWED_ROUTE:
        return False
    user_schema = schemas.UserAuth(username=link.username, password=link.password)
    if not auth(db=db, user=user_schema):
        return False
    link_schema = schemas.ShortLinkBase(route=link.route)
    if get_short_link(db, link_schema):
        return False
    new_link = models.ShortLink(route=link.route, url=link.url)
    try:
        db.add(new_link)
    except:
        db.rollback()
        return False
    db.commit()
    return True


def delete_short_link(db: Session, link: schemas.ShortLinkBaseWithAuth):
    DISALLOWED_ROUTE = {'favicon.ico', 'index.html', 'robots.txt', 'sitemap.xml', 'docs', 'redoc', 'user', 'shortlinks',
                        'shortlink'}
    if link.route in DISALLOWED_ROUTE:
        return False
    user_schema = schemas.UserAuth(username=link.username, password=link.password)
    if not auth(db=db, user=user_schema):
        return False
    link_schema = schemas.ShortLinkBase(route=link.route)
    url = get_short_link(db, link_schema)
    if not url:
        return False
    try:
        db.delete(url)
    except:
        db.rollback()
        return False
    db.commit()
    return True


def update_short_link(db: Session, link: schemas.ShortLinkUpdate):
    DISALLOWED_ROUTE = {'favicon.ico', 'index.html', 'robots.txt', 'sitemap.xml', 'docs', 'redoc', 'user', 'shortlinks',
                        'shortlink'}
    if link.route in DISALLOWED_ROUTE:
        return False
    user_schema = schemas.UserAuth(username=link.username, password=link.password)
    if not auth(db=db, user=user_schema):
        return False
    link_schema = schemas.ShortLinkBase(route=link.route)
    url = get_short_link(db, link_schema)
    if not url:
        return False
    try:
        if link.new_url:
            url.url = link.new_url
        if link.new_route:
            url.route = link.new_route
    except:
        db.rollback()
        return False
    db.commit()
    return True


def get_all_links(db: Session, user: schemas.UserAuth):
    if not auth(db=db, user=user):
        return False
    links = db.query(models.ShortLink).all()
    urls = []
    for link in links:
        urls.append(
            {
                "route": link.route,
                "url": link.url
            }
        )
    return urls
