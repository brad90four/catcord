import backend.db.tasks as tasks
import backend.db.crud as crud
import backend.core.actions as actions
from backend.schemas import UserCreateBody
from fastapi import APIRouter
from uuid import uuid4
import hashlib

router = APIRouter()


@router.post("/token")
async def token(userinfo: UserCreateBody):
    token = str(uuid4())
    tokenhash = actions.gentokenhash(token, userinfo.username)
    password = userinfo.password
    passhash = actions.gentokenhash(password, userinfo.username)

    async with tasks.Database() as conn:
        await crud.new_user(
            conn, str(actions.gensnowflake()), tokenhash, userinfo.username, passhash
        )

    return {"token": token}
