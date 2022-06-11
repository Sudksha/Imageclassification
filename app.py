from flask import Flask, request, jsonify
import flask
import util

artifacts=util.load_saved_artifacts()

app=Flask(__name__, )

@app.route('/')
def home():
    return flask.render_template('index.html')
    
@app.route('/classify_image', methods=['GET','POST'])
def classify_image():
    image_data= request.form['image_data']
    print(artifacts,image_data)
    print(util.classify_image(image_data,artifacts))
    response = jsonify(util.classify_image(image_data,artifacts))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
    
    
    
if __name__== "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    
    #app.run(Host=0.0.0.0,Port=5000,debug=True)
    log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))
