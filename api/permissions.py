from rest_framework.permissions import BasePermission



class IsVisitorUser(BasePermission):
    """
    Allows access only to Visitor users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.isVisitor)

class IsExhibitorUser(BasePermission):
    """
    Allows access only to Exhibitor users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.isExhibitor)
