from django.test import TestCase
from dailyhub.models import Contacto

class ContactoModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ContactoModelTest, cls).setUpClass()
        cls.testContacto = Contacto(nombre="Baltazar", apellido="Díaz", email="baltazardiaz1@gmail.com", direccion='Ac. Manquehue', preferencia="Deportes")
        cls.testContacto.save()

    def testContactoToStringEmail(self):
        self.assertEquals(self.testContacto.email, "baltazardiaz1@gmail.com")

    def testGetById(self):
        self.assertEquals(Contacto.getById(1), self.testContacto)

    def testShortName(self):
        self.assertEquals(self.testContacto.nombre, "Baltazar")