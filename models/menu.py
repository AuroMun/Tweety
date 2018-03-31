# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

# response.title = "Tweety"
# response.subtitle = "Cheep cheep cheep cheep"
# response.menu = [
#     (T('Home'), False, URL('default','home')),
#     (T('Profile'), False, URL('default','profile')),
#     (T('Search'), False, URL('default','search')),
#     (T('Notifs'), False, URL('default','notifs')),
#     ]
def item(name):
    if auth.is_logged_in():
        notifCount = db((db.notifs.person==auth.user.id) & (db.notifs.opened==False)).count()
        if notifCount > 0:
            return A(name+ " " + str(notifCount), _href=URL('default', 'notifs'), _style="color:red;")
        else:
            return A(name, _href=URL('default', 'notifs'), _style="color:grey;")
    else:
        return A(name, _href=URL('default', 'notifs'), _style="color:grey;")

response.title = "Tweety"
response.subtitle = "Cheep cheep cheep cheep"
response.menu = [
    (A('Home', _href=URL('default', 'home'), _style="padding-left:10px;padding-right:20px;color:grey"), False, None),
    (A('Search', _href=URL('default', 'search'), _style="padding-left:10px;padding-right:20px;color:grey"), False, None),
    (A('Profile', _href=URL('default', 'profile'), _style="padding-left:10px;padding-right:20px;color:grey"), False, None),
    (item('Notifs'), False, None),
    ]
