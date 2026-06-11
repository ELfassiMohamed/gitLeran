

class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    
    # Use email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
   
    
    def __str__(self):
        return self.email
    

