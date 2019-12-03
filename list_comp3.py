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

list1=list([person ['name'] for users in user_groups for person in users if person['age'] < 30])
print(list1)