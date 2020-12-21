import json 


"""
users_books = '''
{
    "books":[
        {
            "bookid": "",
            "title": "The Stand",
            "author": "Stephen Kin",
            "lang": "English",
            "genre": "Post Apocalyptic",
            "publisher: "Double Day",
            "pubyear" : "October 3, 1978",
            "isbn" : "978-0-385-12168-2",
            "pages" :"823"
        }
    ]
}
'''

data = json.loads(users_books)

for book in data['books']:
    print(book['title']) #load json string into a python object 



"""


users_books = '''
{
    "books":[
        {
            "isbn" : "978-0-385-12168-2",
            "title": "The Stand",
            "author": "Stephen Kin",
            "lang": "English",
            "genre": "Post Apocalyptic",
            "publisher": "Double Day",
            "pubyear" : "October 3, 1978"
        }
    ]
}
'''

data = json.loads(users_books)

for book in data['books']:
    print(data)

with open('user_books.txt', 'w') as f:
    json.dump(data, f)
'''
for book in data['books']:
    del book['isbn'] #dump python object into a json string 

new_string = json.dumps(data, indent=3, sort_keys=True) #indents code by three tabs and sorts

print(new_string)  #prints without showing the isbn 
'''


#load json filer into python objects and then back to json files 
'''
with open('books.json') as f: 
    data = json.load(f) #loads into a python object 


for book in data['books']:
    print(book['title', 'author', 'lang', 'genre','publisher', 'pubyear',
                'isbn', 'pages'])

'''
'''
for book in data['books']:
    del book['isbn']
'''
