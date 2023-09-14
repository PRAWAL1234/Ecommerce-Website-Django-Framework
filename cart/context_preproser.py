from .models import CartItem
# from django.contrib.auth.models import User
def cart_item_count(request):
    user=request.user
    if user.is_authenticated :
        total_item=CartItem.objects.filter(user=user).count()
    else:
        total_item=0
    return {'cart_total_item':total_item}
    