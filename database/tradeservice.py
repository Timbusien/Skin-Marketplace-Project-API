from database.models import Trade
from datetime import datetime
from database import get_database


def validate_skin(skin_id, my_db):
    exact_skin = my_db.query(Trade).filter_by(skin_id=skin_id).first()

    return exact_skin


def get_exact_user_skin_name_my_db(user_id, my_db):
    exact_skin_name = my_db.query(Trade).filter_by(user_id=user_id).first()

    return exact_skin_name


def get_user_skin_trade(status, skin_id, skin_from_id, skin_to_id, user_to, user_from, balance, user_id, cost_skin):
    my_db = next(get_database())
    check_skin_to = validate_skin(skin_to_id, my_db)
    check_skin_from = validate_skin(skin_from_id, my_db)
    check_user_to = get_exact_user_skin_name_my_db(user_id, my_db)
    check_user_from = get_exact_user_skin_name_my_db(user_id, my_db)

    if check_user_from and check_user_to:
        if check_skin_to and check_skin_from:
            if user_to.balance >= user_from.skin_cost:
                user_to.balance -= user_from.balance
                new_trade = Trade(skin_from_id=check_skin_from.skin_id, skin_to_id=check_skin_to.skin_id,
                                  cost_skin=cost_skin, skin_id=skin_id, balance=balance, user_to=user_to,
                                  user_from=user_from, status=status, trade_date=datetime.now())
                my_db.add(new_trade)
                my_db.commit()
            else:
                return 'No enough money'
        else:
            return 'There is no Skin'
    else:
        return 'User does not exist'


def get_skin_trade_my_db(skin_to_id):
    my_db = next(get_database())
    trade = my_db.query(Trade).filter_by(skin_to_id=skin_to_id).all()

    return trade


def cancel_user_skin_trade(skin_from, skin_to, user_from, user_id, trade_id):
    my_db = next(get_database())
    check_skin_to = validate_skin(skin_to, my_db)
    check_skin_from = validate_skin(skin_from, my_db)
    check_user_to = get_exact_user_skin_name_my_db(user_id, my_db)
    check_user_from = get_exact_user_skin_name_my_db(user_id, my_db)

    if check_user_from and check_user_to:
        if check_skin_to and check_skin_from:
            if user_from.balance >= user_from.skin_cost:
                check_user_from -= user_from.skin_cost
                check_skin_to += user_from.skin_cost

                exact_trade = my_db.query(Trade).filter_by(trade_id=trade_id).first()
                exact_trade.status = False
                my_db.commit()
                return 'Trade canceled Successfully'
            else:
                return 'No enough balance'
        return 'User does not exist'








