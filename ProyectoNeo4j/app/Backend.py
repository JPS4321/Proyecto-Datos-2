from neo4j import GraphDatabase

def getnodes(tx, genero, empresa, plataforma):
    result = tx.run("MATCH (x) WHERE x.Genero =$genero AND x.Empresa =$empresa AND x.Plataforma =$plataforma RETURN x",
                    genero=genero, 
                    empresa=empresa, 
                    plataforma=plataforma)

    nodes = []
    for record in result:
        node = record['x']
        nodes.append(dict(node))  # Convert the node's properties to a dictionary

    return nodes

graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "12345678"))
#graphdb = GraphDatabase.driver(uri="bolt://3.84.62.250:7687", auth=("neo4j", "blasts-launchers-beats"))

def obtener(genero, empresa, plataforma):
    with graphdb.session() as session:
        nodes = session.read_transaction(getnodes, genero, empresa, plataforma)
    return nodes


def agregar(nombre, genero, empresa, plataforma):
    with graphdb.session() as session:
        nodes = session.write_transaction(create_node, nombre, genero, empresa, plataforma)
    return nodes

def eliminar(nombre, genero, empresa, plataforma):
    with graphdb.session() as session:
        session.write_transaction(delete_node, nombre, genero, empresa, plataforma)

def create_node(tx, nombre, genero, empresa, plataforma):
    result = tx.run("CREATE (n:Node {Nombre: $nombre, Genero: $genero, Empresa: $empresa, Plataforma: $plataforma}) RETURN n",
                    nombre=nombre,
                    genero=genero, 
                    empresa=empresa, 
                    plataforma=plataforma)
    nodes = []
    for record in result:
        node = record['n']
        nodes.append(dict(node))
    return nodes

def delete_node(tx, nombre, genero, empresa, plataforma):
    tx.run("MATCH (n {Nombre: $nombre, Genero: $genero, Empresa: $empresa, Plataforma: $plataforma}) DETACH DELETE n",
           nombre=nombre,
           genero=genero,
           empresa=empresa,
           plataforma=plataforma)