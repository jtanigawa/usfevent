from event.models import Message
from accounts.models import UserProfile
from taggit.models import Tag


def base_template_vals(request):
    template_var = {}
    template_var["msg_received_list"] = ""
    template_var["msg_unread"] = ""    
    
    if request.user.is_authenticated():
        current_user_profile = UserProfile.objects.filter(
                                    django_user=request.user)[0]
        template_var["u"] = current_user_profile
        messages = Message.objects.filter(msg_to=current_user_profile)
        template_var["msg_received_list"] = messages
        msg_unread = 0
        for message in messages:
            if message.is_read == False:
                msg_unread += 1
        template_var["msg_unread"] = msg_unread

        template_var["tags"] = Tag.objects.all()

    return template_var
