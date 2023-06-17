import random

from lexicon.lexicon_ru import LEXICON_RU


def get_bot_chance() -> str:
    return random.choice(["rock", "paper", "scissor"])


def _normalise_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalise_user_answer(user_choice)
    rules: dict[str, str] = {
        "rock": "scissor",
        "scissor": "paper",
        "paper": "rock",
    }
    if user_choice == bot_choice:
        return "nobody_won"
    elif rules[user_choice] == bot_choice:
        return "user_won"
    return "bot_won"
