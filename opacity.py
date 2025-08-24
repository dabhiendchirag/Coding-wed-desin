from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return """
        <html>
		<head>
		    <title>Opacitity color</title>
		    <style>
		    img{
		    height: 200px;
		    width: 200px;
		    opacity: 0.1;
		    }
		    img:hover{
		        opacity: 1;
		        transition-duration: 2s;
		        }
		    </style>
		</head>
		 <body>
		 <h1> Car Opacitity Property</h1>
		       <div class="image-box">
		          <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/A_cat_sitting_at_a_desk_actively_contributing_to_Wikip%C3%A9dia%2C_by_ChatGPT_4.0_%26_Dall-E_3.0_%282024%29.png" alt="">
		          <img src="https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg" alt="">
		          <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/Cute_cat_%281698598876%29.jpg" alt="">
		          <img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/Cute_Cat_2.jpg" alt="">
		      </div>
        </body>
		</html>
	"""
	
if __name__ == "__main__":
	app.run()