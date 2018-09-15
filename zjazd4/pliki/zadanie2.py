import sys

user_total_time = {}
user_last_login = {}

file_name = sys.argv[1]

with open(file_name) as f:
    for line in f:
        login, action, time_str = line.split(";")
        time = int(time_str)
        if action == 'LOGIN':
            user_last_login[login] = time
        elif action == 'LOGOUT':

            user_total_time[login] = user_total_time.get(login, 0) + time - user_last_login[login]
print(f'Czas przebywania w systemi:')
for user, time in user_total_time.items():
    print(f'- {user}: {time}')
