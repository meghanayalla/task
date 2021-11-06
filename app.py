
from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify,request


app =Flask(__name__)

app.config["MONGO_DBNAME"] = "task"
app.config["MONGO_URI"]="mongodb+srv://admin:admin@cluster0.f7buy.mongodb.net/task?retryWrites=true&w=majority"


mongo =PyMongo(app)


@app.route('/')
def hello():
   return 'Hello !'


# 127.0.0.1:5000/get/-50.1/50.96
@app.route('/get/<float(signed=True):lon>/<float(signed=True):lat>',methods = ['GET'])
def get_query(lon,lat):
    if (lon>-180) and (lon<180) and (lat>-90) and (lat<90):
        data = mongo.db.car_rental
        cars =[]
        _cars = data.find({"loc.coordinates":{"$near":[-54,63]}}).limit(3)
        for a in _cars:
            cars.append({"id":a['driver'],'longitude':a['loc']['coordinates'][0],'latitude':a['loc']['coordinates'][1],'number_plate':a['number_plate']})

        return jsonify(cars)
    else:
        return("Please check the Latitudes and Longitudes range")
    



    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')