# notes/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Note, NoteChange
from .serializers import NoteSerializer, NoteChangeSerializer


class NoteCreateView(generics.CreateAPIView):
    """
        To Create a new note
    """
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
        To Retrieve and update a note by its id
    """
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the user has access to the note
        if request.user == instance.owner or request.user in instance.shared_users.all():
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({'detail': 'Access forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the user has access to the note
        if request.user != instance.owner and request.user not in instance.shared_users.all():
            return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        # Parse the new content from request data and create a NoteChange entry
       
        serializer = self.get_serializer(instance, data = request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        new_content = request.data.get('content', '')
        NoteChange.objects.create(note=instance, user=request.user, content=new_content)

        return Response({'detail': 'Note updated successfully'}, status=status.HTTP_200_OK)


class NoteShareView(generics.UpdateAPIView):
    """
        To Share a note among different users
    """
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the user is the owner of the note
        if request.user != instance.owner:
            return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        # Parse shared_users from request data and update the shared_users field
        shared_users = request.data.get('shared_users', [])
        if not shared_users:
            return Response({'detail': 'shared_users is a required property'}, status=status.HTTP_400_BAD_REQUEST)
        instance.shared_users.add(*shared_users)
        instance.save()

        return Response({'detail': 'Note shared successfully'}, status=status.HTTP_200_OK)

    
class NoteVersionHistoryView(generics.ListAPIView):
    """
        To View the edit history of note
    """
    permission_classes = [IsAuthenticated]
    queryset = NoteChange.objects.all()
    serializer_class = NoteChangeSerializer

    def get_queryset(self):
        note_id = self.kwargs.get('pk')
        return NoteChange.objects.filter(note_id=note_id)
