from fastapi import HTTPException
from models.users import User
from routes.auth import hash_password
from utils.pagination import pagination


def all_users(search, status, role, page, limit, db):
    users = db.query(User)
    if search:
        search_formatted = "%{}%".format(search)
        users = users.filter(User.username.like(search_formatted))
    if status in [True, False]:
        users = users.filter(User.status == status)
    if role:
        users = users.filter(User.role == role)
    if page and limit:
        return pagination(users, page, limit)
    else:
        return users.all()


def create_user(form, db):
    check_user = db.query(User).filter_by(username=form.username).first()
    if check_user:
        raise HTTPException(status_code=403, detail="User already exists!")
    new_user = User(
        fullname=form.fullname,
        username=form.username,
        password_hash=hash_password(form.password_hash),
        role=form.role,
        status=form.status,

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(form, db):
    user = db.query(User).filter_by(id=form.user_id, status=True)
    if user.first() is None:
        raise HTTPException(status_code=404, detail="User not found!")

    user.update({
        User.fullname: form.fullname,
        User.username: form.username,
        User.password_hash: hash_password(form.password_hash),
        User.role: form.role,
        User.status: form.status,
    })
    db.commit()
    return True
