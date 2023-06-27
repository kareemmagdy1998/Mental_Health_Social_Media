from rest_framework.permissions import BasePermission

class IsDoctorUser(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated as a doctor
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_authenticated and request.user.user_type == 'doctor'

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Only the owner of the post can edit or delete it
        return obj.creator == request.user
