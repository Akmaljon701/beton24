from fastapi.exceptions import HTTPException


def check_ishchi_admin(current_user):
    if current_user.role != "ishchi_admin":
        raise HTTPException(status_code=403, detail="Sizga ruhsat etilmagan!")