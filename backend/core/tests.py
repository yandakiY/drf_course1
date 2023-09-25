from .models import Contact
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class ContactTestCase(APITestCase):
    """
    Test suite for Contact
    """
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {
            "name": "my_name",
            "message": "my message",
            "email": "my_mail@maik.com"
        }
        
        self.url = "/contact/"
        
    def test_create_contact(self):
        '''
        test ContactViewSet create method
        '''
        
        data = self.data
        # test url /contact/
        response = self.client.post(self.url , data)
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count() , 1)
        self.assertEqual(Contact.objects.get().title , "my_name")
        
        
    def test_create_contact_without_name(self):
        
        data = self.data
        # remove prop "name"
        data.pop("name")
        # test response
        response = self.client.post(self.url , data)
        # results
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)
        
        
    def test_create_contact_with_blank_name(self):
        
        data = self.data
        # name eq blank
        data["name"] = ""
        # response
        response = self.client.post(self.url , data)
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)
        
        
    def test_create_contact_without_message(self):
        
        data = self.data
        # remove prop "name"
        data.pop("message")
        # test response
        response = self.client.post(self.url , data)
        # results
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)
        
    
    def test_create_contact_with_blank_message(self):
        
        data = self.data
        # name eq blank
        data["message"] = ""
        # response
        response = self.client.post(self.url , data)
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)
        
        
    def test_create_contact_without_email(self):
        
        data = self.data
        # remove prop "name"
        data.pop("email")
        # test response
        response = self.client.post(self.url , data)
        # results
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)
        
    
    def test_create_contact_with_blank_email(self):
        
        data = self.data
        # name eq blank
        data["email"] = ""
        # response
        response = self.client.post(self.url , data)
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)
        
    
    def test_create_contact_when_email_equals_non_email(self):
        '''
        test ContactViewSet create method when email is not email
        '''
        data = self.data
        # non email format
        data["email"] = "mail"
        # response
        response = self.client.post(self.url , data)
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)