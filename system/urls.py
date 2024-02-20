from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "system"


urlpatterns = [
    path('', views.LoginView, name = "login"),
    path('dashboard', views.Dashboard, name = "dashboard"),
    path('add-medicine', views.AddMedicine, name = "add-medicine"),
    path('generate-qr-code-online', views.qrView, name = "qrView"),
    path('generate-qr-code-online-generater', views.generateQR, name = "generateQR"),
    path('logout', views.logoutView, name = "logout"),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
