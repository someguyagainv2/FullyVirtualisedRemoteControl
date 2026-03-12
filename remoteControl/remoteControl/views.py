from django.http import HttpResponse
registeredServers = {}

def createServer(JobID):
    registeredServers[JobID] = {}
