import jwt
from flask import current_app
from datetime import datetime,timezone

class TokenManager():
    
    # create issued at token claim in eposh seconds
    @staticmethod
    def get_issued_at():
        # Use Utc with timezone for easy calculation 
        iat=datetime.now(timezone.utc)
        #convert issued at to eposh seconds
        epoch_iat = int(iat.timestamp())
        return epoch_iat
    #create expiry token  claim
    @staticmethod
    def get_expiry():
        # Expiry duration in seconds
        expiry_duration=3600
        epoch_exp=TokenManager.get_issued_at() + expiry_duration
        return epoch_exp
        
    #creates payload (used in token creation)
    @staticmethod
    def create_payload(user):
        payload={
            
                "iss": "project-elimu",
                "sub": f"user-{user.id}",
                "iat": TokenManager.get_issued_at(),
                "exp": TokenManager.get_expiry(),
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

