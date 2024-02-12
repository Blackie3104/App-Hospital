class InformacionHospitalaria:
  def __init__(self):
      self.data = []

  def store_information(self, paciente, signos_vitales):
      if paciente.data and signos_vitales.data:
          self.data.append({'paciente': paciente.data.copy(), 'signos_vitales': signos_vitales.data.copy()})
          print("La información del paciente y los signos vitales ha sido almacenada de manera segura y confiable.")
          paciente.data.clear()
          signos_vitales.data.clear()
      else:
          print("No se han ingresado datos del paciente o signos vitales.")

  def show_saved_information(self):
      if self.data:
          print("\nInformación guardada:")
          for idx, info in enumerate(self.data, start=1):
              print(f"\nRegistro {idx}:")
              print("Datos del paciente:")
              for key, value in info['paciente'].items():
                  print(f"{key.capitalize()}: {value}")
              print("\nSignos vitales del paciente:")
              for key, value in info['signos_vitales'].items():
                  print(f"{key.capitalize()}: {value}")
      else:
          print("\nNo hay información guardada.")