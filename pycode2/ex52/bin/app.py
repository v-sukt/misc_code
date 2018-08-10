"""
"""
from gothonweb import map
import web

web.config.debug = False

urls = (
        "/game", "GameEngine",
        "/end", "Bye",
        "/", "Index"
    )

app = web.application(urls, globals())

# to debug the sessiosn
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None })
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base='layout')

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        web.seeother("/game")

class GameEngine(object):

    def GET(self):
        return render.show_room(room=session.room)
        #if session.room:
        #    return render.show_room(room=session.room)
        #else:
        #    # what's missing - no return from the last room the_end*
        #    print "wrong input"
        #    return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # bugged section ! seems solved issue: game gave button and failed message for winners 
        # can even compare the room.name with the last room,
        if form.action in session.room.paths.keys():
            pass
        else:
            form.action = "*"

        if session.room == map.the_end_winner: 
            print "reached the end room"
            raise web.seeother("/end")
        elif session.room == map.the_end_looser:
            print "reached the last looser room"
            return render.you_died()
        elif session.room and form.action:
            # to debug - only on submit you can see the page you are leaving
            print "In the %r room" % session.room.name 
            session.room = session.room.go(form.action)

        web.seeother("/game")

class Bye(object):

    def GET(self):
        print "reached in bye"
        return render.you_won()
        session.kill()

if __name__ == "__main__":
    app.run()
