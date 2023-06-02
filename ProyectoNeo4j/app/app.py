# Importamos las bibliotecas necesarias y funciones desde Backend.
from flask import Flask, request, render_template
from Backend import getnodes, obtener, agregar, create_node, delete_node, eliminar

# Creamos la instancia de nuestra aplicación Flask.
app = Flask(__name__)

# Definimos la ruta principal '/', que renderiza el template 'Index.html'.
@app.route('/')
def Index():
    return render_template('Index.html')

# Definimos la ruta '/Empresas', que renderiza el template 'Empresas.html'.
@app.route('/Empresas')
def Empresas():
    return render_template('Empresas.html') 

# Definimos la ruta '/Generos', que renderiza el template 'Generos.html'.
@app.route('/Generos')
def Generos():
    return render_template('Generos.html') 

# Definimos la ruta '/Plataformas', que renderiza el template 'Plataformas.html'.
@app.route('/Plataformas')
def Plataformas():
    return render_template('Plataformas.html')

# Definimos la ruta '/buscar' para buscar nodos en la base de datos, la solicitud debe ser POST.
@app.route('/buscar', methods=['POST'])
def buscar():
    genero = request.form['Genero']
    empresa = request.form['Empresa']
    plataforma = request.form['Plataforma']

    nodes = obtener(genero, empresa, plataforma)  # Buscamos nodos.

    print(nodes)  # Imprimimos los nodos.

    # Renderizamos 'Index.html' con los nodos obtenidos.
    return render_template('Index.html', nodes=nodes)

# Definimos la ruta '/input' para agregar nodos en la base de datos, la solicitud debe ser POST.
@app.route('/input', methods=['POST'])
def input():
    nombrein= request.form.get('NombreIN')
    plataformin = request.form.get('PlataformaIN')
    generoin = request.form.get('GeneroIN')
    empresain = request.form.get('EmpresaIN')

    # Comprobamos que todos los campos necesarios están presentes.
    if nombrein and plataformin and generoin and empresain:
        nodes2 = agregar(nombrein, generoin, empresain, plataformin)  # Agregamos el nodo.
        print(nodes2)  # Imprimimos el resultado.

        # Renderizamos 'Index.html' con los nuevos nodos.
        return render_template('Index.html', nodes2=nodes2)
    else:
        # Devolvemos un error si no se proporcionaron todos los campos necesarios.
        return "Error: Not all required fields were provided.", 400

# Definimos la ruta '/delete' para eliminar nodos en la base de datos, la solicitud debe ser POST.
@app.route('/delete', methods=['POST'])
def delete():
    nombre = request.form.get('NombreDEL')
    genero = request.form.get('GeneroDEL')
    empresa = request.form.get('EmpresaDEL')
    plataforma = request.form.get('PlataformaDEL')

    # Comprobamos que todos los campos necesarios están presentes.
    if nombre and genero and empresa and plataforma:
        elim = eliminar(nombre, genero, empresa, plataforma)  # Eliminamos el nodo.

        # Renderizamos 'Index.html' con la confirmación de eliminación.
        return render_template('Index.html', elim=elim)
    else:
        # Devolvemos un error si no se proporcionaron todos los campos necesarios.
        return "Error: Not all required fields were provided.", 400

# Ejecutamos nuestra aplicación en modo debug y puerto 5000.
if __name__ == '__main__':
    app.run(debug=True, port=5000)
