1. Open Project and Create Virtual Environment
2. pip install -r requirements.txt
3. Create User
    python manage.py createsuperuser --username krishna --email krishna@gmail.com
4. Generate tokens
    python manage.py drf_create_token krishna
    Generated token d173bb565c34e9ea9ab37b75b4d4fb23a3620c2f for user krishna
5. Run test.py file of api_test