# -*- encoding: utf-8 -*-

from flask import render_template
from flask_login import login_required
from apps.authentication import blueprint


@blueprint.route('/explore')
@login_required
def explore():

    return render_template('podcasts/explore.html', segment='explore')

# Login & Registration

# @blueprint.route("/github")
# def login_github():
#     """ Github login """
#     if not github.authorized:
#         return redirect(url_for("github.login"))

#     res = github.get("/user")
#     return redirect(url_for('home_blueprint.index'))

# @blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     login_form = LoginForm(request.form)
#     if 'login' in request.form:

#         # read form data
#         username = request.form['username']
#         password = request.form['password']

#         # Locate user
#         user = Users.query.filter_by(username=username).first()

#         # Check the password
#         if user and verify_pass(password, user.password):

#             login_user(user)
#             return redirect(url_for('authentication_blueprint.route_default'))

#         # Something (user or pass) is not ok
#         return render_template('accounts/login.html',
#                                msg='Wrong user or password',
#                                form=login_form)

#     if not current_user.is_authenticated:
#         return render_template('accounts/login.html',
#                                form=login_form)
#     return redirect(url_for('home_blueprint.index'))


# @blueprint.route('/register', methods=['GET', 'POST'])
# def register():
#     create_account_form = CreateAccountForm(request.form)
#     if 'register' in request.form:

#         username = request.form['username']
#         email = request.form['email']

#         # Check usename exists
#         user = Users.query.filter_by(username=username).first()
#         if user:
#             return render_template('accounts/register.html',
#                                    msg='Username already registered',
#                                    success=False,
#                                    form=create_account_form)

#         # Check email exists
#         user = Users.query.filter_by(email=email).first()
#         if user:
#             return render_template('accounts/register.html',
#                                    msg='Email already registered',
#                                    success=False,
#                                    form=create_account_form)

#         # else we can create the user
#         user = Users(**request.form)
#         db.session.add(user)
#         db.session.commit()

#         # Delete user from session
#         logout_user()
        
#         return render_template('accounts/register.html',
#                                msg='Account created successfully.',
#                                success=True,
#                                form=create_account_form)

#     else:
#         return render_template('accounts/register.html', form=create_account_form)


# @blueprint.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('authentication_blueprint.login'))

