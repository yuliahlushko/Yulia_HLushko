notes = []
i = True
while i:
    action = input('Оберіть дію (add, earliest, latest, longest, shortest, exit): ')
    if action == 'add':
        note = input('Додай нотатку: ')
        notes.append(note)
        print(notes)
    elif action == 'earliest':
        print(notes)
    elif action == 'latest':
        print(list(reversed(notes)))
    elif action == 'longest':
        notes.sort(reverse=True, key=len)
        print(notes)
    elif action == 'shortest':
        notes.sort(key=len)
        print(notes)
    elif action == 'exit':
        i = False
