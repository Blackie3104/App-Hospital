from paciente import Paciente
from signos_vitales import SignosVitales
from informacion_hospitalaria import InformacionHospitalaria

class HospitalUI:
    def __init__(self):
        self.sections = {
            '1': "Datos del paciente",
            '2': "Signos vitales",
            '3': "Almacenar información de manera segura y confiable",
            '4': "Mostrar información guardada",
            '5': "Notas de evolución",
            '6': "Imágenes diagnósticas",
            '7': "Resultados de exámenes de laboratorio",
            '8': "Medicamentos formulados"
        }
        self.paciente = Paciente()
        self.signos_vitales = SignosVitales()
        self.informacion_hospitalaria = InformacionHospitalaria()

    def display_menu(self):
        print("\nGESTION HOSPITALITARIA DEL HOSPITAL SAN VICENTE")
        print("Por favor, seleccione la sección que desea ver:")
        for key, value in self.sections.items():
            print(f"{key}. {value}")

    def show_section(self):
        while True:
            self.display_menu()
            section_number = input("Ingrese el número de la sección que desea ver (0 para salir): ")

            if section_number == '0':
                print("Saliendo del programa...")
                break
            elif section_number == '1':
                self.paciente.input_data()
                self.paciente.show_data()
            elif section_number == '2':
                self.signos_vitales.input_data()
                self.signos_vitales.show_data()
            elif section_number == '3':
                self.informacion_hospitalaria.store_information(self.paciente, self.signos_vitales)
            elif section_number == '4':
                self.informacion_hospitalaria.show_saved_information()
            elif section_number in self.sections:
                print(f"Mostrar {self.sections[section_number]}")
            else:
                print("Número de sección inválido. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    ui = HospitalUI()
    ui.show_section()















