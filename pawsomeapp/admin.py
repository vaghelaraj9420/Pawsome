from django.contrib import admin
from .models import Pets
from .models import pList
from .models import ppList
from .models import daycare
from .models import caretaker
from .models import Contact
from .models import Orders
from .models import vet



# Register your models here.

admin.site.register(Pets)
admin.site.register(pList)
admin.site.register(ppList)
admin.site.register(daycare)
admin.site.register(caretaker)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(vet)