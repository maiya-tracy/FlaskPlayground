from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play', defaults={'x': 3, 'color': 'blue'})
@app.route('/play/<x>', defaults={'color': 'blue'})
@app.route('/play/<x>/<color>')
def play(x, color):
	return render_template('play.html', x=int(x), color=color)



@app.errorhandler(404)
def page_not_found(error):
	return "Sorry! No response. Try again."



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.