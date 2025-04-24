from django.db import models
from django.urls import reverse  # Helps with generating URL paths
from datetime import date  # For checking today's feedings
from django.contrib.auth.models import User  # Needed for user-cat relationship

# Choices used for the 'meal' field in Feeding model
# First value is stored in the database, second is the human-readable label
MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner"),
)

# ---------------------------
# Toy Model
# ---------------------------

class Toy(models.Model):
    # Represents a toy a cat can have (many-to-many with Cat)

    name = models.CharField(max_length=50)
    # Toy name (e.g., 'Laser Pointer')

    color = models.CharField(max_length=20)
    # Color of the toy (e.g., 'Red')

    def __str__(self):
        # String representation for admin panel or shell
        return self.name

    def get_absolute_url(self):
        # Tells Django where to redirect after Create/Update
        # Used by ToyCreate and ToyUpdate views
        # PK - because we are using class based views
        return reverse("toy-detail", kwargs={"pk": self.id})


# ---------------------------
# Cat Model
# ---------------------------

class Cat(models.Model):
    # Represents a cat a user can view, feed, or assign toys to

    name = models.CharField(max_length=100)
    # Name of the cat (e.g., 'Mittens')

    breed = models.CharField(max_length=100)
    # Breed (e.g., 'Siamese')

    description = models.TextField(max_length=250)
    # A short bio or story about the cat

    age = models.IntegerField()
    # Age in years (can be 0 if kitten)

    toys = models.ManyToManyField(Toy)
    # Many-to-Many: a cat can have multiple toys, and toys can belong to multiple cats

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ☝️ This line links a cat to a user

    def __str__(self):
        # Used in admin panel or shell
        return self.name

    def get_absolute_url(self):
        # Used after Create/Update to redirect to detail view
        return reverse("cat-detail", kwargs={"cat_id": self.id})


# ---------------------------
# Feeding Model
# ---------------------------

class Feeding(models.Model):
    # Represents one meal for one cat on one day

    date = models.DateField("Feeding date")
    # Date the feeding happened (e.g., '2025-04-24')

    meal = models.CharField(
        max_length=1,
        choices=MEALS,  # Choices defined above
        default=MEALS[0][0]  # Default to 'B' (Breakfast)
    )
    # Meal type: Breakfast, Lunch, or Dinner

    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    # Connects feeding to one cat
    # CASCADE means if the cat is deleted, so are its feedings

    def __str__(self):
        # Readable format like 'Lunch on 2025-04-24'
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]
        # Feedings will show up with newest ones first by default