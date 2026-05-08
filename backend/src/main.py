from fastapi import FastAPI
from src.modules.army.router import router as army_router
from src.modules.auth.router import router as auth_router
from src.modules.lfg.router import router as lfg_router
from src.modules.store.router import router as store_router
from src.modules.users.router import router as users_router

app = FastAPI(title="Warhammer App", version="0.0.1")

app.include_router(army_router, prefix="/api/army", tags=["army"])
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(lfg_router, prefix="/api/lfg", tags=["lfg"])
app.include_router(store_router, prefix="/api/store", tags=["store"])
app.include_router(users_router, prefix="/api/users", tags=["users"])
