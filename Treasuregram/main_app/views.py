from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, 'index.html', {'treasures': treasures})

class Treasure:
    def __init__(self, name, value, material, location, image):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.image = image

treasures = [
    Treasure('Pumpkin', 500.00, 'organic', 'Aspen', '../static/images/jack-o-lantern-light.svg'),
    Treasure('Iron pyrite', 2.00, 'not real gold', 'Cripple Creek', '../static/images/badger-honey-regular.svg'),
    Treasure('Coffee can', 20.00, 'tin', 'Colorado Springs, CO', '../static/images/deer-solid.svg')
]