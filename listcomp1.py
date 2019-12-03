user_groups = [
    [
        {'name':'Manuel','age':31},
        {'name':'Max','age':30}
    ],
    [
        {'name':'Sarah','age':29},
        {'name':'Julie','age':32}
    ]
]

#user_name = [ person['name'] for group in user_groups for person in group if (person['age']>30)]
user_name = [ person['name'] for user in user_groups for person in user if person['age'] ]
print (user_name)
print (type(user_name))