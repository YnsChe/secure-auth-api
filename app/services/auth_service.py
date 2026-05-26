# Put the whole authentication flow per example

"""def authenticate_user(conn, username, password):

    stored_hash = get_stored_password(conn, username)

    if not stored_hash:
        return False

    if not verify_password(stored_hash, password):
        return False

    return create_access_token(username)"""