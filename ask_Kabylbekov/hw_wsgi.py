
def application(environ, start_response):
	data = "Hello, world!\n"
	start_response("200 OK", [
		("Content-Type", "text/plain"),
		("Content-Length", str(len(data)))
	])
	return iter([data])

import cgi

forms = b'''<html>
 <body>
   <h1>Index Page</h1>
   
   <form method=post>
    <fieldset>
   <legend>POST FORM</legend>
   <ul>
    <li>First Name: <input name='first'></li>
    <li>Last Name:  <input name='last'></li>
   </ul>
   <input type='submit' value='POST'>
   </fieldset>
   </form>
   
   <form method=get>
   <fieldset>
   <legend>GET FORM</legend>
   <ul>
    <li>First Name: <input name='first'></li>
    <li>Last Name:  <input name='last'></li>
   </ul>
   <input type='submit' value='GET'>
   </fieldset>
   </form>
   
   <p>%s</p>
   
 </body>
</html>
'''
    
def app(environ, start_response):
    
    # use FieldStorage but we need to pass in the wsgi.input input stream
    # for POST requests and the environ variable for the environment
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    
    if 'first' in form:
        first = form.getvalue("first", "")
        last = form.getvalue("last", "")
        info = "<p>First = '%s', Last = '%s'</p>" % (first, last)
    else:
        info = "<p>No form submitted</p>"
    
            
    page = [b"<html>", forms.encode(), info.encode(), b"</html>"]
    
    headers = [('content-type', 'text/html')]
    start_response('200 OK', headers)
    return page