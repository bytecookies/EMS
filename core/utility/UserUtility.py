from django.contrib.auth import get_user_model
User = get_user_model()


def accept_tnd(id):
    print("lksdjf")
    user = User.objects.get(pk=id)
    user.t_n_d = True
    user.save()
    print("acceting t&d")
