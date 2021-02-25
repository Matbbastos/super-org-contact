from functools import wraps
from flask import redirect, url_for, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'credentials' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
