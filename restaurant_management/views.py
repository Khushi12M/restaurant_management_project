from rest_framework.decorators import api_view
from rest_framework.response import response

def restaurant_menu(request):

    Menu =[
        {"name": "Paneer Butter Masala","description": "Creamy curry with paneer cubes", "price":250.00},
        {"name":" Chiken Biryani", "description": "Fragrant basmati rice with spiced chicken", "price": 300.00},
        {"name": "Veg Manchurian", "description": "Crispy vegetable balls in tangy sauce", "price": 220.00},
        {"name": "Masala Dosa", "description": "Crispy dosa stuffed with spiced potatoes", "prices": 150.00}


    ]
    return Response(Menu)
       
        

    