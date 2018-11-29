"""We are using the templates/hello_form.html form to get the data and display"""
import web

urls = ( '/hello', "Index"
    )

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class Index(object):
    """The class that is called by the application's run function with .GET
    Rather than entering the key=values at the address bar as accepted by web.input() 
    it's better to use POST forms"""

    def GET(self):
        return render.hello_form_laid_out()

    def POST(self):
        form = web.input(name="NoBody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
