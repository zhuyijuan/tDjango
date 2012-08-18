'''
Created on 2012-8-15

@author: dell
'''
from tDjango.mtv.models import Publisher
if __name__ == '__main__':
    p1=Publisher(name='emily1',address='emily1.home',email='emily1@s.com')
   # p1.save()
    p_list=Publisher.objects.all()
   # print p_list
    
    p2=Publisher.create("zyj","addd")
    print p2
    #for p in p_list:
       # print p