import jwt
# from server.app import app
from flask import current_app

class TokenManager():
    
        
    #creates payload (used in token creation)
    @staticmethod
    def create_payload(user):
        payload={
            
                "iss": "project-elimu",
                "sub": f"user-{user.id}",
                # later implementation after basic token implementation
                # "iat": 1691234567,
                # "exp": 1691244567,
                "user_id": user.id,
                "email": user.email,
                "role": user.role_id,
                "is_active": user.active
            
            }
        return payload
    # cls method to create token
    @classmethod
    def create_token(cls,user):
        #payload
        payload=TokenManager.create_payload(user)
        #secret key
        secret_key=current_app.config['SECRET_KEY']
        token=jwt.encode(payload, secret_key, algorithm="HS256")
        return token
    
    #I will write the method to decode token in order to get user identity later 
    