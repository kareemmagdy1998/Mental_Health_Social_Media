from rest_framework.permissions import BasePermission



class IsDoctorUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return (
            request.user.is_authenticated
            and hasattr(request.user, "doctor")
        )
    
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Only the owner of the post can edit or delete it
        print (request.user)
        return obj.creator == request.user


class IsCommentOwnerOrReadOnly(BasePermission): 
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return obj.author == request.user
