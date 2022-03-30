import json
from django.http import HttpRequest, JsonResponse


def api_home(req: HttpRequest, *args, **kwargs):
    try:
        data = json.loads(req.body)
    except:
        print("Unable to load body")

    data["headers"] = dict(req.headers)
    data["params"] = dict(req.GET)

    return JsonResponse(data if data else {"msg": "done"})
