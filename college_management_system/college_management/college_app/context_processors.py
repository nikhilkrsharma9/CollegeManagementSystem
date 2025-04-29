# college_app/context_processors.py
from .models import InstitutionalInfo

def institutional_info(request):
    info = InstitutionalInfo.objects.first()
    return {'institutional_info': info}