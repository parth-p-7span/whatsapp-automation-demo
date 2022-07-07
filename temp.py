from firebase import Firebase

Firebase.initialize_firebase()

# response = Firebase.create_user("918780495805", "Parth Panchal")
# response = Firebase.update_user("918780495805", "name", "Parth H Panchal")
response = Firebase.get_user_data("917227856454")
print(response)