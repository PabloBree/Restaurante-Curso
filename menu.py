from tkinter import *
import sqlite3
#from SQLite.ejercicio_restaurant import restaurante as Resto

#Config de la raiz
root = Tk()
root.title("El Pollo Loco")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root,text="   El Pollo Loco   ",fg='darkgreen',font=('Times New Roman', 28, "bold italic")).pack()
Label(root,text="Menu del dia",fg='green',font=('Times New Roman', 24, "bold italic")).pack()

#Separacion de titulos
Label(root,text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

#Buscar las categorias y platos de la BD
cate_disp = cursor.execute("SELECT * FROM categoria").fetchall()
for ctg in cate_disp:
    Label(root,text=ctg[1],fg='black',font=('Times New Roman', 20, "bold italic")).pack()
    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(ctg[0])).fetchall()
    for pt in platos:
        Label(root, text=pt[1], fg='grey', font=('Times New Roman', 16, "bold italic")).pack()

Label(root,text="").pack()
Label(root,text="$12(IVA inc.)",fg='darkgreen', font=('Times New Roman', 28, "bold italic")).pack(anchor='e')

conexion.close()




#bucle de la aplicacion
root.mainloop()
