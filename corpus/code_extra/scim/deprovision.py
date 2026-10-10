LOGIN_DISABLE_SLA_MIN = 5
SESSION_REVOKE_SLA_MIN = 15

def deprovision(user_id, session_store):
    disable_login(user_id)
    session_store.revoke_all(user_id)
