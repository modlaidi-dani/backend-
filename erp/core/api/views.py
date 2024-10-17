from rest_framework.response import Response


def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(routes)
