"""We are using the templates/hello_form.html form to get the data and display"""
import web
from os import path

urls = ( '/hello', "Index"
    )

app = web.application(urls, globals())

render = web.template.render('templates/')

#class Upload(object):
#    def GET(self):
#        web.header("Content-Type","text/html; charset=utf-8")
#        return render.hello_form_pic()
#
#    def POST(self):
#        x = web.input(myfile={})
#        filedir= "/tmp"
#        if 'myfile' in x:
#            fout = open(filedir + '/' + x.myfile.filename, 'wb'); # creates the file where the uploaded file should be stored
#            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
#            fout.close() # closes the file, upload complete
#            return "Success! Your image has been saved in the given folder."
#            raise web.seeother('/upload')

class Index(object):
    """The class that is called by the application's run function with .GET
    Rather than entering the key=values at the address bar as accepted by web.input() 
    it's better to use POST forms"""

    def GET(self):
        return render.hello_form_pic()

    def POST(self):
        #import subprocess
        #sub = subprocess.Popen("pwd", stdout=subprocess.PIPE)
        #filedir = sub.stdout.read().strip()

        filedir = "static"
        form = web.input(name="NoBody", greet="Hello", myfile={})
        #print "%r" % form # The structure is <Storage {'myfile':FieldStorage(myfile_str,fileneame_str,file_binary), 
        #                                               'name':'var_value', 'greet':'var_value'}
        
        if 'myfile' in form: #this code worked - need to find out the contents of form
            fout = open(str(filedir)+'/'+form.myfile.filename, 'wb')
            fout.write(form.myfile.file.read())
            fout.close()
        #    written=True
        #else:
        #    written=False
        
        if path.isfile(filedir+'/'+form.myfile.filename): #check if the file exists
            greeting = "%s, %s" % (form.greet, form.name)
        else:
            greeting = "ERROR: file not written"

        # print "%s, %s\nfile %s uploaded at %s: status:%s" % (form.greet, form.name, form.myfile.filename, filedir, written)
        return render.index_pic(greeting = greeting, filepath=filedir+'/'+form.myfile.filename)


if __name__ == "__main__":
    app.run()
