from fastapi import APIRouter
from database.tradeservice import get_skin_trade_my_db, get_user_skin_trade, cancel_user_skin_trade
from trade import CancelTradeValidator, CreateTradeValidator

trade_router = APIRouter(prefix='/trades', tags=['Trade Management'])


@trade_router.post('/create-trade')
async def add_new_trade(data: CreateTradeValidator):
    trade_data = data.model_dump()
    result = get_user_skin_trade(**trade_data)

    return {'message': result}


@trade_router.post('/cancel-trade')
async def cancel_trade(data: CancelTradeValidator):
    cancel_trade_data = data.model_dump()
    result = cancel_user_skin_trade(**cancel_trade_data)

    return {'message': result}


@trade_router.get('/check-trade-status')
async def get_trade(trade_id: int):
    result = get_skin_trade_my_db(skin_to_id=trade_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Trade Does not Exist'}


