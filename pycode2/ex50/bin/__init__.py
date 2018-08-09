"""The modules that are executed for the web app
----------------

app.py : 
    The module is basic web app. that can listen on default port and print some predefined message
post_form.py :
    This uses the templates index.html and hello_form_laid_out.html and Get's some values from user (handled with 
    POST method of the class) and returns the Greetings (using GET method of class)
    Good For:
        - basic user input
        - sample usage of POST method to handle the post requests from browser
        - getting values from the browser and transfer it to the template renderer
post_image.py : 
    This uses templates index_pic.html and hello_form_pic.html - so Get the image store it in static directory and 
    show the image as the image of person with greetings received earlier. 
    Good for:
        - get current directory
        - get the file from user via the form
        - store the file with the same name as it's uploaded name - check if it exists on disk
        - output the image at 50% size using template - the file path sent to the template

_ more details of changes in this are in last 3-5 commits before this one"""