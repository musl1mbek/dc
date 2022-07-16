from audioop import add
from cgitb import html, text
from codecs import namereplace_errors
from email.mime import image
from tracemalloc import start
from unicodedata import name

from django import shortcuts
from django.forms import DurationField
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serilizer import *
from .models import *

@api_view(['GET'])
def Getinfo(request):
    a = Info.objects.last()
    ser = InfoSerializer(a)
    return Response(ser.data)

@api_view(['GET'])
def Getslider(request):
    b = Slider.objects.all().order_by('-id')[0:5]
    ser = SliderSerializer(b, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getprojects(request):
    c = Projects.objects.all()
    ser = ProjectsSerializer(c, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Gettechnopark(request):
    a = Technopark.objects.all()
    ser = TechnoparkSerilaizer(a, many=True)
    return Response(ser.data)
@api_view(['GET'])
def Getsection(request, pk):
    b = Section.objects.get(id=pk)
    ser = SectionSerializer(b)
    return Response(ser.data)

@api_view(['GET'])
def Getpostal(request):
    c = Postalservices.objects.all()
    ser = PostalSerializer(c, many=True)
    return Response(ser.data)

@api_view(['POST'])
def Getboglanish(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    a = Boglanish.objects.create(fullname=fullname, phone=phone, text=text)
    ser = BoglanishSerializer(a)
    return Response(ser.data)
    
@api_view(['GET'])
def Getmobileoperators(request):
    e = Mobileoperators.objects.all()
    ser = MobileoperatorsSerializer(e, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getinternetproviders(request):
    f = Internetproviders.objects.all()
    ser = InternetprovidersSerializer(f, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getouraudience(request):
    g = OurAudience.objects.all()
    ser = OurAudienceSerializer(g, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getpercentage(request):
    h = Percentage.objects.all()
    ser = PercentageSerializer(h, many=True)
    return Response(ser.data)
@api_view(['GET'])
def Getresidents(request):
    i = Residents.objects.all()
    ser = ResidentsSerializer(i, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getteam(request):
    j = Team.objects.all()
    ser = TeamSerializer(j, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getcoimages(request):
    k = Coimages.objects.all()
    ser = CoimagesSerializer(k, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getcoworking(request):
    l = Coworking.objects.all()
    ser = CoworkingSerializer(l, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getinfrastructure(request):
    m = InfrastructureSlider.objects.all()
    ser = InfrastructureSliderSerializer(m, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getstudydirections(request):
    n = StudyDirections.objects.all()
    ser = StudydirectionsSerializer(n, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getitacademy(request):
    o = ItAcademy.objects.all()
    ser = ItAcademySerializer(o, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getstartupdirections(request):
    q = StartupDirections.objects.all()
    ser = StartupDirectionsSerializer(q, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getincubationcenters(request):
    r = IncubationCenters.objects.all()
    ser = IncubationCentersSerializer(r, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getraqamlashtirish(request):
    s = Raqamlashtirishxizmalari.objects.all()
    ser = RaqamlashtirishXizmatlariSerializer(s, many=True)
    return Response(ser.data)

@api_view(['POST'])
def Getcontact(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    email = request.POST.get('email')
    a = Contact.objects.create(fullname=fullname, phone=phone, text=text, email=email)
    ser = ContactSerializer(a)
    return Response(ser.data)

@api_view(['GET'])
def Getxizmatturi(request):
    u = XizmatTuri.objects.all()
    ser = XizmatTuriSerializer(u, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getxizmatlar(request):
    v = Xizmatlar.objects.all()
    ser = XizmatlarSerializer(v, many=True)
    return Response(ser.data)


@api_view(['POST'])
def Getapplication(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    email = request.POST.get('email')
    xizmat = request.POST.get('xizmat')
    xizmat = XizmatTuri.objects.get(id=xizmat)
    b = Application.objects.create(fullname=fullname, phone=phone, text=text, email=email, xizmat=xizmat)
    ser = ApplicationSerializer(b)
    return Response(ser.data)


def Index(request):
    return render(request,'dashboard-school.html')



def Section_funk(request):
    section = Section.objects.all()
    context = {
        'section': section
    }
    return render(request, 'section.html', context)


def Info_funk(request):
    section = Info.objects.all().order_by('-id')
    context = {
        'section': section
    }

    return render(request, 'info.html',context)


def Slider_funk(request):
    section = Slider.objects.all()
    context = {
        'section': section
    }

    return render(request, 'slider.html',context)



def Projects_funk(request):
    section = Projects.objects.all()
    context = {
        'section': section
    }

    return render(request, 'project.html', context)




def Technopark_funk(request):
    section = Technopark.objects.all()
    context = {
        'section': section
    }

    return render(request, 'technopark.html', context)



def Postal_Services(request):
    section = Postalservices.objects.all()
    context = {
        'section': section
    }

    return render(request, 'postalservices.html', context)


def Boglanish_Funk(request):
    section = Boglanish.objects.all()
    context = {
        'section': section
    }
    return render(request, 'boglanish.html', context)











def deletebooglanish(request, pk):
    todo = Boglanish.objects.get(id=pk)

    todo.delete()
    return redirect('Boglanish')


def DeleteInfo(request, pk):
    todo = Info.objects.get(id=pk)

    todo.delete()
    return redirect('info')

def DeleteSlider(request, pk):
    slider = Slider.objects.get(id=pk)

    slider.delete()
    return redirect('Slider')

def DeleteProject(request, pk):
    project = Projects.objects.get(id=pk)

    project.delete()
    return redirect('Project')

def DeleteTechnopark(request, pk):
    tech = Technopark.objects.get(id=pk)

    tech.delete()
    return redirect('Technopark')

def DeleteSection(request, pk):
    section = Section.objects.get(id=pk)

    section.delete()
    return redirect('Section')

def DeletePostalServices(request, pk):
    postalservice = Postalservices.objects.get(id=pk)

    postalservice.delete()
    return redirect('PostalServices')

def DeleteMobileOperators(request, pk):
    mobileoperators = Mobileoperators.objects.get(id=pk)

    mobileoperators.delete()
    return redirect('Mobileoperators')

def DeleteInternetproviders(request, pk):
    internetproviders = Internetproviders.objects.get(id=pk)

    internetproviders.delete()
    return redirect('Internetproviders')

def DeleteOurAudience(request, pk):
    ourAudience = OurAudience.objects.get(id=pk)

    ourAudience.delete()
    return redirect('OurAudience')

def DeletePercentage(request, pk):
    percentage = Percentage.objects.get(id=pk)

    percentage.delete()
    return redirect('Percentage')


def DeleteResidents(request, pk):
    residents = Residents.objects.get(id=pk)

    residents.delete()
    return redirect('Residents')

def DeleteTeam(request, pk):
    team = Team.objects.get(id=pk)

    team.delete()
    return redirect('Team')

def DeleteCoimages(request, pk):
    team = Coimages.objects.get(id=pk)

    team.delete()
    return redirect('Coimages')

def DeleteCoworking(request, pk):
    team = Coworking.objects.get(id=pk)

    team.delete()
    return redirect('Coworking')

def DeleteInfrastructureSlider(request, pk):
    team = InfrastructureSlider.objects.get(id=pk)

    team.delete()
    return redirect('InfrastructureSlider')

def DeleteStudyDirections(request, pk):
    team = StudyDirections.objects.get(id=pk)

    team.delete()
    return redirect('StudyDirections')

def DeleteItAcademy(request, pk):
    team = ItAcademy.objects.get(id=pk)

    team.delete()
    return redirect('ItAcademy')

def DeleteStartupDirections(request, pk):
    team = StartupDirections.objects.get(id=pk)

    team.delete()
    return redirect('StartupDirections')

def DeleteIncubationCenters(request, pk):
    team = IncubationCenters.objects.get(id=pk)

    team.delete()
    return redirect('IncubationCenters')


def DeleteRaqamlashtirishxizmatlari(request, pk):
    team = Raqamlashtirishxizmalari.objects.get(id=pk)

    team.delete()
    return redirect('Raqamlashtirishxizmatlari')


def DeleteContact(request, pk):
    team = Contact.objects.get(id=pk)

    team.delete()
    return redirect('Contact')

def DeleteXizmatTuri(request, pk):
    team = XizmatTuri.objects.get(id=pk)

    team.delete()
    return redirect('XizmatTuri')

def DeleteXizmatlar(request, pk):
    team = Xizmatlar.objects.get(id=pk)

    team.delete()
    return redirect('Xizmatlar')


def DeleteApplication(request, pk):
    team = Application.objects.get(id=pk)

    team.delete()
    return redirect('Application')









def Change_Info(request,pk):

    if request.method == "POST":
        info = Info.objects.get(id=pk)
        if 'logo' in request.FILES:
            info.logo = request.FILES['logo']

        phone = request.POST.get('phone')
        short_phone = request.POST['short_phone']
        print(short_phone)
        email = request.POST.get('email')
        address_uz = request.POST.get('address_uz')
        address_ru = request.POST.get('address_ru')
        address_en = request.POST.get('address_en')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        info.phone = phone
        info.email = email
        info.address_uz = address_uz
        info.address_ru = address_ru
        info.address_en = address_en
        info.lat = lat
        info.long = long
        info.short_phone = short_phone
        info.save()
        return redirect('info')
    return redirect('info')

def Change_Slider(request):
    if request.method == "POST":
        slider = Slider.objects.get(id=request.POST.get('id'))
        if 'video' in request.FILES:
            slider.video = request.FILES['video']
        slider.title_uz = request.POST.get('title_uz')
        slider.title_ru = request.POST.get('title_ru')
        slider.title_en = request.POST.get('title_en')

        slider.save()

    return redirect('Slider')

def Change_Project(request):
    if request.method == "POST":
        id = request.POST.get('id')
        project = Projects.objects.get(id=id)
        if 'logo' in request.FILES:
            project.image = request.FILES['logo']
        
        project.text_uz = request.POST.get('text_uz')
        project.text_ru = request.POST.get('text_ru')
        project.text_en = request.POST.get('text_en')

        project.save()

    return redirect('Project')

def Change_Technopark(request):
    if request.method == "POST":
        id = request.POST.get('id')
        technopark = Technopark.objects.get(id=id)
        if 'icon' in request.FILES:
            technopark.icon = request.FILES['icon']
        
        technopark.text_uz = request.POST.get('text_uz')
        technopark.text_ru = request.POST.get('text_ru')
        technopark.text_en = request.POST.get('text_en')
        technopark.number = request.POST.get('number')
        technopark.save()
    return redirect('Technopark')

def Change_Section(request):
    if request.method == "POST":
        id = request.POST.get('id')
        section = Section.objects.get(id=id)
        if 'image' in request.FILES:
            section.icon = request.FILES['image']
        section.name_uz = request.POST.get('name_uz')
        section.name_ru = request.POST.get('name_ru')
        section.name_en = request.POST.get('name_en')
        section.text_uz = request.POST.get('text_uz')
        section.text_ru = request.POST.get('text_ru')
        section.text_en = request.POST.get('text_en')

        section.save()
    return redirect('Section')


def Change_PostalServices(request):
    if request.method == "POST":
        id = request.POST.get('id')
        postalservice = Postalservices.objects.get(id=id)
        if 'logo' in request.FILES:
            postalservice.logo = request.FILES['logo']
        postalservice.save()
    
    return redirect('PostalServices')


def Change_MobileOperators(request):
    if request.method == "POST":
        id = request.POST.get('id')
        operator = Mobileoperators.objects.get(id=id)
        if 'logo' in request.FILES:
            operator.logo = request.FILES['logo']
        operator.save()
    return redirect('Mobileoperators')

def Change_InternetProviders(request):
    if request.method == "POST":
        id = request.POST.get('id')
        operator = Internetproviders.objects.get(id=id)
        if 'logo' in request.FILES:
            operator.logo = request.FILES['logo']
        operator.save()
    return redirect('Internetproviders')


def Mobileoperators_Funk(request):
    section = Mobileoperators.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Mobileoperators.html', context)


def Internetproviders_Funk(request):
    section = Internetproviders.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Internetproviders.html', context)


def OurAudience_Funk(request):
    section = OurAudience.objects.all()
    context = {
        'section': section
    }

    return render(request, 'OurAudience.html', context)


def Percentage_Funk(request):
    section = Percentage.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Percentage.html', context)


def Residents_Funk(request):
    section = Residents.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Residents.html', context)


def Team_Funk(request):
    section = Team.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Team.html', context)


def Coimages_Funk(request):
    section = Coimages.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Coimages.html', context)

def Coworking_Funk(request):
    section = Coworking.objects.all()
    coimages = Coimages.objects.all()
    context = {
        'section': section,
        'coimages': coimages
    }

    return render(request, 'Coworking.html', context)


def InfrastructureSlider_Funk(request):
    section = InfrastructureSlider.objects.all()
    context = {
        'section': section
    }

    return render(request, 'InfrastructureSlider.html', context)


def StudyDirections_Funk(request):
    section = StudyDirections.objects.all()
    context = {
        'section': section
    }

    return render(request, 'StudyDirections.html', context)


def ItAcademy_Funk(request):
    section = ItAcademy.objects.all()
    context = {
        'section': section
    }

    return render(request, 'ItAcademy.html', context)


def StartupDirections_Funk(request):
    section = StartupDirections.objects.all()
    context = {
        'section': section
    }

    return render(request, 'StartupDirections.html', context)


def IncubationCenters_Funk(request):
    section = IncubationCenters.objects.all()
    context = {
        'section': section
    }

    return render(request, 'IncubationCenters.html', context)


def Raqamlashtirishxizmatlari_Funk(request):
    section = Raqamlashtirishxizmalari.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Raqamlashtirishxizmalari.html', context)


def Contact_Funk(request):
    section = Contact.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Contact.html', context)
    

def XizmatTuri_Funk(request):
    section = XizmatTuri.objects.all()
    context = {
        'section': section
    }

    return render(request, 'XizmatTuri.html', context)
    

def Xizmatlar_Funk(request):
    section = Xizmatlar.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Xizmatlar.html', context)



def Application_Funk(request):
    section = Application.objects.all()
    context = {
        'section': section
    }

    return render(request, 'Application.html', context)


def InfoCreate_Funk(request):
    if request.method == "POST":
        logo = request.FILES['logo']
        if logo in request.FILES:
            Info.logo = request.FILES['logo'] 
        short_phone = request.POST.get('short_phone')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address_uz = request.POST.get('address_uz')
        address_ru = request.POST.get('address_ru')
        address_en = request.POST.get('address_en')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        Info.objects.create(logo=logo, short_phone=short_phone,phone=phone,email=email,address_uz=address_uz, address_ru=address_ru, address_en=address_en,lat=lat,lng=lng)
        return redirect('info')

    return render(request, 'create-info.html',)



def SliderCreate_Funk(request):
    if request.method == "POST":
        video = request.FILES['video']
        if video in request.FILES:
            Slider.video = request.FILES['video'] 
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        title_en = request.POST.get('title_en')
        # address_uz = request.POST.get('address_uz')
        # address_ru = request.POST.get('address_ru')
        # address_en = request.POST.get('address_en')
        # lat = request.POST.get('lat')
        # lng = request.POST.get('lng')
        Slider.objects.create(video=video,title_uz=title_uz,title_ru=title_ru,title_en=title_en)
        return redirect('Slider')

    return render(request, 'create-slider.html',)



def ProjectsCreate_Funk(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
            Projects.image = request.FILES['image'] 
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        # address_uz = request.POST.get('address_uz')
        # address_ru = request.POST.get('address_ru')
        # address_en = request.POST.get('address_en')
        # lat = request.POST.get('lat')
        # lng = request.POST.get('lng')
        Projects.objects.create(image=image,text_uz=text_uz,text_ru=text_ru,text_en=text_en)

        return redirect('Project')

    return render(request, 'create-project.html',)

    
def TechnoparkCreate_Funk(request):
    if request.method == "POST":
        logo = request.FILES['logo']
        if logo in request.FILES:
            Technopark.logo = request.FILES['logo'] 
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        number = request.POST.get('number')
        # address_uz = request.POST.get('address_uz')
        # address_ru = request.POST.get('address_ru')
        # address_en = request.POST.get('address_en')
        # lat = request.POST.get('lat')
        # lng = request.POST.get('lng')
        Technopark.objects.create(icon=logo,text_uz=text_uz,text_ru=text_ru,text_en=text_en,number=number)

        return redirect('Technopark')

    return render(request, 'create-technopark.html',)

def SectionCreate_Funk(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
            Section.image = request.FILES['image'] 
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        Section.objects.create(image=image, text_uz=text_uz, text_ru=text_ru,text_en=text_en, name_uz=name_uz, name_ru=name_ru,name_en=name_en)
        return redirect('Section')
    return render(request, 'create-section.html',)

def PostalserviceCreate_Funk(request):
    if request.method == "POST":
        logo = request.FILES['logo']
        if logo in request.FILES:
            Postalservices.image = request.FILES['logo'] 
        Postalservices.objects.create(logo=logo)
        return redirect('PostalServices')
        
    return render(request, 'create-postalservices.html')

def MobilCreate_Funk(request):
    if request.method == "POST":
        logo = request.FILES['logo']
        if logo in request.FILES:
            Mobileoperators.image = request.FILES['logo'] 
        Mobileoperators.objects.create(logo=logo)
        return redirect('Mobileoperators')
    return render(request, 'create-mobil.html')

def InternetprovidersCreate_Funk(request):
    if request.method == "POST":
        logo = request.FILES['logo']
        if logo in request.FILES:
            Internetproviders.image = request.FILES['logo'] 
        Internetproviders.objects.create(logo=logo)
        return redirect('Internetproviders')
    return render(request, 'create-interprovider.html')

def OurAudienceCreate_Funk(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
            OurAudience.image = request.FILES['image'] 
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        OurAudience.objects.create(image=image, text_uz=text_uz, text_ru=text_ru,text_en=text_en, name_uz=name_uz, name_ru=name_ru,name_en=name_en)
        return redirect('OurAudience')
    return render(request, 'create-ouraudience.html',)


def PercentageCreate_Funk(request):
    if request.method == 'POST':

        percent= request.POST.get('percent')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        Percentage.objects.create(percent=percent,name_uz=name_uz,name_ru=name_ru,name_en=name_en)
        return redirect('Percentage')

    return render(request, 'create-percentagte.html')

def ResidentsCreate_Funk(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
            Residents.image = request.FILES['image']
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        Residents.objects.create(name_uz=name_uz,name_ru=name_ru,name_en=name_en,image=image)
        return redirect('Residents')
    return render(request, 'create-residents.html')

def CreateTeam_funk(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
            Team.image = request.FILES['image']
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        Team.objects.create(text_uz=text_uz,text_ru=text_ru,text_en=text_en,image=image)
        return redirect('Team')
    return render(request, 'create-team.html')

def CreateCoimages_Funk(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
            Coimages.image = request.FILES['image'] 
        Coimages.objects.create(image=image)
        return redirect('Coimages')
    return render(request, 'create-coimages.html')


def CoworkingCreate_Funk(request):
    coworking = Coworking.objects.all().order_by('-id')
    coimages = Coimages.objects.all().order_by('-id')
    context = {
        "coworking":coworking,
        "coimages":coimages,
    } 
    if request.method == "POST":
        data = request.POST
        images = []
        for img in request.POST.getlist('image'):
            images.append(Coimages.objects.get(id=img))
        print(images)
        a = Coworking.objects.create(
            text_uz = data.get('text'),
            text_ru = data.get('text_ru'),
            text_en = data.get('text_en'),
        )
        a.image.set(images)
        a.save()
        return redirect('Coworking')
    return render(request, 'coworking-create.html', context)



def CreateInfrastructureCreate_Funk(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
            Team.image = request.FILES['image']
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        InfrastructureSlider.objects.create(text_uz=text_uz,text_ru=text_ru,text_en=text_en,image=image)
        return redirect('InfrastructureSlider')
    return render(request, 'create-infrastructureSlider.html')


def CreateStudyDirections_Funk(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
                StudyDirections.image = request.FILES['image'] 
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        title_en = request.POST.get('title_en')
        StudyDirections.objects.create(image=image, text_uz=text_uz, text_ru=text_ru,text_en=text_en, tittle_uz=title_uz, tittle_ru=title_ru,tittle_en=title_en)
        return redirect('StudyDirections')
    return render(request, 'create-StudyDirections.html')


def CreateItAcademy(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
                ItAcademy.image = request.FILES['image'] 
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        texnologies = request.POST.get('texnologies')
        duration = request.POST.get('duration')
        start = request.POST.get('start')
        ItAcademy.objects.create(name_uz=name_uz, name_ru=name_ru,name_en=name_en,texnologies=texnologies,duration=duration,start=start,image=image)
        return redirect('ItAcademy')
    return render(request, 'create-itacademy.html')

def CreateStartUp(request):
    if request.method == 'POST':
        logo = request.FILES['icon']
        if logo in request.FILES:
            StartupDirections.logo = request.FILES['logo']
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        StartupDirections.objects.create(icon=logo,name_ru=name_ru,name_en=name_en,name_uz=name_uz)
        return redirect('StartupDirections')
    return render(request, 'create-StartUp.html')

def CreateIncubationCenters(request):
    if request.method == 'POST':
        logo = request.FILES['icon']
        if logo in request.FILES:
            IncubationCenters.logo = request.FILES['logo']
        name_uz = request.POST.get('text_uz')
        name_ru = request.POST.get('text_ru')
        name_en = request.POST.get('text_en')
        IncubationCenters.objects.create(icon=logo,text_uz=name_uz, text_ru=name_ru,text_en=name_en)
        return redirect('IncubationCenters')
    return render(request, 'create-IncubationCenters.html')

def CreateRaqamlashtirish(request):
    if request.method == "POST":
        image = request.FILES['image']
        if image in request.FILES:
            Raqamlashtirishxizmalari.image = request.FILES['image'] 
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        Raqamlashtirishxizmalari.objects.create(name_uz=name_uz,name_ru=name_ru,name_en=name_en,image=image,text_uz=text_uz, text_ru=text_ru,text_en=text_en)
        return redirect('Raqamlashtirishxizmatlari')
    return render(request, 'create-raqamlashtirish.html')


def CreateXizmatlar(request):
    if request.method == 'POST':
        price  = request.POST.get('price')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        XizmatTuri.objects.create(price=price ,name_ru=name_ru,name_en=name_en,name_uz=name_uz)
        return redirect('Xizmatlar')
    return render(request, 'create-xizmatlar.html')