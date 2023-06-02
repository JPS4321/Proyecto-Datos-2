# Importamos la biblioteca neo4j para interactuar con la base de datos Neo4j.
from neo4j import GraphDatabase

# Función para obtener nodos de la base de datos que coinciden con los criterios proporcionados.
def getnodes(tx, genero, empresa, plataforma):
    # Ejecutamos la consulta Cypher.
    result = tx.run("MATCH (x) WHERE x.Genero =$genero AND x.Empresa =$empresa AND x.Plataforma =$plataforma RETURN x",
                    genero=genero, 
                    empresa=empresa, 
                    plataforma=plataforma)

    nodes = []
    # Convertimos los nodos en un diccionario y los agregamos a una lista.
    for record in result:
        node = record['x']
        nodes.append(dict(node))  

    return nodes

# Establecemos una conexión con la base de datos Neo4j.
#graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "12345678"))  #ESTA ES LA CONEXION LOCAL
graphdb = GraphDatabase.driver(uri="bolt://3.84.62.250:7687", auth=("neo4j", "blasts-launchers-beats")) #ESTA ES LA CONEXION DEL NEO4J A INTERNET

# Función para obtener nodos de la base de datos que coinciden con los criterios proporcionados.
def obtener(genero, empresa, plataforma):
    # Abrimos una nueva sesión y ejecutamos la transacción de lectura.
    with graphdb.session() as session:
        nodes = session.read_transaction(getnodes, genero, empresa, plataforma)
    return nodes

# Función para agregar un nodo a la base de datos.
def agregar(nombre, genero, empresa, plataforma):
    # Abrimos una nueva sesión y ejecutamos la transacción de escritura.
    with graphdb.session() as session:
        nodes = session.write_transaction(create_node, nombre, genero, empresa, plataforma)
    return nodes

# Función para eliminar un nodo de la base de datos.
def eliminar(nombre, genero, empresa, plataforma):
    # Abrimos una nueva sesión y ejecutamos la transacción de escritura.
    with graphdb.session() as session:
        session.write_transaction(delete_node, nombre, genero, empresa, plataforma)

# Función para crear un nodo en la base de datos.
def create_node(tx, nombre, genero, empresa, plataforma):
    # Ejecutamos la consulta Cypher.
    result = tx.run("CREATE (n:Node {Nombre: $nombre, Genero: $genero, Empresa: $empresa, Plataforma: $plataforma}) RETURN n",
                    nombre=nombre,
                    genero=genero, 
                    empresa=empresa, 
                    plataforma=plataforma)

    nodes = []
    # Convertimos los nodos en un diccionario y los agregamos a una lista.
    for record in result:
        node = record['n']
        nodes.append(dict(node))

    return nodes

# Función para eliminar un nodo de la base de datos.
def delete_node(tx, nombre, genero, empresa, plataforma):
    # Ejecutamos la consulta Cypher.
    tx.run("MATCH (n {Nombre: $nombre, Genero: $genero, Empresa: $empresa, Plataforma: $plataforma}) DETACH DELETE n",
           nombre=nombre,
           genero=genero,
           empresa=empresa,
           plataforma=plataforma)
