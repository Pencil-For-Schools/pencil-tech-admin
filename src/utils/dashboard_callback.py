def dashboard_callback(request, context):

    context.update(
        {"random": "THIS IS RANDOM TEXT FROM DASHBOARD CALLBACK"}
    )

    return context
