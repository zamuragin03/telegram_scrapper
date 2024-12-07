from aiogram.fsm.state import State,StatesGroup

class FSMUser(StatesGroup):
    beginning = State()
    choosing_action = State()
    choosing_method_type = State()
    choosing_deposit_amount = State()
    choosing_sub_rate = State()
    activating_sub = State()
    typing_wishes = State()
    typing_present_amount = State()
    
    typing_none_id = State()
    