from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, 'index.html', {'treasures': treasures})

class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location

treasures = [
    Treasure('Gold nugget', 500.00, 'gold', 'Aspen, CO'),
    Treasure('Iron pyrite', 2.00, 'not real gold', 'Cripple Creek'),
    Treasure('Coffee can', 20.00, 'tin', 'Colorado Springs, CO')
]