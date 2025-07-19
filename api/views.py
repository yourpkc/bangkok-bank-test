from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from api.forms import BookingForm
from api.models import Booking
from api.serializers import BookingSerializer
from django.contrib.auth.models import User

@login_required
def landing_page(request):
    queryset = Booking.objects.all().order_by('-booking_datetime')
    # print("===========", (request.user))
    # if not request.user.is_superuser():
    #     queryset = queryset.filter(user=request.user)

    context = {
        'bookings': queryset,
        # 'bookings': BookingSerializer(queryset, many=True).data,
    }
    return render(request, 'landing.html', context)

@login_required
def booking_page_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('landing_page')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
