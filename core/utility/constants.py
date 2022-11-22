
from utility.models import *


def department():
    try:
        DEPARTMENT = tuple([(str(d.pk), d.name)
                            for d in Department.objects.all()])
    except:
        DEPARTMENT = None

    return DEPARTMENT
       


def designation():
    try:
        DEPARTMENT = tuple([(str(d.pk), d.name)
                            for d in Department.objects.all()])
    except:
        DEPARTMENT = None

    return DEPARTMENT


try:
    DEPARTMENT = department()
    DESIGNATION = designation()
except:
    DEPARTMENT = (("1","dskj"))
    DESIGNATION = (("1", "dskj"))
