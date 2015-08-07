
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
# Create your views here.

def showdata(request):
	return render_to_response("showdata.html", locals(), context_instance=RequestContext(request))