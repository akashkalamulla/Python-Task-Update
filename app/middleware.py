from flask import redirect, url_for, request
from flask_login import current_user

def restrict_access():
    if current_user.is_authenticated:
        if request.endpoint in ['web.login', 'web.signup']:
            return redirect(url_for('web.dashboard'))
    else:
        if request.endpoint in ['web.dashboard']:
            return redirect(url_for('web.login'))
