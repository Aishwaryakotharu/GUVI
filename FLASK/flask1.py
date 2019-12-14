from flask import Flask
app=Flask(__name__)

@app.route('/',methods=['POST'])
def hello_world():
	return 'hello_world'

@app.route('/aish')
def hello_world1():
	return str(11)+'aish_world'

# main driver function 
if __name__=='__main__':
	app.run()


'''
# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
# Flask constructor takes the name of  
# current module (__name__) as argument. 
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function.
# run() method of Flask class runs the application  
# on the local development server.  
# ‘/’ URL is bound with hello_world() function.'''