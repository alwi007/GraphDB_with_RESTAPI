from flask_restful import Resource, Api
from SPARQLWrapper import GET, JSON, JSONLD, POST, TURTLE, SPARQLWrapper
import json
from flask import Flask, render_template, make_response, request, jsonify
import sparql_dataframe
from pandas.io.json import json_normalize
import pandas as pd
import datetime
import uuid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import base64


# Flask
app = Flask(__name__)
api = Api(app)


# Method for General Select SPARQL Query
@app.route('/query', methods=['GET', 'POST'])
def query():
        sparql = SPARQLWrapper("http://localhost:port/repositories/<repositoryID>")

        sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX URI: <your URI>
        SELECT * WHERE  { ?s ?p ?o} limit 100
        """)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        result = result['results']['bindings']
        result = json.dumps(result)
        return result
return HTMLform.html

# Method for Insert SPARQL Query
@app.route('/result', methods=['GET', 'POST'])
def result():
    json=request.get_json()
    json_new=json
    Reading1=json.get('Reading Value1 from the device')
    Reading2=json.get('Reading Value2 from the device')
    Reading3=json.get('Reading Value3 from the device')
    -------
    if Reading1 is None:
        print("No reading1")
    else:
        sparql = SPARQLWrapper("http://localhost:port/repositories/<repositoryID>/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX URI: <Your URI>
            INSERT DATA {"""INSERT QUERY.} """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if Reading2 is None:
        print("No reading2")
    else:
        sparql = SPARQLWrapper("http://localhost:port/repositories/<repositoryID>/statements")
        sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX URI: <Your URI>
            INSERT DATA {"""INSERT QUERY.} """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    if Reading3 is None:
        print("No reading3")
    else:
        sparql = SPARQLWrapper("http://localhost:port/repositories/<repositoryID>/statements")        	sparql.setQuery("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                        PREFIX URI: <Your URI>
            INSERT DATA {"""INSERT QUERY.} """)
        sparql.setReturnFormat(JSON)
        sparql.setMethod(POST)
        results = sparql.query()

    return 'ok'


# Method for Plot
@app.route('/plot', methods=['GET', 'POST'])
def plot():
    endpoint = ("http://localhost:port/repositories/<repositoryID>")
    if request.method == "POST":
        Item1 = request.form["Item1ID"]
        Item2= request.form["Item12ID"]
        Item3 = request.form["Item3ID"]
        Item4= request.form["Item4ID"]
        
        q = ("""
                SPARQL SELECT Query
                """)
        result = sparql_dataframe.get(endpoint, q, post=True)
        img = BytesIO()

        y = result['val']
        x = result['time']

        plt.plot(y)

        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        print(y)

        return render_template('plot.html', plot_url=plot_url)

    # Front End form to get the variable entries from user
    return render_template('form.html')





if__name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='7207', threaded=True)
