from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
        path('', TemplateView.as_view(template_name='homepage.html'), name='index'),
        path('about/', TemplateView.as_view(template_name='about_us.html'), name='AboutUs'),
        path('mission/', TemplateView.as_view(template_name='our_mission.html'), name='OurMission'),
        path('sales/', TemplateView.as_view(template_name='sales.html'), name='Sales'),
        path('AL/' , TemplateView.as_view(template_name='Automatic_Transmission_Fluid.html'), name='AT'),
        path('AU/', TemplateView.as_view(template_name='AUTOMOTIVE_LUBRICANTS.html'), name='AL'),
        path('HO/', TemplateView.as_view(template_name='AW Hydraulic Oil.html'), name='HO'),
        path('CO/', TemplateView.as_view(template_name='Compressor_Oil.html'), name='CO'),
        path('coolant/', TemplateView.as_view(template_name='Coolant.html'), name='COOLANT'),
        path('CU/', TemplateView.as_view(template_name='cutting_oil.html'), name='CU'),
        path('GE/', TemplateView.as_view(template_name='Gear_Oil.html'), name='GE'),
        path('HDB/', TemplateView.as_view(template_name='HEAVY DUTY BRAKE FLUID DOT 3.html'), name='HDB'),
        path('MSO/', TemplateView.as_view(template_name='MARINE_SYSTEM_OIL.html'), name='MSO'),


        

    

   
    
]