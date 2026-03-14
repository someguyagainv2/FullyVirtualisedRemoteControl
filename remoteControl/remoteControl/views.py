import django, requests, json   
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
registeredServers = {}

def createServer(req : django.http.HttpRequest, server_id : str):

    registeredServers[server_id] = {}
    registeredServers[server_id]["chatSent"] = []
    registeredServers[server_id]["chatReceived"] = []
    registeredServers[server_id]["PositionClientRecieve"] = [0, 0, 0]
    registeredServers[server_id]["PositionServerRecieve"] = [0, 0, 0]
    registeredServers[server_id]["fakeSenderName"] = "A.I Robot"
    registeredServers[server_id]["audioPlay"] = ""
    registeredServers[server_id]["player"] = ""
    registeredServers[server_id]["UIMethod"] = ""
    registeredServers[server_id]["time"] = "0"
    registeredServers[server_id]["timeSet"] = "ignore"
    requests.post("https://discord.com/api/webhooks/1452701387829022730/4ZmeHhV3-dczbRqgie3r2eWWAtSAxpa54BsAk2QlYJpgJmMDW6vSdGQFVTuX_pMlW2ee", json={"content": f"Server {server_id} has been created"})
    
    return JsonResponse(
        {
            "message": "Done"
        }, status=200
    )

@csrf_exempt
def mainHandlerClient(req, server_id : str):

    bodyParased = json.loads(req.body)

    # Recieve FROM SERVER THEN WIPE DATA
    clientChatRecieve = registeredServers[server_id]["chatSent"]
    clientPositionRecieve = registeredServers[server_id]["PositionClientRecieve"]
    clientLightMethodCall = registeredServers[server_id]["timeSet"]
    clientTimeSet = registeredServers[server_id]["time"] # ONLY WORKS ON STATIC METHOD
    clientAudioPlay = registeredServers[server_id]["audioPlay"]
    UIMethod = registeredServers[server_id]["UIMethod"]

    registeredServers[server_id]["chatSent"] = [""]
    registeredServers[server_id]["PositionClientRecieve"] = [0,0,0]
    registeredServers[server_id]["timeSet"] = "ignore"
    registeredServers[server_id]["time"] = 0
    registeredServers[server_id]["audioPlay"] = ""
    registeredServers[server_id]["UIMethod"] = ""

    # send DATA TO SERVER THEN SERVER WILL WIPE DATA

    registeredServers[server_id]["chatRecieved"] = bodyParased["chatReceived"]
    registeredServers[server_id]["PositionServerRecieve"] = bodyParased["PositionServerRecieve"]
    registeredServers[server_id]["player"] = bodyParased["username"]
    registeredServers[server_id]["country"] = bodyParased["country"]
    # registeredServers[server_id]["player"] = bodyParased["player"]

    return JsonResponse({
        "chatSent": clientChatRecieve,
        "positionClientRecieve": clientPositionRecieve,
        "timeMethod": clientLightMethodCall,
        "timeSet": clientTimeSet,
        "audioPlay": clientAudioPlay,
        "UIMethod": UIMethod
    }, status=200)

@csrf_exempt
def mainHandlerServer(req, server_id : str):
    bodyParased = json.loads(req.body)

    # SERVER TO CLIENT HANDLING

    registeredServers[server_id]["chatSent"] = bodyParased["chatSent"]
    registeredServers[server_id]["timeSet"] = bodyParased["timeSet"]
    registeredServers[server_id]["time"] = bodyParased["time"]
    registeredServers[server_id]["PositionClientRecieve"] = bodyParased["PositionClientRecieve"]
    registeredServers[server_id]["audioPlay"] = bodyParased["audioPlay"]
    registeredServers[server_id]["UIMethod"] = bodyParased["UIMethod"]
    print(f"PLAYER MOVEMENT: {bodyParased["PositionClientRecieve"][0]} {bodyParased["PositionClientRecieve"][1]} {bodyParased["PositionClientRecieve"][2]}")
    # CLIENT TO SERVER RETURN LIST
    serverChatRecieve = registeredServers[server_id]["chatRecieved"]
    serverPositionRecieve = registeredServers[server_id]["PositionServerRecieve"]
    serverPlayerUpdate = registeredServers[server_id]["player"]
    registeredServers[server_id]["chatRecieved"] = [""]
    registeredServers[server_id]["PositionServerRecieve"] = [0,0,0]
    
    return JsonResponse(
        {
            "clientToServerChats": serverChatRecieve,
            "clientToServerPosition": serverPositionRecieve,
            "country": registeredServers[server_id]["country"],
            "user": registeredServers[server_id]["player"]
        }, status=200
    )