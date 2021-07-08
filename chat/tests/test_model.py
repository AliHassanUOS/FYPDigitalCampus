from chat.models import Room, Message

from django.test  import TestCase



class Room_check(TestCase):

    def SetUp(self):
        Room.obejcts.create(name = ' New Room ')

    def test_room_created(self):
        room = Room.objects.get(id = 1)
        name = "New Room"
        self.assertEqual(room.name, name)
        

class message_check_test(TestCase):
    def  setup(self):
        Message.objects.create(value = "new message")

    
    def test_room_created(self):
        room = Room.objects.get(id = 1)
        name = "New Room"
        self.assertEqual(room.name, name)
        
    









