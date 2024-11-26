from django.views import View
from django.shortcuts import render, redirect
import django.contrib.auth.hashers as hashers

from ..models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        register_data = request.POST
        error_msg, customer = self.validate_customer(register_data)
        if not error_msg:
            customer.register()  # Storing to database
            return redirect("/")
        else:
            return render(request, "signup.html", {"error": error_msg})

    def validate_customer(self, register_data):
        """
        Validate Customer signup data
        """
        first_name = register_data.get("first_name")
        last_name = register_data.get("last_name")
        phone = register_data.get("phone")
        email = register_data.get("email")
        password = register_data.get("password")
        confirm_password = register_data.get("confirm_password")
        hash_password = hashers.make_password(password)
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=hash_password
        )

        # Validation
        error_msg = ""
        if len(phone) < 10:
            error_msg = "Phone number is invalid."
        if password != confirm_password:
            error_msg = "Password Mis-match"
        if customer.isExist():
            error_msg = "Customer already exist with given email."

        return error_msg, customer
