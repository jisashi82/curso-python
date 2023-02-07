from .conexiondb import ConexionDB
from tkinter import messagebox


def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo('Crear Registro', 'se creo la tabla en la BD')
    except:
        messagebox.showwarning('Crear Registr', 'La tabla ya esta creada')


def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo('Eliminar tabla', 'Se elimino la tabla de la BD')
    except:
        messagebox.showerror('Eliminar Tabla', 'La tabla fue eliminada')


class Pelicula:
    def __init__(self, nombre, duracion, genero) -> None:
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self) -> str:
        return f'Pelicula: {self.nombre}, Duracion: {self.duracion}, Genero: {self.genero}'


def guardar(pelicula: Pelicula):
    conexion = ConexionDB()
    sql = f"""
    INSERT INTO peliculas(nombre,duracion,genero) 
    VALUES('{pelicula.nombre}', '{pelicula.duracion}','{pelicula.genero}')
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror('Conexion a la Tabla',
                             'La tabla peliculas no esta creada')


def listar():
    conexion = ConexionDB()
    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        messagebox.showerror(
            'Conexion', 'No existe la tabla para recuperar registros')

    return lista_peliculas


def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql = f"""
    UPDATE peliculas 
    SET nombre='{pelicula.nombre}', duracion='{pelicula.duracion}', genero='{pelicula.genero}'
    WHERE id_pelicula= {id_pelicula}
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror('Conexion', e.__str__())
