# Generated by Django 3.2.9 on 2021-11-24 10:35

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('referelcode', models.CharField(blank=True, default='', max_length=20)),
                ('refererid', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('wallet', models.IntegerField(default=0)),
                ('dateofbirth', models.CharField(blank=True, default='', max_length=20)),
                ('adhaarcard', models.CharField(blank=True, default='', max_length=20)),
                ('phone_no', models.CharField(blank=True, default='', max_length=20)),
                ('secondary_no', models.CharField(blank=True, default='', max_length=20)),
                ('is_phone_verified', models.BooleanField(default=False, verbose_name='Phone Verification')),
                ('is_email_verified', models.BooleanField(default=True, verbose_name='Email Verification')),
                ('verified_code', models.CharField(max_length=30)),
                ('reset_password', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('home_address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('profile_image', models.CharField(blank=True, max_length=225, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('owner_name', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_name', models.CharField(blank=True, max_length=255, null=True)),
                ('registration_date', models.DateTimeField(blank=True, null=True)),
                ('gst_state', models.CharField(blank=True, max_length=255, null=True)),
                ('gst_type', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_city', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_landmark', models.CharField(max_length=255, null=True)),
                ('pin_code', models.IntegerField(default=0, null=True)),
                ('shop_image', models.CharField(blank=True, max_length=225, null=True)),
                ('user_type', models.IntegerField(default=0, null=True)),
                ('account', models.CharField(blank=True, max_length=225, null=True)),
                ('is_shop_verified', models.BooleanField(default=False)),
                ('owner_image', models.CharField(blank=True, max_length=225, null=True)),
                ('floor_no', models.IntegerField(default=0, null=True)),
                ('mall_name', models.CharField(blank=True, max_length=225, null=True)),
                ('state', models.CharField(blank=True, max_length=225, null=True)),
                ('shop_area', models.CharField(blank=True, max_length=225, null=True)),
                ('shop_comment', models.CharField(blank=True, max_length=225, null=True)),
                ('owner_comment', models.CharField(blank=True, max_length=225, null=True)),
                ('is_submitted', models.BooleanField(default=False)),
                ('is_auth', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Profileinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Information', models.TextField(blank=True, null=True)),
                ('philisophy', models.TextField(blank=True, null=True)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('toprecipe', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=225, null=True)),
                ('selectedimage5', models.IntegerField(default=9, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(default='admin', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='petapp.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_list', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='petapp.product')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_add', to='petapp.product')),
            ],
            options={
                'verbose_name_plural': 'Carts',
                'ordering': ('-price',),
            },
        ),
    ]
