from random import randint

def get_weather(city: str, day: str) -> dict:
    """
    Написать погоду в городе city на день day
    Arguments:
    city: название города
    day: дата
    Returns:
    {
    
    }
    """
    return {
        "city": city,
        "day" : day,
        "temperature": round(randint(-5, 20), 1)
    }
#def make_flascards(topic: str, count: int = 3) -> dict:
    """Create flashcards for a school or programming topic."""
    # TODO: убрать пробелы по краям topic
    # TODO: если topic пустой, вызвать ValueError
    # TODO: если count меньше 1 или больше 10, вызвать ValueError
    # TODO: вернуть dict с ключами "topic" и "cards"
    # TODO: cards должен быть списком словарей
    # TODO: у каждой карточки должны быть "front" и "back"
def split_time(minutes: int, split_minutes: int, break_time: int) -> dict:
    '''
    Принять обычную бытовую задачу и разбить время на короткие рабочие блоки
    Args:
    minutes, split_minutes, break_time
    Returns:
    {
    "blocks": full_blocks,
    "remaining_time": left_time,
    "full_break_time": full_break_time,
    "steps":steps
    }
    '''
    if minutes <= 0 or minutes >= 1440:
        return ValueError
    if split_minutes <= 0:
        return ValueError
    if break_time <= 0:
        return ValueError
    full_blocks = minutes // split_minutes
    left_time = minutes % split_minutes
    break_numbers = full_blocks - 1
    if break_numbers < 0:
        return ValueError
    full_break_time = break_numbers * break_time
    steps = []
    for i in range(full_blocks):
        steps.append(f'Блок {i + 1}, длиной: {split_minutes} минут.')
    for i in range(break_numbers):
        steps.append(f'Перерыв {i} {break_time} минут')
    return {
        "Blocks": full_blocks,
        "Time_left": left_time,
        "Time_of_all_breaks": full_break_time,
        "Steps": steps

    }
def convert_units()  -> str:
    length = {
        "milimeters": 0.001,
        "centimeters": 0.01,
        "meters": 1.0,
        "kilometers": 1000.0,
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        

    }

    weight= {
        "grams": 1,
        "kilograms": 1000,
        "g": 1.0,
        "kg": 1000.0
    }

    time = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "sec": 1.0,
        "min": 60.0,
        "hours": 3600.0
    }

    