jack = {'name':'jack', 'car':'bmw'}
john = {'name':'john', 'car':'audi'}
mee = {'name':'mee'}

users =[jack, john, mee]

#cars =[person['car'] for person in users]
cars =[person.get('car', '') for person in users]
print(cars)

###(values) =[ (expression) for (value) in (collection) if (condition) ]