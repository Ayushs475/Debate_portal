from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser,debate,vote
from .serializers import CustomUserSerializer,DebateSerializer,VoteSerializer
from django.shortcuts import get_object_or_404

class UserRegistrationView(APIView):
    def get(self, request, username):
        # Retrieve user by username or return 404 if not found
        user = get_object_or_404(CustomUser, username=username)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Implement user registration logic
        # ...
        # Example response
        response_data = {'message': 'User registered successfully'}
        return Response(response_data, status=status.HTTP_201_CREATED)

    def put(self, request, username):
        # Retrieve user by username or return 404 if not found
        user = get_object_or_404(CustomUser, username=username)
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        # Retrieve user by username or return 404 if not found
        user = get_object_or_404(CustomUser, username=username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DebateManagementView(APIView):
    def get(self, request):
        debates = Debate.objects.all()
        serializer = DebateSerializer(debates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DebateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DebateDetailView(APIView):
    def get(self, request, debate_id):
        debate = Debate.objects.get(pk=debate_id)
        serializer = DebateSerializer(debate)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VoteView(APIView):
    def post(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BanUserView(APIView):
    def post(self, request, username):
        user = CustomUser.objects.get(username=username)
        # Implement logic to ban the user (e.g., set a 'banned' flag)
        user.banned = True
        user.save()
        return Response({'message': f'{username} has been banned'}, status=status.HTTP_200_OK)

class AssignModeratorRoleView(APIView):
    def post(self, request, username):
        user = CustomUser.objects.get(username=username)
        # Implement logic to assign the moderator role
        user.role = 'Moderator'
        user.save()
        return Response({'message': f'{username} has been assigned the moderator role'}, status=status.HTTP_200_OK)

class ReportUserInfractionView(APIView):
    def post(self, request, username):
        # Implement logic to report user infractions
        # This could involve recording and tracking reports
        return Response({'message': f'User {username} has been reported for an infraction'}, status=status.HTTP_200_OK)

