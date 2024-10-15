geektech = {
    'name': 'Geektech',
    'address': 'Токтогула 175',
    'courses': {'Backend', 'Android'}
}
geeks = dict(name= 'GEEKS', address= 'Ибраимова 103')
geektech.update(geeks)
geeks = geektech.copy()
geeks['courses'].update(['Frontend', 'IOS'])
print(geeks)