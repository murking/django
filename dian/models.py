#coding:utf-8

from django.db import models

# Create your models here.

class Dish(models.Model):
    dish_id=models.PositiveIntegerField(verbose_name='菜品号')
    dish_name=models.CharField(max_length=2000,null=True ,verbose_name='菜名')
    dish_imag=models.FileField(verbose_name='菜品图片',upload_to='images/',max_length=255)
    dish_price=models.PositiveIntegerField(verbose_name='价格')
    dish_class=models.PositiveIntegerField(verbose_name='类型')

    def __unicode__(self):
        return self.id

    @classmethod
    def get_all_dishes(cls):
        return Dish.objects.all()

    @classmethod
    def get_zhushi(cls):
        dish_zhu=Dish.objects.filter(dish_class=1)
        return dish_zhu

    @classmethod
    def get_cai(cls):
        dish_cai=Dish.objects.filter(dish_class=0)
        return dish_cai
    @classmethod
    def get_sh(cls):
        dish_sh=Dish.objects.filter(dish_class=2)
        return dish_sh

    @classmethod
    def creat_dish(cls,id,name,imag):
        dish=Dish.objects.create(dish_id=id,dish_name=name,dish_imag=imag)
        return dish


class Customer(models.Model):
    customer_room=models.CharField(max_length=10,verbose_name='房间号')
    customer_dishs=models.CharField(max_length=45,verbose_name='菜表')
    customer_sum=models.PositiveIntegerField(verbose_name='总价')
    customer_statu=models.PositiveIntegerField(verbose_name='状态')

    def __unicode__(self):
        return self.id

    @classmethod
    def create(cls,room,dishs,price):
        customer=Customer.objects.create(customer_room=room,customer_dishs=dishs,customer_sum=price,customer_statu=0)
        return customer

    @classmethod
    def get_all_Customer(cls):
        Customers=Customer.objects.all()
        return Customers

    @classmethod
    def get_one(cls,room):
        customer=Customer.objects.filter(customer_room=room)
        return customer

    @classmethod
    def get_by_time(cls):
        customer=Customer.objects.filter(customer_statu=0).order_by('id')
        return customer

    @classmethod
    def change(cls,id):
        Customer.objects.filter(id=id).update(customer_statu=1)

    @classmethod
    def delete_room(cls,room):
        Customer.objects.filter(customer_room=room).delete()


class Cook(models.Model):
    cook_user=models.CharField(max_length=10,verbose_name='用户名')
    cook_pas=models.CharField(max_length=10,verbose_name='密码')


    def __unicode__(self):
        return self.id

    @classmethod
    def get_by_user(cls,user,pas):
        cook=Cook.objects.filter(cook_user=user)
        return cook

