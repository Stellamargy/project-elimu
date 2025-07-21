from flask import Blueprint
# Create Blueprint then register it with app
#Creating auth blueprint
auth=Blueprint('auth',__name__,'/auth')

#Route to add users
    