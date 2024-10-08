from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from bs4 import BeautifulSoup

class FileUploadButtonTest(TestCase):
    def test_upload_button_exists(self):
        # Reemplaza 'upload_file_view' por el nombre de tu vista
        url = reverse('upload_file')
        
        # Realiza una petición GET a la vista
        response = self.client.get(url)
        
        # Asegúrate de que la respuesta sea 200 (éxito)
        self.assertEqual(response.status_code, 200)
        
        # Utiliza BeautifulSoup para analizar el HTML de la respuesta
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Verifica que exista un input de tipo "file" en el formulario
        upload_button = soup.find('button', {'type': 'submit'})
        self.assertIsNotNone(upload_button, "El botón para subir archivos no existe en la página")

