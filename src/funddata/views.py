
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import ShowDataForm
from .models import ShowData

# Create your views here.

def showdata(request):
	form = ShowDataForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		#messages.success(request, 'Account Added')
		#return HttpResponseRedirect('/thank-you/')
	query_results = ShowData.objects.all()
	#for query_result in query_results:
	#	print query_result.fund_id 
	return render_to_response("showdata.html", locals(), context_instance=RequestContext(request))