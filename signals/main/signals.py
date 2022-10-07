from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete,pre_init,pre_save,post_delete,post_init,post_save
from django.core.signals import request_finished,request_started,got_request_exception

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("logged in")

@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("login failed")


#user_logged_in.connect(login_success,sender=User)

@receiver(pre_save,sender=User)
def begining_save(sender,instance,**kwargs):
    print("Begining of save")

@receiver(post_save,sender=User)
def ending_save(sender,instance,created,**kwargs):
    print("Ending of save")

@receiver(pre_delete,sender=User)
def ending_delete(sender,instance,**kwargs):
    print("Ending of delete")

@receiver(request_started)
def at_request_start(sender,environ,**kwargs):
    print("Http request started")
#request_started.connect(at_request_start)

@receiver(request_finished)
def at_request_finished(sender,**kwargs):
    print("Http request finished")

@receiver(got_request_exception)
def at_got_request_exception(sender,request,**kwargs):
    print("Http request exception")
