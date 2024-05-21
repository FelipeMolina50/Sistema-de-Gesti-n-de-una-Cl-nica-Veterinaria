import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from typing import List


class Persona:
    def __init__(self, nombre: str, telefono: str):
        self.__nombre = nombre
        self.__telefono = telefono

    @property
    def get_nombre(self):
        return self.__nombre

    @get_nombre.setter
    def get_nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def get_telefono(self):
        return self.__telefono

    @get_telefono.setter
    def get_telefono(self, telefono: str):
        self.__telefono = telefono

class Propietario(Persona):
    def __init__(self, nombre: str, telefono: str, direccion: str):
        super().__init__(nombre, telefono)
        self.__direccion = direccion

    @property
    def get_direccion(self):
        return self.__direccion

    @get_direccion.setter
    def get_direccion(self, direccion: str):
        self.__direccion = direccion

class Paciente:
    def __init__(self, nombre: str, especie: str, raza: str, edad: int, propietario: Propietario):
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__propietario = propietario
        self.__historial_medico = []

    @property
    def get_nombre(self):
        return self.__nombre

    @get_nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def get_especie(self):
        return self.__especie

    @get_especie.setter
    def especie(self, especie: str):
        self.__especie = especie

    @property
    def get_raza(self):
        return self.__raza

    @get_raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def get_edad(self):
        return self.__edad

    @get_edad.setter
    def edad(self, edad: int):
        self.__edad = edad

    @property
    def propietario(self):
        return self.__propietario

    @property
    def historial_medico(self):
        return self.__historial_medico

    def agregar_historial(self, consulta: str):
        self.__historial_medico.append(consulta)

class Cita:
    def __init__(self, paciente: Paciente, fecha_hora: datetime, motivo: str):
        self.__paciente = paciente
        self.__fecha_hora = fecha_hora
        self.__motivo = motivo

    @property
    def paciente(self):
        return self.__paciente

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    @property
    def motivo(self):
        return self.__motivo

class Medicamento:
    def __init__(self, nombre: str, descripcion: str, precio: float, stock: int):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def actualizar_stock(self, cantidad: int):
        self.__stock += cantidad

    def actualizar_precio(self, nuevo_precio: float):
        self.__precio = nuevo_precio

class Suministro:
    def __init__(self, nombre: str, descripcion: str, precio: float, stock: int):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def actualizar_stock(self, cantidad: int):
        self.__stock += cantidad

    def actualizar_precio(self, nuevo_precio: float):
        self.__precio = nuevo_precio

class InventarioMedicamentos(Medicamento, Suministro):
    def __init__(self, nombre: str, descripcion: str, precio: float, stock: int):
        Medicamento.__init__(self, nombre, descripcion, precio, stock)
        Suministro.__init__(self, nombre, descripcion, precio, stock)

    def generar_alerta_stock(self):
        if self.stock < 10:
            print(f"Alerta: El stock de {self.nombre} es bajo (Cantidad: {self.stock}).")

class VetClinicApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Clínica Veterinaria")
        self.geometry("800x600")

        self.pacientes = []
        self.citas = []
        self.inventario = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Registro de Pacientes").grid(row=0, column=0, columnspan=2)
        tk.Label(self, text="Nombre:").grid(row=1, column=0)
        tk.Label(self, text="Especie:").grid(row=2, column=0)
        tk.Label(self, text="Raza:").grid(row=3, column=0)
        tk.Label(self, text="Edad:").grid(row=4, column=0)
        tk.Label(self, text="Propietario:").grid(row=5, column=0)
        tk.Label(self, text="Teléfono:").grid(row=6, column=0)
        tk.Label(self, text="Dirección:").grid(row=7, column=0)

        self.nombre_paciente = tk.Entry(self)
        self.nombre_paciente.grid(row=1, column=1)
        self.especie_paciente = tk.Entry(self)
        self.especie_paciente.grid(row=2, column=1)
        self.raza_paciente = tk.Entry(self)
        self.raza_paciente.grid(row=3, column=1)
        self.edad_paciente = tk.Entry(self)
        self.edad_paciente.grid(row=4, column=1)
        self.nombre_propietario = tk.Entry(self)
        self.nombre_propietario.grid(row=5, column=1)
        self.telefono_propietario = tk.Entry(self)
        self.telefono_propietario.grid(row=6, column=1)
        self.direccion_propietario = tk.Entry(self)
        self.direccion_propietario.grid(row=7, column=1)

        tk.Button(self, text="Registrar Paciente", command=self.registrar_paciente).grid(row=8, column=0, columnspan=2)

        tk.Label(self, text="Ver Historial Médico").grid(row=0, column=2, columnspan=2)
        tk.Label(self, text="Seleccione Paciente:").grid(row=1, column=2)

        self.lista_pacientes = tk.Listbox(self)
        self.lista_pacientes.grid(row=2, column=2, rowspan=6)
        tk.Button(self, text="Ver Historial", command=self.ver_historial).grid(row=8, column=2)

        self.historial_text = tk.Text(self, width=50, height=20)
        self.historial_text.grid(row=2, column=3, rowspan=6)

    def registrar_paciente(self):
        nombre = self.nombre_paciente.get()
        especie = self.especie_paciente.get()
        raza = self.raza_paciente.get()
        edad = int(self.edad_paciente.get())
        propietario_nombre = self.nombre_propietario.get()
        propietario_telefono = self.telefono_propietario.get()
        propietario_direccion = self.direccion_propietario.get()

        propietario = Propietario(propietario_nombre, propietario_telefono, propietario_direccion)
        nuevo_paciente = Paciente(nombre, especie, raza, edad, propietario)
        self.pacientes.append(nuevo_paciente)
        self.lista_pacientes.insert(tk.END, nombre)

        messagebox.showinfo("Información", f"Paciente {nombre} registrado con éxito.")

        self.nombre_paciente.delete(0, tk.END)
        self.especie_paciente.delete(0, tk.END)
        self.raza_paciente.delete(0, tk.END)
        self.edad_paciente.delete(0, tk.END)
        self.nombre_propietario.delete(0, tk.END)
        self.telefono_propietario.delete(0, tk.END)
        self.direccion_propietario.delete(0, tk.END)

    def ver_historial(self):
        seleccion = self.lista_pacientes.curselection()
        if seleccion:
            indice = seleccion[0]
            paciente = self.pacientes[indice]
            historial = paciente.historial_medico
            self.historial_text.delete(1.0, tk.END)
            if historial:
                for entrada in historial:
                    self.historial_text.insert(tk.END, entrada + "\n")
            else:
                self.historial_text.insert(tk.END, "No hay historial médico para este paciente.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un paciente para ver su historial.")

if __name__ == "__main__":
    app = VetClinicApp()
    app.mainloop()