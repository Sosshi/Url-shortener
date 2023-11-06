import secrets, string

from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

from .models import ShortnerModel


class Home(CreateView):
    model = ShortnerModel
    template_name = "home.html"
    fields = [
        "original_url",
    ]


def redirect_url_to_original(request, shortened):
    original_url = ShortnerModel.objects.filter(slug=shortened).first()
    return redirect(original_url.original_url)


def shorten_url_view(request):
    url = request.POST.get("url", "")
    if url:
        try:
            random_slug = "".join(
                secrets.choice(string.ascii_letters + string.digits)
                for _ in range(secrets.randbelow(7) + 4)
            )
            shortened_url = ShortnerModel.objects.create(
                original_url=url, slug=random_slug
            )
            return HttpResponse(
                f"""
                <div id="message" class="mt-3">
                <p id="message_text">http://127.0.0.1:8000/{shortened_url.slug}/</p>
                <button id="copyButton" onclick="triggerCopy()" class="btn btn-light" >
                    Copy to Clipboard
                </button>
            </div>

"""
            )
        except Exception as e:
            return HttpResponse(f"{e}")
    return HttpResponse("Please provide a url")


def redirect_to_login(request):
    return redirect(reverse("account_signup"))
