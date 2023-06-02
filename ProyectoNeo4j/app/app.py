from flask import Flask, request, render_template
from Backend import getnodes, obtener, agregar, create_node, delete_node, eliminar
#from Backend import getnodes 

app = Flask(__name__)

@app.route('/')
def Index():

    return render_template('Index.html') 


@app.route('/Empresas')
def Empresas():

    return render_template('Empresas.html') 


@app.route('/Generos')
def Generos():

    return render_template('Generos.html') 


@app.route('/Plataformas')
def Plataformas():

    return render_template('Plataformas.html') 



@app.route('/buscar', methods=['POST'])
def buscar():
    genero = request.form['Genero']
    empresa = request.form['Empresa']
    plataforma = request.form['Plataforma']

    nodes = obtener(genero, empresa, plataforma)

    print(nodes)

    return render_template('Index.html', nodes=nodes)


@app.route('/input', methods=['POST'])
def input():
    nombrein= request.form.get('NombreIN')
    plataformin = request.form.get('PlataformaIN')
    generoin = request.form.get('GeneroIN')
    empresain = request.form.get('EmpresaIN')

    if nombrein and plataformin and generoin and empresain:
        nodes2 = agregar(nombrein, generoin, empresain, plataformin)
        print(nodes2)
        return render_template('Index.html', nodes2=nodes2)
    else:
        return "Error: Not all required fields were provided.", 400
    

@app.route('/delete', methods=['POST'])
def delete():
    nombre = request.form.get('NombreDEL')
    genero = request.form.get('GeneroDEL')
    empresa = request.form.get('EmpresaDEL')
    plataforma = request.form.get('PlataformaDEL')

    if nombre and genero and empresa and plataforma:
        elim = eliminar(nombre, genero, empresa, plataforma)
        return render_template('Index.html', elim=elim)
    else:
        return "Error: Not all required fields were provided.", 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
