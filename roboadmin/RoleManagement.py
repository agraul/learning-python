# Role Mangement functions
import asyncio
import discord


def assign_role(message):
    message_content = message.content
    # strip trigger and split content
    #TODO:
    contents = message_content[2:].split(' ')
    if not contents:
        pass
        print("message has no content")
    else:
        try:
            role = contents[0]
            user = contents[1]
        except IndexError:
            role = contents[0]
            user = message.author
    server_roles = []
    for s_role in message.server.roles:
        server_roles.append(s_role.name)

    if role.lower() in server_roles:
        print(f'Found {role.lower()} in server roles.')
    elif role.upper() in server_roles:
        print(f'Found {role.upper()} in server roles.')
    elif role.title() in server_roles:
        print(f'Found {role.title()} in server roles.')

    else:
        print(f'{role} not in server roles.')



