# Create your views here.
from django.shortcuts import render
from .models import NewsUpdate,NewsletterSubscription,ContactUs, Store
from .forms import ContactUsForm,NewsletterSubscriptionForm
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

def home_view(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
            form = NewsletterSubscriptionForm()  # reset form
        else:
            messages.error(request, "Please enter a valid email.")
    else:
        form = NewsletterSubscriptionForm()
    
    return render(request, 'FutureApp/home.html', {'form': form})

def about_us_view(request):
    return render(request, 'FutureApp/about_us.html')

def our_service_view(request):
    return render(request, 'FutureApp/our_service.html')

def programs_view(request):
    return render(request, 'FutureApp/programs.html')

def study_abroad_view(request):
    return render(request, 'FutureApp/study_abroad.html')

def energy_solution_view(request):
    return render(request, 'FutureApp/energy_solution.html')

def store_view(request):
    return render(request, 'FutureApp/store.html')


def news_update_view(request):
    posts = NewsUpdate.objects.order_by('-date_published')
    return render(request, 'FutureApp/news_update.html', {'posts': posts})




class contact_view(FormView):
    template_name = 'FutureApp/ContactUs.html'    
    form_class = ContactUsForm
    success_url = reverse_lazy('contact')  # Redirect after successful form submission

    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent successfully!") 
        return super().form_valid(form)

def newsletter_subscribe_view(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
            form = NewsletterSubscriptionForm()  # reset form
        else:
            messages.error(request, "Please enter a valid email.")
    else:
        form = NewsletterSubscriptionForm()

    return render(request, 'FutureApp/home.html', {'form': form})


def store_view(request):
    items = Store.objects.all()
    return render(request, 'FutureApp/store.html', {'items': items})

def store_detail_view(request, pk):
    item = get_object_or_404(Store, pk=pk)
    return render(request, 'FutureApp/store_detail.html', {'item': item})


def add_to_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Store, id=item_id)
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        item_key = str(item_id)

        if item_key in cart:
            cart[item_key]['quantity'] += quantity
        else:
            cart[item_key] = {
                'name': item.name,
                'price': float(item.price),
                'quantity': quantity,
            }

        request.session['cart'] = cart

        return JsonResponse({
            'name': item.name,
            'price': float(item.price),
            'quantity': cart[item_key]['quantity'],
        })