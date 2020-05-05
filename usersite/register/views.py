from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.conf import settings
import boto3

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            ## Save to Dynamodb
            save_to_db(form)
            messages.success(response, f'Account created!')
            return redirect("/register_success")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})

def login_success(response):
    return render(response, "register/login_success.html")

def register_success(response):
    return render(response, "register/register_success.html")

def save_to_db(form):
    # DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
    # dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url=DYNAMO_ENDPOINT)
    # Locally debug mode
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    table = dynamodb.Table('userRegister')
    table.put_item(
        Item={
            'username': form.cleaned_data.get('username'),
            'email': form.cleaned_data.get('email'),
            'password': form.cleaned_data.get('password1')
        }
    )
    print('Saved !')