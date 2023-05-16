from django.shortcuts import render, get_object_or_404
from apps.chat.models import Thread, ChatMessage
from apps.user.forms import FriendForm
from apps.user.models import MatiCoffeeUser, Friend
from django.http import HttpResponse
from django.db.models import Q
from apps.chat.forms import ThreadForm

# Create your views here.
def chat_view(request):

    """
    View that contains the websocket path.
    It renders the chatbox depending the request.user

    Thread object filters a conversation among two persons.
    Condition 1: first_person is request.user.
    Condition 2: second_person is request.user
    """

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()

    user = get_object_or_404(MatiCoffeeUser, id= request.user.id)

    thread = Thread.objects.filter(
    Q(first_person=user.id, second_person=user.last_person_chat) |
    Q(first_person=user.last_person_chat, second_person=user.id)
).first()
    msgs = ChatMessage.objects.filter(thread = thread.id)
    return render(request, 'pages/chat_page.html', {"thread" : thread, 'msgs': msgs})

def set_last_person_msg(request):

    """
    When a user send msg to a contact or open any msg from history,
    The field last_person_chat should be updated with selected person
    from these views (contacts, msg history).
    """

    user = get_object_or_404(MatiCoffeeUser, id= request.user.id)
    if request.method == "POST":
        user.last_person_chat = int(request.POST['last_person_chat'])
        user.save()
        return HttpResponse('El ultimo chat fue actualizado', status= 200)
    return HttpResponse('Ocurrio un error', status=400)

def chats_view(request):

    """
    Messages History.
    Render the request.user threads.
    """

    threads = Thread.objects.by_user(user = request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {'Threads':threads}
    return render(request,'pages/chats.html', context)

def add_contacts_view(request):

    """
    Add contact view.

    This view renders all users in database with the possibility
    to add them

    if request == POST

    The view will create a Friend Request with is_approved in False by default.
    """

    users = MatiCoffeeUser.objects.values_list('username', 'id', 'profile_img')

    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("La solicitud de amistad se envio con exito", status=201)
        else:
            return HttpResponse("La solicitud a esa persona ya existe", status=400)
    else:
        form = FriendForm()

    return render(request, 'pages/add_contacts.html', {'users':users})

def contacts_view(request):

    """
    Contacts View

    This view returns all user friends with the condition that 
    these contains field is_approved in True.
    """

    user = MatiCoffeeUser.objects.get(id=request.user.id)
    friends = Friend.objects.filter(Q(user_to_request=user) | Q(user=user), is_approved=True)
    return render(request, 'pages/contacts.html', {'friends':friends})

def request_view(request):

    """
    Requests View

    This view returns all Friend objects with field is_approved in false.
    
    """

    user = MatiCoffeeUser.objects.get(id=request.user.id)
    request_profiles = Friend.objects.filter(Q(user_to_request=user), is_approved=False)
    return render(request, 'pages/requests.html', {'request_profiles': request_profiles})

def delete_request(request, pk):

    """
    Delete requests
    This view receives an id. If the method is post, the request (Friend Model)
    will be deleted.
    """

    obj = get_object_or_404(Friend, id = pk)

    if request.method == 'POST':
        obj.delete()
        return HttpResponse("La solicitud de amistad se elimino con exito", status=200)

def accept_request(request, pk):

    """
    Accept Requests

    From frontend will be sent a Post request with
    {'is_approved' : True} in request body, for 
    consequence Friend object will be updated with her
    field is_approved to True.
    
    """

    obj = get_object_or_404(Friend, id=pk)

    if request.method == 'POST':
        is_approved = request.POST.get('is_approved') == 'true'
        obj.is_approved = is_approved
        obj.save()
        return HttpResponse("La solicitud de amistad fue aceptada!", status=200)
    
    return HttpResponse("No se puede procesar la solicitud.", status=400)
