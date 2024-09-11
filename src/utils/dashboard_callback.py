def dashboard_callback(_, context):

    context.update(
        {"random": "THIS IS RANDOM TEXT FROM DASHBOARD CALLBACK"}
    )

    return context
