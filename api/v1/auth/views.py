from rest_framework_simplejwt.views import TokenObtainPairView
from api.v1.auth.serializers import UserTokenObtainPairSerializer

class UserTokenObtainPairView(TokenObtainPairView):  #allows to extend or modify the behavior of token creation,like  might want to include addidtional fields.
    serializer_class = UserTokenObtainPairSerializer


