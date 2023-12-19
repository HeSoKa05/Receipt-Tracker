from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ReceiptModel


class UserTest(TestCase):
    """
    Testing user authentications like creating an account and logging-in
    """

    def create_user_test(self):
        response = self.client.post(reverse('receipt_tracker_app:register'), {
            'username': 'testuser',
            'password1': 'testpass',
            'password2': 'testpass'
        })
        self.assertEqual(response.status_code, 302)  # to check if user is redirected after successful registration
        # checking if the user is created
        existed_user = User.objects.filter(username='testuser', password='testpass').exists()
        self.assertTrue(existed_user)

    def login_user_test(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)  # check if user is redirected after successful login-in

        # check if the user is logged in
        logged_in_user = '_auth_user_id' in self.client.session
        self.assertTrue(logged_in_user)

        # returning logged in user for future operations
        return self.user


class ReceiptModelTest(TestCase):
    """
    Testing Receipt Model: create, retrieve
    """

    def user_log_in(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_receipt_model(self):
        """
        Testing objects creations in the ReceiptModel model.
        """
        self.user_log_in()  # user should be logged in to be able to create a receipt
        receipt = ReceiptModel.objects.create(user=self.user,
                                              store_name='test store',
                                              item_list='test item list',
                                              total_amount='3',
                                              description='test description')
        # aserting that the receipt object is created successfully
        self.assertEqual(receipt.store_name, 'test store')
        self.assertEqual(receipt.item_list, 'test item list')
        self.assertEqual(receipt.total_amount, '3')
        self.assertEqual(receipt.description, 'test description')


class ReceiptViewTest(TestCase):
    def user_log_in(self):
        """
        Testing a user logging in operation
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_receipt_view(self):
        """
        Testing a receipt view response code if it 200
        """
        self.user_log_in()
        response = self.client.get(reverse('receipt_tracker_app:receipt_list'))
        self.assertEqual(response.status_code, 200)

    def test_receipt_detail_view(self):
        """
        Testing the detail view response code of a receipt after creating it.
        """
        self.user_log_in()
        receipt = ReceiptModel.objects.create(user=self.user,
                                              store_name='test store 2',
                                              item_list='item1, item2',
                                              description='receipt description',
                                              total_amount=1)
        response = self.client.get(reverse('receipt_tracker_app:receipt_detail', args=(receipt.id,)))
        self.assertEqual(response.status_code, 200)


class ReceiptUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.receipt = ReceiptModel.objects.create(user=self.user,
                                                   store_name='store test',
                                                   item_list='items test',
                                                   total_amount=14)

    def receipt_update_test(self):
        url = reverse('receipt_tracker_app:receipt_update', args=(self.receipt.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Receipt Update')
        # trying to update some data
        response = self.client.post(url, {'total_amount': 4,
                                          'description': 'test description'})
        self.assertEqual(response.status_code, 302)  # check if the user is redirected after successful update

        # check if the receipt is updated
        self.receipt.refresh_from_db()
        self.assertEqual(self.receipt.desciption, 'test description')
        self.assertEqual(self.receipt.total_amount, 4)
