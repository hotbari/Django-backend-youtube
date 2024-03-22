from django.db import models
from common.models import CommonModel
from users.models import User



# User:Subscriber = 1:N 내가 구독한 사람
# User:Subscribed_to = 1:N 나를 구독한 사람
class Subscription(CommonModel):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions') # subscriber_set 대신 related_name으로 불러올 수 있음
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
    