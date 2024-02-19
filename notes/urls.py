from django.urls import path
from .views import NoteCreateView, NoteRetrieveUpdateView, NoteShareView, NoteVersionHistoryView

urlpatterns = [
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('<int:pk>/', NoteRetrieveUpdateView.as_view(), name='note-detail'),
    path('share/<int:pk>/', NoteShareView.as_view(), name='note-share'),
    path('version-history/<int:pk>/', NoteVersionHistoryView.as_view(), name='note-version-history'),
]
