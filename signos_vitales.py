class SignosVitales:
  def __init__(self):
      self.data = {}

  def input_data(self):
      print("\nPor favor, ingrese los signos vitales del paciente:")
      self.data['presión_arteria'] = input("Presión arteria: ")
      self.data['temperatura'] = input("Temperatura: ")
      self.data['saturación_O2'] = input("Saturación O2: ")
      self.data['frecuencia_respiratoria'] = input("Frecuencia respiratoria: ")

  def show_data(self):
      if self.data:
          print("\nSignos vitales del paciente:")
          for key, value in self.data.items():
              print(f"{key.capitalize()}: {value}")
      else:
          print("\nNo se han ingresado signos vitales del paciente.")