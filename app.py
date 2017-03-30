'''
Japronto trials
'''
import json
from pprint import pprint
import asyncio
from japronto import Application

users = []
with open('users.json') as data_file:
    users = json.load(data_file)

def get_users(request):
    '''get_users'''
    return request.Response(json=users)

def get_user(request):
    '''get_user'''
    id = request.match_dict['id']
    pprint(id)
    user = [u for u in users if u['id'] == id]
    return request.Response(json=user[0])

async def async_def(request):
    '''async_def'''
    for i in range(1, 4):
        await asyncio.sleep(1)
        print(i, ' seconds elapsed')
    return request.Response(text='3 seconds elapsed')

def create_user(request):
    pprint('creating user')
    msg = ''
    try:
        user = request.json
    except json.JSONDecodeError:
        pass
    else:
        if len([u for u in users if u['id'] == user['id']]) != 0:
            msg = 'User with id: ' + user['id'] + ' already exists!'
        else:
            users.append(user)
            msg = 'Created user with id: ' + user['id'] + '\nuser: \n' + str(user)

            

    # return request.Response(text='created user = ' + str(user))
    return request.Response(text=msg)



app = Application()

r = app.router
r.add_route('/', get_users)
r.add_route('/users', get_users, 'GET')
r.add_route('/users/{id}', get_user, 'GET')
r.add_route('/users', create_user, 'POST')

r.add_route('/async', async_def)

app.run(debug=True)
