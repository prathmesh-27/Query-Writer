from django.shortcuts import render
from api.gemini import explain_to_sql
from .models import QueryHistory

def home(request):
    sql_output = ""
    sql_explanation = ""
    recent_queries = QueryHistory.objects.order_by('-timestamp')[:3]

    if request.method == 'POST':
        explanation = request.POST.get("explanation")
        db_type = request.POST.get("db_type")
        model = request.POST.get("model")

        sql_output = explain_to_sql(explanation, db_type, model)

        # Only save if there was no error returned
        if not sql_output.startswith("❌") and not sql_output.lower().startswith("error"):
            QueryHistory.objects.create(
            explanation=explanation,
            sql_output=sql_output,
            db_type=db_type,
            model_used=model
        )

    return render(request, "index.html", {
        "sql_output": sql_output,
        "recent_queries": recent_queries
    })

def history(request):
    all_queries = QueryHistory.objects.order_by('-timestamp')
    return render(request, "history.html", {"all_queries": all_queries})
