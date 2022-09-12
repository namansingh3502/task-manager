from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list(request):
    """
    :return: list of task
    """

    tasks = Task.objects.filter(user=request.user).order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_detail(request, task_id):
    """
    :param request:
    :param task_id:
    :return: details of the task_id if that task is created by the loggedin user else error 401
    """
    try:
        tasks = Task.objects.get(id=task_id, user=request.user)
    except Task.DoesNotExist:
        return Response({"msg": "Not authorized"}, status=HTTP_401_UNAUTHORIZED)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    """

    :param request:
    :return: Create new task and return Success and error msgs
    """

    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
    else:
        print(serializer.errors)
        return Response({"msg": "Invalid Data."}, status=HTTP_400_BAD_REQUEST)

    return Response({"msg": "Task created successfully."}, status=HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_update(request, task_id):
    """

    :param request:
    :param task_id:
    :return: update task details if task is created by the user loggedin else error 401
    """
    try:
        task = Task.objects.get(id=task_id, user=request.user)
    except Task.DoesNotExist:
        return Response({"msg": "Not authorized"}, status=HTTP_401_UNAUTHORIZED)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def task_delete(request, task_id):
    """

    :param request:
    :param task_id:
    :return: delete task details if task is created by the user loggedin else error 401
    """
    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
    except Task.DoesNotExist:
        return Response({"msg": "Task Does not exist."}, status=HTTP_401_UNAUTHORIZED)

    return Response('Item successfully delete!')
