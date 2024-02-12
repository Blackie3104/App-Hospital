class Paciente:
  def __init__(self):
      self.data = {}

  def input_data(self):
      print("\nPor favor, ingrese los datos del paciente:")
      self.data['documento'] = input("Documento: ")
      self.data['nombre'] = input("Nombre: ")
      self.data['sexo'] = input("Sexo: ")
      self.data['fecha_nacimiento'] = input("Fecha de nacimiento (YYYY-MM-DD): ")

  def show_data(self):
      if self.data:
          print("\nDatos del paciente:")
          for key, value in self.data.items():
              print(f"{key.capitalize()}: {value}")
      else:
          print("\nNo se han ingresado datos del paciente.")