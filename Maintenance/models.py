from django.db import models


class ServiceType(models.Model):
    service_type = (
        ('tyre_replacement', 'Tyre Replacement'),
        ('suspension_repair', 'Suspension Repair'),
        ('ac_repair', 'AC Repair'),
    )


serviceType = models.CharField(max_length=50, choices=ServiceType)


class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()


class MaintenanceStatus(models.Model):
    status = (
        ('overdue', 'Over Due'),
        ('completed', 'Completed'),
        ('due', 'Due'),
        ('in_progress', 'In Progress'),
    )


maintenance_status = models.CharField(max_length=50, choices=MaintenanceStatus)


class SelectedDrivers(models.Model):
    drivers = (
        ('akbar', 'Akbar'),
        ('anas', 'Anas'),
        ('sharjeel', 'Sharjeel'),
        ('afzaal', 'Afzaal')
    )


Drivers = models.CharField(max_length=50, choices=SelectedDrivers)


class Vehicles(models.Model):
    vehicle = (
        ('corolla', 'Toyota Corolla'),
        ('civic', 'Honda Civic'),
        ('city', 'Honda City'),
    )


Vehicles = models.CharField(max_length=50, choices=Vehicles)


class Maintenance(models.Model):
    technician = models.CharField(max_length=100)
    fleet = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    start_date = models.DateField()
    delivery_date = models.DateField()
    next_maintenance_date = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
