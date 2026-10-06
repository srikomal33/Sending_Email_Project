from django.shortcuts import render
from django.http import HttpResponse
from Send_Email import info
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


# Create your views here.

def home(request):
    return render(request, "sendEmails/index.html")


def staticText(request):
    subject = "staticText Email"

    toEmail1 = "srikomal33@gmail.com"
    toEmail2 = "komalsri0303@gmail.com"

    message = (
        "Hello Komal Srivastava!!\n"
        "Welcome to SRM!!\n"
        "Thank you for visiting our website.\n\n"
        "Thank you\n"
    )

    from_email = info.EMAIL_HOST_USER
    to_list = [toEmail1, toEmail2]

    send_mail(
        subject,
        message,
        from_email,
        to_list,
        fail_silently=True
    )

    return render(request, "sendEmails/emailSent.html")


def dynamicText(request):
    first_name = "Alex"
    marks = 396
    college_name = "Oxford University"

    toEmail1 = "srikomal33@gmail.com"
    toEmail2 = "komalsri0303@gmail.com"

    email_subject = "dynamicTextHTML Email"

    # Fetched from Front End
    # first_name = request.POST['first_name']

    # Fetched from Database
    # first_name = models.Student.name

    message = render_to_string(
        'sendEmails/dynamicText.html',
        {
            'name': first_name,
            'marks': marks,
            'university': college_name
        }
    )

    email = EmailMessage(
        email_subject,
        message,
        info.EMAIL_HOST_USER,
        [toEmail1, toEmail2]
    )

    email.fail_silently = True
    email.send()

    return render(request, "sendEmails/emailSent.html")


def beautifulHTML(request):
    first_name = "Andrew"
    marks = 396
    college_name = "Harvard University"
     
    toEmail1 = "srikomal33@gmail.com"
    toEmail2 = "komalsri0303@gmail.com"
     
    email_subject = "beautifulHTML Email"
     
         # Fetched from Front End
         # first_name = request.POST['first_name']
     
         # Fetched from Database
         # first_name = models.Student.name
     
    message = render_to_string(
             'sendEmails/beautifulHTML.html',
             {
                 'name': first_name,
                 'marks': marks,
                 'university': college_name
             }
         )
     
    email = EmailMessage(
             email_subject,
             message,
             info.EMAIL_HOST_USER,
             [toEmail1, toEmail2]
         )
     
    email.fail_silently = True
    email.content_subtype="html"
    email.send()
     
    return render(request, "sendEmails/emailSent.html")
    


def attachmentEmail(request):
    name = "Stephen"
    role="Full Stack Developer"
    company_name="Nexora Technologies PVT. Limited"
     
    toEmail1 = "srikomal33@gmail.com"
    toEmail2 = "komalsri0303@gmail.com"
     
    email_subject = "You are Placed!!"
     
    message = render_to_string(
             'sendEmails/attachmentEmail.html',
             {
                 'name': name,
                 'role': role,
                 'organization_name': company_name
             }
         )
     
    email = EmailMessage(
             email_subject,
             message,
             info.EMAIL_HOST_USER,
             [toEmail1, toEmail2]
         )
    email.attach_file(str(settings.BASE_DIR)+"\\Offer_Letter_Stephen_Full_Stack_Developer.pdf")
     
    email.fail_silently = True
    email.content_subtype="html"
    email.send()
     
    return render(request, "sendEmails/emailSent.html")
        
    