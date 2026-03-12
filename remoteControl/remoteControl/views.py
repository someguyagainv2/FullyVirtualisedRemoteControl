import django, requests, json   
from django.http import HttpResponse, JsonResponse
registeredServers = {}

def createServer(req : django.http.HttpRequest, server_id : int):

    registeredServers[server_id] = {}
    registeredServers[server_id]["chatSent"] = []
    registeredServers[server_id]["chatReceived"] = []
    requests.post("https://discord.com/api/webhooks/1452701387829022730/4ZmeHhV3-dczbRqgie3r2eWWAtSAxpa54BsAk2QlYJpgJmMDW6vSdGQFVTuX_pMlW2ee", json={"content": f"Server {server_id} has been created"})
    print(registeredServers)
    return JsonResponse(
        {
            "message": "Done"
        }, status=200
    )


def sendChatToClient(req, server_id):
    if server_id not in registeredServers:
        return JsonResponse(
            {
                "message": "Server not found"
            },
            status=404
        )
    chat = json.loads(req.body)["chat"]
    registeredServers[server_id]["chatSent"].append(chat)
    return JsonResponse(
        {
            "message": "Done"
        }, status=200
    )

def recieveChatClient(req, server_id):
    if server_id not in registeredServers:
        return JsonResponse(
            {
                "message": "Server not found"
            },
            status=404
        )
    chat = req.body
    registeredServers[server_id]["chatSent"] = []
    return JsonResponse(
        {
            "message": "Done"
        }, status=200
    )