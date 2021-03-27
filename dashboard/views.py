from django.shortcuts import render
from django.http import HttpResponse
from .models import ScenarioChange
from calculations.views import calculations

from .forms import ScenarioForm
# Create your views here.


def dashboard_view(request, *args, **kwargs):

    # obj =  ScenarioChanges.objects.get(id=1)
    # context = {
    #     "object" : obj,
    #     "form" : scenario_create_view(request)["form"]
    # }
    context = {"hey": calculations(request)}
    return render(request, "dashboard.html", context)


def ajaxHandling(request):
    """AJAX handler.

    Checks if the request is a post. Uses from the request the task/job id to fetch the Celery unique identifier.
    In turn it retrieves by using the Celery unique identifier the actual results

    Args:
        object: request
    Returns:
        JSON response of result calculation

    """
    if request.method == 'POST':
        try:

            # start retrieving taskID/JobID
            jobId = request.POST.get('TaskID')

            # The model Job has a primary key that is exactly the matching jobID from the front-end
            celery_id = Job.objects.values_list(
                'celery_id', flat=True).get(pk=jobId)
            if not (celery_id is None):
                # the model Task Results contains the results, so search via celery_id to get the results
                result = models.TaskResult.objects.values_list(
                    'result', flat=True).get(task_id=celery_id)
                cleaned_result = json.loads(result)

                data = {
                    'rawResultData': cleaned_result,
                }
                return JsonResponse(data)
            else:
                data = {
                    'status': "job failed (celery_id not found)",
                }
                return JsonResponse(data)
        except Exception as e:
            data = {
                'status': "job failed (Cannot fetch database jobID:" + str(jobId) + ")******" + str(
                    e) + "*********" + "celeryID:" + str(celery_id),
            }
            return JsonResponse(data)
    else:
        return render(request, 'error.html')
