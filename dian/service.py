#coding=utf-8

__author__ = 'zjh-mac'

from models import *
from operator import attrgetter

STATIC_IMAGE_URL = 'http://127.0.0.1:8000/front/static/images'

class DishService(object):
    @classmethod
    def get_all_dishes(cls):
        dishes = Dish.get_all_dishes()
        return dishes

    @classmethod
    def creat_dish(cls,id,name,image):
        dish=Dish.creat_dish(id,name,image)
        return dish

    @classmethod
    def get_cai(cls):
        cai=Dish.get_cai()
        return cai

    @classmethod
    def get_zhu(cls):
        zhu=Dish.get_zhushi()
        return zhu

    @classmethod
    def get_sh(cls):
        sh=Dish.get_sh()
        return sh

class CustomerSefvice(object):
    @classmethod
    def get_one_room(cls,room):
        customer=Customer.get_one(room)
        return customer

    @classmethod
    def create(cls,room,dish,price):
        customer=Customer.create(room,dish,price)
        return customer

    @classmethod
    def get_by_time(cls):
        customer_by_time = Customer.get_by_time()
        return customer_by_time

    @classmethod
    def change(cls,id):
        Customer.change(id)

    @classmethod
    def delet_room(cls,room):
        Customer.delete_room(room)

class Cookservice(object):
    @classmethod
    def get_by(cls,user,pas):
        user_by=Cook.get_by_user(user,pas)
        return user_by