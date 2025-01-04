from rest_framework.generics import RetrieveUpdateAPIView
from SellerApp.models import ModelSeller
from UserApp.models import ModelUser
from .serializers import UpdateSellerSerializer
from .permissions import IsSeller
from .throttles import SellerThrottle


class UpdateSellerProfileAPIView(RetrieveUpdateAPIView):
    queryset           = ModelSeller.objects.all()
    serializer_class   = UpdateSellerSerializer
    permission_classes = [IsSeller]
    throttle_classes   = [SellerThrottle]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        seller = ModelSeller(user=self.request.user)
        seller.save()
        return seller
