from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from blog.models import Hobies,Categories,Hotel
from .forms import HotelForm
def handler404(request, exception):
    # istenilen sayfaya yönlendirme yap
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return redirect('logout')
def home(request):
    if not request.user.is_authenticated:
        return redirect("logout")
    active_page="home"
    return render(request,"blog/home.html",{"active_page":active_page})
def hobies(request):
    if not request.user.is_authenticated:
        return redirect("logout")
    context={
        "kullanilacakveriler":Hobies.objects.filter(is_showed=True),
        "kategoriler":Categories.objects.all(),
        "active_page":"hobies",
    }
    return render(request,"blog/hobies.html",context)

def about(request):
    if not request.user.is_authenticated:
        return redirect("logout")
    detay={
    "active_page":"about",}
    return render(request,"blog/about.html",detay)
def hobydetails(request ,yol,id):
    if not request.user.is_authenticated:
        return redirect("logout")
    veridetaylari=Hobies.objects.get(yol=yol,id=id)
    #veridetaylari=veriler["hobies"]
    # # selection=None
    # # for i in veridetaylari:
    # #     if i["id"]==id:
    # #         selection=i
    #selection=[i for i in veridetaylari if i["id"]==id][0]
    return render(request,"blog/hobydetails.html",{'secim':veridetaylari,"active_page":"hobidetay",})
def hobies_by_categories(request ,yol):
    if not request.user.is_authenticated:
        return redirect("logout")
    context={
        "kullanilacakveriler":Hobies.objects.filter(is_showed=True,kategori__yol=yol),#kategori__yol models.py dosyasında hobieste belirttiğimiz kategori alanı ve __  başka bir alana geçtiğimiz bilgisini verir yol ise Categories Sınıfının nesnesidir.
        "kategoriler":Categories.objects.all(),
        "selected_kategori":yol,
        "active_page":"hobies",
    }
    return render(request,"blog/hobies.html",context)

# veriler={
#     "hobies":[
#         {
#         "id":1,
#         "title": "archery:",
#         "image":"Archery.gif",
#         "description": """
#             The main benefits of archery are strength building and improved hand-eye coordination. By practicing the sport you’ll also benefit your focus, patience, and self-confidence, and relax by spending more time outside. Overall archery has a lot of physical and mental health benefits.<br/> Archery involves a lot of muscles, mainly in your upper body. These include your back, shoulders, core, and arms, but other parts of your body are involved in the movements as well. The short bursts of hard exercise are really great for building strength and developing your muscles. With proper form, archery can stimulate a lot of muscle growth.
#             Along with the strength building, archery also involves a lot of cardio. Running from target to target in a 3D shoot or to retrieve your arrows are only some of the examples. Clearly, some types of archery, like 3D and field archery, involve more cardio exercise than others, but all have some aspects of cardio in them.
#             Surprisingly, a lot of calories are burned when practicing archery. A research many people like to show when discussing this, by The Economist, was done on Olympic gold medal winners and stated that archery is among the top calories burning sports. So if you’re tired of running on a treadmill, pick up a bow and start practicing.
#         """,
#         "is_showed":True
#         },
#         {
#         "id":2,
#         "title": "Drink Tea:",
#         "image":"tea.gif",
#         "description": """
#             Is Turkish Tea Good for You?<br/>
#             Called Cay in Turkish, as well as being a social experience, black Turkish tea has many health benefits. For example, Netherlands Studies showed that Turkish black tea helps regulate heart blood vessels, leading to fewer chances of strokes or heart attacks. In addition, flavonoids in black tea keep cholesterol down, help to stabilise our metabolism and lead to a reduced risk of diabetes. Turkish tea is also said to help with obesity and stress. Estimates say Turks drink the most tea globally, and Turkey ranks as the fifth-highest exporter; hence everyone can tap into health benefits.""",
#         "is_showed":False
#         },
#         {
#         "id":3,
#         "title": "Drink Coffe:",
#         "image":"coffe.gif",
#         "description": """
#             The average number of cups per person per day is 3, and this hasn’t changed since 1999. It’s safe to say that most of us love our coffee. And fortunately, coffee is one of the healthiest things you can consume, with benefits for nearly every aspect of your health.
#             In this in-depth guide, I want to illustrate both the benefits and the potential downsides of coffee, and how we can use coffee in a smart way to improve our health, our performance (both physical and mental), and ultimately, improve our lives.""",
#         "is_showed":True
#         }
#     ]
# }
def upload_hoby(request):
    if not request.user.is_authenticated:
        return redirect("logout")
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'blog/upload_hoby.html', {'form': form})
 
 
def success(request):
    if not request.user.is_authenticated:
        return redirect("logout")
    detay={
    "bilgilendirme":"successfully uploaded",}
    return render(request,"blog/success.html",detay)

def display_hotel_images(request):
    if not request.user.is_authenticated:
        return redirect("logout")
    if request.method == 'GET':
 
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
        return render(request, 'blog/hotels.html',
                       {'hotel_images': Hotels,
                        "active_page":"hotels",})