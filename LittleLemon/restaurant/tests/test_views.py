from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemView

class MenuViewTest(TestCase):
    def setUp(self):
        # Temporarily remove authentication requirement
        MenuItemView.permission_classes = []  # 🔓 disables IsAuthenticated

        self.item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IceCream")
        self.assertContains(response, "80.00")  # Decimal precision
        self.assertContains(response, "100")
