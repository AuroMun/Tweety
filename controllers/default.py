# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    if auth.user: redirect(URL('home'))
    return locals()

@auth.requires_login()
def home():
    db.cheeps.author.default = auth.user
    db.cheeps.tstamp.default = request.now
    form = SQLFORM(db.cheeps).process()
    form.element('textarea[name=body]')['_style'] = 'width:400px; height:40px;'
    form.element('textarea[name=body]')['_placeholder'] = "What's up, lil bird?"
    form2 = SQLFORM(db.cheeps, col3={'name': 'Your full name'})
    form2.element('textarea[name=body]')['_style'] = 'width:400px;height:40px;'
    form2.element('textarea[name=body]')['_placeholder'] = "What's up, lil bird?"
    if form2.process().accepted:
       response.flash("LALALA")

    followees = db(db.followers.follower==auth.user_id)
    list = [auth.user_id] + [row.followee for row in followees.select(db.followers.followee)]
    cheeps = db(db.cheeps.author.belongs(list)).select(orderby=~db.cheeps.tstamp, limitby=(0,100))
    return locals()

def profile():
    user = db.auth_user(request.args(0))
    if not user:
        redirect(URL('home'))
    cheeps = db(db.cheeps.author==user.id).select(orderby=~db.cheeps.tstamp, limitby=(0,100))
    details = db(db.auth_user.id==user.id).select()
    return locals()

@auth.requires_login()
def reply():
    a = request.post_vars
    id_new = db['cheeps'].insert(**{'body': a.body, 'author': a.child, 'tstamp': request.now})
    db['replies'].insert(**{'child': id_new, 'parent': a.parent})
    return locals()

@auth.requires_login()
def search():
    form = SQLFORM.factory(Field('name',requires=IS_NOT_EMPTY()))
    if form.accepts(request):
        tokens = form.vars.name.split()
        query = reduce(lambda a,b:a&b,
                       [db.auth_user.first_name.contains(k)|db.auth_user.last_name.contains(k) \
                            for k in tokens])
        people = db(query).select( orderby=db.auth_user.first_name|db.auth_user.last_name)
        #,left=db.followers.on(db.followers.followee==db.auth_user.id)
        print "Heyy"
        for person in people:
            print person.id
            print auth.user.id
            query1 = (db.followers.followee==person.id)
            query2 = (db.followers.follower==auth.user.id)
            listOfFollowers =  db(query1 & query2).select()
            if len(listOfFollowers)!=0:
                person['isFollow'] = True
                print "You are following " + person.first_name
            else:
                person['isFollow'] = False
                print "You are not following " + person.first_name
    else:
        people = []
    return locals()

@auth.requires_login()
def follow():
    me = auth.user
    if request.env.request_method!='POST': raise HTTP(400)
    if request.args(0) =='follow' and not db.followers(follower=me,followee=request.args(1)):
        # insert a new friendship request
        db.followers.insert(follower=me,followee=request.args(1))
    elif request.args(0)=='unfollow':
        # delete a previous friendship request
        db(db.followers.follower==me)(db.followers.followee==request.args(1)).delete()

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki()

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
