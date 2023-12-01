from fastapi import FastAPI
from user.user_api import user_router
from skin.skin_api import skin_router
from trade.trade_api import trade_router
from comment.comment_api import comment_router
from database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/')
app.include_router(user_router)
app.include_router(skin_router)
# app.include_router(trade_router)
app.include_router(comment_router)


@app.get('/sample')
async def smth():
    return 'Nothing here'



