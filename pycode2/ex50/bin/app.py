""" Web applications's working:
Here's what's happening when your browser hits your application:

1. Your browser makes a network connection to your own computer, which is called localhost and is 
    a standard way of saying "whatever my own computer is called on the network." It also uses port 8080.
2. Once it connects, it makes an HTTP request to the bin/app.py application and asks for the / URL, 
    which is commonly the first URL on any website.
3. Inside bin/app.py you've got a list of URLs and what classes they match. The only one we have is 
    the'/', 'index' mapping. This means that whenever someone goes to / with a browser, web will find the 
    class index and load it to handle the request.
4. Now that web has found class index it calls the index.GET method on an instance of that class to 
    actually handle the request. This function runs and simply returns a string for what web should send to 
    the browser.
5. Finally, web has handled the request and sends this response to the browser, which is what you 
    are seeing.

How a template works:
1. In your bin/app.py you've added a new variable, render, which is a web.template.render object.
2. This render object knows how to load .html files out of the templates/ directory because you 
    passed that to it as a parameter.
3. Later in your code, when the browser hits the index.GET, now instead of just returning the string 
    greeting as earlier, you call render.index and pass the greeting to it as a variable.
4. This render.index method is kind of a magic function where the render object sees that you're 
    asking for index, goes into the templates/ directory, looks for a page named index.html, and 
    then "renders" it, or converts it.
5. In the templates/index.html file you see the beginning definition that says this template takes
    a greeting parameter, just like a function. Also, just like Python this template is indentation 
    sensitive, so make sure you get them right.
6. Finally, you have the HTML in templates/index.html that looks at the greeting variable and, if 
    it's there, prints one message using the $greeting, or a default message.
"""
import web

urls = ('/', 'Index')

app = web.application(urls, globals())

# Used a render for rendering the templates | the names of files are used
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World!!"
        return render.index(greeting = greeting)

if __name__ == '__main__':
    app.run()