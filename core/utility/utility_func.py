from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMultiAlternatives
import random
User = get_user_model()



def accept_tnd(id):
    print("lksdjf")
    user = User.objects.get(pk=id)
    user.t_n_d = True
    user.save()
    print("acceting t&d")


def unique_id():
    prifix="IM"
    num=random.randrange(1,10**10)
    code = prifix+str(num)
    check=User.objects.filter(registration_id=code)
    if not check:
        return code
    else:
        get_code=unique_id()
        return get_code


def populate_id():
    k=User.objects.all()
    for i in k:
        User.objects.filter(pk=i.pk).update(registration_id=unique_id())