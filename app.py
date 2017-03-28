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
    return request.Response(json=users)

def get_user(request):
    id = request.match_dict['id']
    pprint(id)
    user = [u for u in users if u['id'] == id]
    return request.Response(json=user[0])

async def async_def(request):
    for i in range(1, 4):
        await asyncio.sleep(1)
        print(i, ' seconds elapsed')
    return request.Response(text='3 seconds elapsed')        


app = Application()

r= app.router
r.add_route('/', get_users)
r.add_route('/users', get_users)
r.add_route('/users/{id}', get_user)
r.add_route('/async', async_def)

app.run(debug=True)
