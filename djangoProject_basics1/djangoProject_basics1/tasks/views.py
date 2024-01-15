from django.http import HttpResponse
from django.shortcuts import render

from djangoProject_basics1.tasks.models import Task


# def index(request):
#     name = request.GET.get("name", "noname")
#     content = f"<h1>{name}, welcome to my page!</h1>" + \
#               "<p>Let's start with the black magic!</p>"
#
#     return HttpResponse(content)


# def index(request):
#     all_tasks = Task.objects.all()
#
#     if not all_tasks:
#         return HttpResponse("<h2>No tasks!</h2>")
#
#     result = []
#
#     for task in all_tasks:
#         result.append(f"""
#     <li>
#         <h3>{task.title}</h3>
#         <p>{f"- {task.description}"}</p>
#     </li>
#             """)
#
#     ul = f"<ol>{''.join(result)}</ol>"
#
#     content = f"""
#     <h2>You have {len(all_tasks)} tasks:</h2>
#     {ul}
#     """
#     return HttpResponse(content)
#     # return render(request, "tasks/index.html")


# fetch data from database:
def index(request):
    title_filter = request.GET.get("title_filter", "")
    tasks = Task.objects.all()
    done_tasks = Task.objects.filter(is_done=True).count()

    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter.lower())

    context = {
        "title": "Welcome to the tasks app!",
        "task_list": tasks,
        "task_list_count": tasks.count(),
        "title_filter": title_filter,
        "done_tasks": done_tasks
    }

    return render(
        request,
        "tasks/index.html",
        context,
        )
