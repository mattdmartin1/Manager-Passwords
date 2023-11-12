# Master Password
# view function
# add function
# While True
# add of view existing loop

master_pwd = input('What is the master password?: ')

def view():
    
    pass

def add():
    name = input('Account Name: ')
    pwd = input('Enter password: ')
    
    with open ('new_txt.file', 'a') as f:
        f.write(name + '|' + pwd + '\n')
        

while True:
    mode = input('Would you like to add a new password or existing ones (view, add), press q to quit? ').lower()
    if mode == 'quit':
        break
    
    if mode == 'view':
        view()
    
    elif mode == 'add':
        add()
    
    else:
        print('Incorrect mode. ')
        continue