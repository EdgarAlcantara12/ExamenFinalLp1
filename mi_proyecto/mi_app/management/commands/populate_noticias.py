from django.core.management.base import BaseCommand
from mi_app.models import CategoriaHerramienta, Herramienta

class Command(BaseCommand):
    help = 'Popula la base de datos con herramientas y enlaces'

    def handle(self, *args, **kwargs):
        # Categorías y herramientas
        datos = {
            "Criptografía y Seguridad de Datos": [
                {"nombre": "VeraCrypt", "enlace": "https://www.veracrypt.fr/"},
                {"nombre": "Hashcat", "enlace": "https://hashcat.net/hashcat/"},
                {"nombre": "Gpg4win", "enlace": "https://gpg4win.org/"},
                {"nombre": "Cryptomator", "enlace": "https://cryptomator.org/"},
            ],
            "Herramientas de Seguridad en IoT": [
                {"nombre": "Shodan", "enlace": "https://www.shodan.io/"},
                {"nombre": "Firmware Analysis Toolkit (FAT)", "enlace": "https://github.com/attify/firmware-analysis-toolkit"},
                {"nombre": "IoT Inspector", "enlace": "https://www.iot-inspector.com/"},
                {"nombre": "OpenVAS", "enlace": "https://www.greenbone.net/en/openvas/"},
                {"nombre": "Fing", "enlace": "https://www.fing.com/"},
                {"nombre": "IoTSeeker", "enlace": "https://security.radware.com/"},
            ],
            "Análisis Forense": [
                {"nombre": "Autopsy", "enlace": "https://www.sleuthkit.org/autopsy/"},
                {"nombre": "EnCase", "enlace": "https://www.guidancesoftware.com/encase-forensic"},
                {"nombre": "FTK (Forensic Toolkit)", "enlace": "https://accessdata.com/products-services/forensic-toolkit-ftk"},
                {"nombre": "X-Ways Forensics", "enlace": "https://www.x-ways.net/forensics/"},
                {"nombre": "Cellebrite UFED", "enlace": "https://www.cellebrite.com/en/home/"},
                {"nombre": "Sleuth Kit", "enlace": "https://www.sleuthkit.org/"},
            ],
            "Monitoreo de Red": [
                {"nombre": "Zabbix", "enlace": "https://www.zabbix.com/"},
                {"nombre": "PRTG Network Monitor", "enlace": "https://www.paessler.com/prtg"},
                {"nombre": "NetFlow Analyzer", "enlace": "https://www.manageengine.com/products/netflow/"},
            ],
        }

        # Agregar datos a la base de datos
        for categoria_nombre, herramientas in datos.items():
            categoria, created = CategoriaHerramienta.objects.get_or_create(nombre=categoria_nombre)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Categoría creada: {categoria_nombre}'))

            for herramienta_data in herramientas:
                herramienta, created = Herramienta.objects.get_or_create(
                    nombre=herramienta_data['nombre'],
                    defaults={
                        'descripcion': f"Descripción de {herramienta_data['nombre']}",
                        'enlace': herramienta_data['enlace'],
                        'categoria': categoria,
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Herramienta creada: {herramienta.nombre}'))
                else:
                    herramienta.enlace = herramienta_data['enlace']
                    herramienta.save()
                    self.stdout.write(self.style.WARNING(f'Herramienta actualizada: {herramienta.nombre}'))
