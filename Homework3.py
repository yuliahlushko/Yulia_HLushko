action = input('Оберіть дію (add, earliest, latest, longest, shortest, Exit): ')
notes = []
while action in ['add']:
    note = input('Додай нотатку: ')
    notes.append(note)
    print(notes)
    action = input('Оберіть дію (add, earliest, latest, longest, shortest, Exit): ')
    continue
if action == 'longest':
    notes.sort(reverse=True, key=len)
    print(notes)
    action = input('Оберіть дію (add, earliest, latest, longest, shortest, Exit): ')
if action == 'shortest':
    notes.sort(key=len)
    print(notes)
    action = input('Оберіть дію (add, earliest, latest, longest, shortest, Exit): ')
if action == 'earliest':
    print(notes.reverse())
    action = input('Оберіть дію (add, earliest, latest, longest, shortest, Exit): ')
if action == 'latest':
    print(notes)
    action = input('Оберіть дію (add, earliest, latest, longest, shortest, Exit): ')