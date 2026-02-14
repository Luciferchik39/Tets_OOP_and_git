
# 1.	Написать функцию build_stats(events) -> dict, которая вернёт:
# 	•	by_action: сколько раз встречалась каждая action
# 	•	by_user: сколько событий у каждого user
# 	2.	Битые события (без action или user) не падать, а:
# 	•	считать в отдельный счётчик invalid
# 	3.	Запрещено использовать collections.Counter (чтобы прокачать dict).
# def build_stats(events:list):
#     invalid = 0
#     answer = {
#         # мы храним имя user и его количество
#         'by_user': {},
#         'by_action': {},
#         'invalid': 0
#     }
#     by_action = {}
#     by_user = {}
#     for event in events:
#         if "user" not in event or 'action' not in event:
#             answer['invalid'] += 1
#             continue
#         a = event['user']
#         b = event['action']
#
#         if a in answer['by_user']:
#             answer['by_user'][a] += 1
#         else:
#             answer['by_user'][a] = 1
#
#         if b in answer['by_action']:
#             answer['by_action'][b] += 1
#         else:
#             answer['by_action'][b] = 1
#     return answer
#
#
# events = [
#     {"user": "u1", "action": "click"},
#     {"user": "u2", "action": "view"},
#     {"user": "u1", "action": "click"},
#     {"user": "u1", "action": "buy"},
#     {"user": "u2", "action": "click"},
#     {"user": "u3"},  # action отсутствует (битые данные)
# ]
# print(build_stats(events))
# print(events[0].values())
# print(events[0].items())
# print(events[0].keys())