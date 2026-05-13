from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from machines.models import Machine


def chatbot_page(request):

    response = ""

    if request.method == "POST":

        user_message = request.POST.get('message').lower()

        # MACHINE AVAILABILITY
        if "available" in user_message:

            machines = Machine.objects.filter(is_available=True)

            if machines.exists():
                response = "Available Machines:<br>"

                for machine in machines:
                    response += f"- {machine.name}<br>"

            else:
                response = "No machines available currently."

        # PRICE CHECK
        elif "price" in user_message or "rent" in user_message:

            machines = Machine.objects.all()

            found = False

            for machine in machines:

                if machine.name.lower() in user_message:
                    response = f"{machine.name} costs ₹{machine.daily_rate}/day"
                    found = True
                    break

            if not found:
                response = "Please specify machine name."

        # GREETING
        elif "hello" in user_message or "hi" in user_message:
            response = "Hello! Welcome to RoadAxis AI."

        else:
            response = "Sorry, I didn't understand. Try asking about machine availability or pricing."

    return render(request, 'chatbot/chatbot.html', {
        'response': response
    })