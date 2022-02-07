import pwd


def fetch_users():
    users = []
    for user in pwd.getpwall():
        # 1000, 'home'
        if user.pw_uid >= 500 and 'Users' in user.pw_dir:
            users.append(
                {
                    'name': user.pw_name,
                    'id': user.pw_uid,
                    'home': user.pw_dir,
                    'shell': user.pw_shell
                }
            )
    return users
