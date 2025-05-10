def get_next_question(history):
    steps = [
        "What legal issue are you facing?",
        "When did this issue occur?",
        "Who else is involved?",
        "What outcome are you seeking?"
    ]
    user_responses = [m['user'] for m in history if 'user' in m]
    if len(user_responses) < len(steps):
        return steps[len(user_responses)]
    return None
