from django.views import View
from django.shortcuts import render, redirect
import django.contrib.auth.hashers as hashers

from ..models.customer import Customer


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        login_data = request.POST
        email = login_data.get("email")
        password = login_data.get("password")
        customer = Customer.get_customer_by_email(email)
        error_msg = ""
        if customer:
            flag = hashers.check_password(password, customer.password)
            if flag:
                request.session['customerid'] = customer.id
                return redirect("/")
            else:
                error_msg = "Invalid Password"
                return render(request, "login.html", {"error": error_msg})
        else:
            error_msg = "Invalid User"
            return render(request, "login.html", {"error": error_msg})


def logout(request):
    request.session.clear()
    return redirect("/")
