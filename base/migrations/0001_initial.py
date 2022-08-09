# Generated by Django 4.0.5 on 2022-07-06 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departure_Time', models.DateTimeField(auto_now_add=True)),
                ('Landing_Time', models.DateTimeField(auto_now_add=True)),
                ('Remaining_Tickets', models.IntegerField()),
                ('Airline_Company_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.airline_companies')),
                ('Destination_Country_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.countries')),
                ('Origin_Country_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Origin_Country_Id', to='base.countries')),
            ],
        ),
        migrations.CreateModel(
            name='User_Roles',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Role_Name', models.CharField(choices=[('CU', 'Customer'), ('AC', 'Airline Company'), ('AD', 'Admin')], default='CU', max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Username', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=256, null=True, unique=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('User_Role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.user_roles')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.TextField(blank=True, max_length=50, null=True)),
                ('Last_Name', models.TextField(blank=True, max_length=50, null=True)),
                ('Address', models.TextField(blank=True, max_length=50, null=True)),
                ('Phone_No', models.TextField(blank=True, max_length=50, null=True, unique=True)),
                ('Credit_Card_no', models.TextField(blank=True, max_length=50, null=True, unique=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('User_Id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.users')),
            ],
        ),
        migrations.AddField(
            model_name='airline_companies',
            name='Country_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.countries'),
        ),
        migrations.AddField(
            model_name='airline_companies',
            name='User_ID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.users'),
        ),
        migrations.CreateModel(
            name='Adminstrators',
            fields=[
                ('Id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('First_Name', models.TextField(blank=True, max_length=50, null=True)),
                ('Last_Name', models.TextField(blank=True, max_length=50, null=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('User_Id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.users')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.customers')),
                ('Flight_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.flights')),
            ],
            options={
                'unique_together': {('Flight_Id', 'Customer_Id')},
            },
        ),
    ]
