# _*_ coding: utf-8 _*_
from tDjango.mtv.models import Publisher,Person,Author,Book
from django.utils.datetime_safe import date
if __name__ == '__main__':
    p1=Publisher(name='emilyPublisher',address='emily1Publisher.home',email='emilyPublisher@s.com')
    p1.save()
    a=Author.authorInstance("emily","zhu","emily@s.com")
    a.save()
    a1=Author.authorInstance("emily1","zhuzhu","emily.zhu@s.com")
    a1.save()
    b=Book(title="emily's the first book",publisher=p1,date=date.today()) 
     
    #####----设置多对多关系时，必须先保存本对象，因为python用了中间表保存，所以必须先保存才能有ID入中间表
    b.save()
    b.authors=(a,a1)
    b.save()
    b2=Book.bookInstance("emily's the second book", p1, date.today())
    b2.save()
    b2.authors=[a1]
    b2.save()
   


    #####-------many-to-one  one的一方默认一个（有many对应的class_set）many方的引用（onerelationmanage对象），
    ##########------------取出many方的数据必须调all()才能转成集合使用
    bl=Publisher.objects.all()[0].book_set.all()
    for b in bl:
       print b
        
    ##### many-relation_objects must invoke all()----iterator so get the value   
    al=Book.objects.all()[0].authors.all()
    for at in al:
        print at    

    
    p=Person.personInstance('zhuyijuanq','m')
    p.save()
    p=Person.objects.all()[0]
    #####----shirt_size的使用类似于java中的enum，所有在person申明中用了tuple定义了常量，
    #####-------------get_shirt_size_display调用了tuple对应的字典中的value,数据库中存入的是 key
    print p.shirt_size
    print p.get_shirt_size_display()
    
    
#    
#    