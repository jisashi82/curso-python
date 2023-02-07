import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model import peliculaDAO

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root=root
        self.config(width=480, height=320, background='azure')
        
        self.id_pelicula=None
        
        self.campos_pelicula()
        self.tabla_peliculas()
        self.deshabilita_campos()
        self.pack()
    
    #Crea una etiqueta: nom_etiqueta el texto que se mostrara, lista[row,column,padx,pady]    
    def etiqueta(self,nom_etiqueta,lista):
        etiqueta=tk.Label(self,text=nom_etiqueta)
        etiqueta.config(font=('Arial',12,'bold'))
        etiqueta.grid(row=lista[0], column=lista[1], padx=lista[2], pady=lista[3])
        return etiqueta
    
    def campos_pelicula(self):
        #labels de cada campo        
        self.label_nombre= self.etiqueta('Nombre',[0,0,10,10])      
        self.label_duracion=self.etiqueta('Duracion', [1,0,10,10]) 
        self.label_genero=self.etiqueta('Genero', [2,0,10,10])
         
        #Entrys de cada campo
        self.mi_nombre=tk.StringVar()
        entry_config={'width':50, 'state':'disabled', 'font':('Arial',12)}
        self.entry_nombre=tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(entry_config,)
        self.entry_nombre.grid(row=0,column=1, padx=10,pady=10, columnspan=2)
        
        self.mi_duracion=tk.StringVar()
        self.entry_duracion=tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(entry_config)
        self.entry_duracion.grid(row=1,column=1, padx=10,pady=10, columnspan=2)
        
        self.mi_genero=tk.StringVar()
        self.entry_genero=tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(entry_config)
        self.entry_genero.grid(row=2,column=1, padx=10,pady=10, columnspan=2)
        
        #Botones ---------------------------------------------------------------
        fuenteBtn=('Arial',11,'bold')
        self.boton_nuevo=tk.Button(self,text='Nuevo', command=self.nuevo_registro)
        self.boton_nuevo.config(width=20, font=fuenteBtn, fg='#f8f9f9', bg='#58d68d', cursor='hand2', activebackground='#a9dfbf')
        self.boton_nuevo.grid(row=4,column=0, padx=10,pady=10)
        
        self.boton_guardar=tk.Button(self,text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=fuenteBtn, fg='#f8f9f9', bg='#5dade2', cursor='hand2', activebackground='#aed6f1')
        self.boton_guardar.grid(row=4,column=1, padx=10,pady=10)
        
        self.boton_cancelar=tk.Button(self,text='Cancelar', command=self.deshabilita_campos)
        self.boton_cancelar.config(width=20, font=fuenteBtn, fg='#f8f9f9', bg='#ec7063', cursor='hand2', activebackground='#f5b7b1')
        self.boton_cancelar.grid(row=4,column=2, padx=10,pady=10)
    
    def nuevo_registro(self):
        self.id_pelicula=None
        self.habilitar_campos()
    
    def deshabilita_campos(self):
        self.mi_duracion.set('')
        self.mi_nombre.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        
        self.boton_guardar.config(state='disabled')    
        self.boton_cancelar.config(state='disabled')
    
    def habilitar_campos(self):
        self.mi_duracion.set('')
        self.mi_nombre.set('')
        self.mi_genero.set('')
        
        
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        
        self.boton_guardar.config(state='normal')    
        self.boton_cancelar.config(state='normal')
        
    def guardar_datos(self):
        pelicula=peliculaDAO.Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(), 
            self.mi_genero.get()
            )
        
        if self.id_pelicula == None:
            peliculaDAO.guardar(pelicula)
        else:
            peliculaDAO.editar(pelicula,self.id_pelicula)
        self.tabla_peliculas()
        self.deshabilita_campos()
        
    def editar_datos(self):
        try:
            self.id_pelicula=self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula=self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula=self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula=self.tabla.item(self.tabla.selection())['values'][2]
            
            self.habilitar_campos()
            
            self.entry_nombre.insert(0,self.nombre_pelicula)
            self.entry_duracion.insert(0,self.duracion_pelicula)
            self.entry_genero.insert(0,self.genero_pelicula)
        except:
            messagebox.showerror('Edicion de Datos', 'No ha seleccionado ningun registro')
            
    def eliminar_datos(self):
        try:
            self.id_pelicula=self.tabla.item(self.tabla.selection())['text']
            peliculaDAO.eliminar(self.id_pelicula)
            self.tabla_peliculas()
        except:
            messagebox.showwarning('Eliminando..','Seleccione un registro')
            
    def tabla_peliculas(self):
        self.lista_peliculas=peliculaDAO.listar()
        self.tabla=ttk.Treeview(self, columns=('Nombre','Duracion', 'Genero'))
        self.tabla.grid(row=5, column=0, columnspan=4)
        
        #scrollbar
        self.scrollbar = ttk.Scrollbar(self,orient=tk.VERTICAL, command=self.tabla.yview)
        self.scrollbar.grid(row=5, column=4, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scrollbar.set)
        
        #TITULOS DE CABeCERAS DE LA TABLA
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='NOMBRE')
        self.tabla.heading('#2',text='DURACION')
        self.tabla.heading('#3',text='GENERO')
        
        #RECORREMOS LA LISTA DE PELICULAS Y SE INSERTAN EN LA TABLA
        for p in self.lista_peliculas:
            self.tabla.insert('',tk.END,text=p[0],values=(p[1],p[2],p[3]))
        
        #Botones de Editar y Eliminar de la tabla
        fuenteBtn=('Arial',11,'bold')
        self.boton_editar=tk.Button(self,text='Editar', command=self.editar_datos)
        self.boton_editar.config(width=20, font=fuenteBtn, fg='#f8f9f9', bg='#58d68d', cursor='hand2', activebackground='#a9dfbf')
        self.boton_editar.grid(row=6,column=1, padx=10,pady=10)
        
        self.boton_eliminar=tk.Button(self,text='Eliminar', command=self.eliminar_datos)
        self.boton_eliminar.config(width=20, font=fuenteBtn, fg='#f8f9f9', bg='#ec7063', cursor='hand2', activebackground='#f5b7b1')
        self.boton_eliminar.grid(row=6,column=2, padx=10,pady=10)
        
        
        
def barra_menu(root:tk.Tk):
    
        barraMenu=tk.Menu(root)        
        root.config(menu=barraMenu,width=480, height=320)
        
        menu_inicio=tk.Menu(barraMenu, tearoff=0)
        barraMenu.add_cascade(label='Inicio', menu=menu_inicio)
        
        menu_inicio.add_command(label='Crear registro en BD', command=peliculaDAO.crear_tabla)
        menu_inicio.add_command(label='Eliminar BD', command=peliculaDAO.borrar_tabla)
        menu_inicio.add_command(label='Salir', command=root.destroy)
        
        barraMenu.add_cascade(label='Consulta', menu='')
        barraMenu.add_cascade(label='Configuracion', menu='') 
        barraMenu.add_cascade(label='Ayuda', menu='')
        
         