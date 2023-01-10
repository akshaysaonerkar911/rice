from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

model = pickle.load(open("rice.pkl","rb"))


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/rice",methods=["POST","GET"])
def rice():
    id=int(request.form.get("id"))
    Area=int(request.form.get("Area"))
    MajorAxisLength=float(request.form.get("MajorAxisLength"))
    MinorAxisLength=float(request.form.get("MinorAxisLength"))
    Eccentricity=float(request.form.get("Eccentricity"))
    ConvexArea=int(request.form.get("ConvexArea"))
    EquivDiameter=float(request.form.get("EquivDiameter"))
    Extent=float(request.form.get("Extent"))
    Perimeter=float(request.form.get("Perimeter"))
    Roundness=float(request.form.get("Roundness"))
    AspectRation=float(request.form.get("AspectRation"))

    result = model.predict([[id,Area,MajorAxisLength,MinorAxisLength,Eccentricity,ConvexArea,EquivDiameter,Extent,Perimeter,Roundness,AspectRation]])
    

    if result[0]==0:
        return "this rice is basmati"
    else:
        return "this is not basmati rice"












if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)