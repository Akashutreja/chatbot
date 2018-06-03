from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def webhook(request):
    if request.method == 'POST':
        req = request.data
        result=process_request(req)

    return Response(result)

def process_request(req):
    action=req.get("queryResult").get("action")
    if action=="input.welcome":
        return Response({"fulfillmentText": 'Hi, what is your name?'})
    elif action=="user.name":
        name=req.get("queryResult").get("parameteres").get("name")
        res="Hey"+name+" I am Nikki… Your HR Assistant! I will be in touch with you frequently to know how it is going with you & help you out wherever you need support.How was your day today?"
        return Response({"fulfillmentText":res})


