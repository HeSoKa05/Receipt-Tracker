from django.urls import path
from .views import (HomeView,
                    ReceiptListView,
                    ReceiptDetailView,
                    ReceiptCreateView,
                    ReceiptUpdateView,
                    ReceiptDeleteView,
                    NewUserView,
                    UserLoginView,
                    UserLogoutView,
                    UserProfileView)

app_name = 'recept_tracker_app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # CRUD operations: Create, Retrieve, Update, Delete
    # Create a new receipt
    path('receipt/create/', ReceiptCreateView.as_view(), name='receipt_create'),
    # receipts list -> Retrieve/Read
    path('receipts/', ReceiptListView.as_view(), name='receipt_list'),
    # Retrieve/Read receipt details
    path('receipt/<int:pk>/', ReceiptDetailView.as_view(), name='receipt_detail'),
    # Update a receipt
    path('receipt/<int:pk>/update/', ReceiptUpdateView.as_view(), name='receipt_update'),
    # Delete a specific receipt
    path('receipt/<int:pk>/delete/', ReceiptDeleteView.as_view(), name='receipt_delete'),

    # handling the Signup, Signin, Sign out, and profile urls:
    path('accounts/registration/', NewUserView.as_view(), name='register'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    path('accounts/profile/', UserProfileView.as_view(), name='profile')
]