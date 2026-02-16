"""   ===============       Задача для работы сосписком в котором СЛОВАРИ      ======================

.	Написать функцию build_stats(events) -> dict, которая вернёт:
	•	by_action: сколько раз встречалась каждая action
	•	by_user: сколько событий у каждого user
	2.	Битые события (без action или user) не падать, а:
	•	считать в отдельный счётчик invalid
	3.	Запрещено использовать collections.Counter (чтобы прокачать dict).

"""

def build_stats(events:list) -> dict:
    ansver = {
        'invalid': 0,
        'by_action': {},
        'by_user': {}
    }

    for obj in events:
        if not obj.get('user') or not obj.get('action'):
            ansver['invalid'] += 1
            continue
        if obj['user'] not in ansver['by_user']:
            ansver['by_user'][obj['user']] = 1
        else:
            ansver['by_user'][obj['user']] += 1
        if obj['action'] not in ansver['by_action']:
            ansver['by_action'][obj['action']] = 1
        else :
            ansver['by_action'][obj['action']] += 1

    return ansver


events = [
    {"user": "u1", "action": "click"},
    {"user": "u2", "action": "view"},
    {"user": "u1", "action": "click"},
    {"user": "u1", "action": "buy"},
    {"user": "u2", "action": "click"},
    {"user": "u3"},  # action отсутствует (битые данные)
]

result = build_stats(events)
print(result)


"""   ===============      
"""