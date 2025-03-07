# contact/views.py
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Contact

class ContactFormView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    #success_url = reverse_lazy('contact:contact_success')
    success_url = reverse_lazy('contact:contact_form')
    
    def form_valid(self, form):
        # Save the contact message
        contact = form.save()
        
        # Send email notification
        subject = f"New Contact Form Submission: {contact.subject}"
        message = f"""
        Name: {contact.name}
        Email: {contact.email}
        Subject: {contact.subject}
        
        Message:
        {contact.message}
        """
        # from_email = settings.DEFAULT_FROM_EMAIL
        # recipient_list = [settings.DEFAULT_FROM_EMAIL]
        from_email = contact.email
        recipient_list = [settings.EMAIL_HOST_USER]
        
        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            messages.warning(self.request, "Your message was saved but email notification failed. We'll still get back to you soon.")
        
        messages.success(self.request, "Your message has been sent successfully. We'll get back to you soon!")
        return super().form_valid(form)

def contact_success(request):
    return render(request, 'contact/contact_success.html')