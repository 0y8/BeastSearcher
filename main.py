import requests
import os

os.system('clear')

user_id = input('Starting User ID: ')
item_id = input('Item ID: ')

while True:
    
    user_id = int(user_id) + 1


    r = requests.get(f"https://inventory.roblox.com/v1/users/{user_id}/items/Asset/{item_id}").text

    if "name" in r:
        
        print('Found Owner:', user_id)
        
        file2 = open("owners.txt", "a")
        file2.write(f'str({user_id}\n')
        file2.close()
        
    else:
        print('Invalid Owner')
        
        
