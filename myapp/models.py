from django.db import models

# Create your models here.


class generalParticulars(models.Model):
    Institution = models.CharField(max_length=100, null=True)
    County = models.CharField(max_length=100)
    Subcounty = models.CharField(max_length=100)
    Building = models.CharField(max_length=100)
    Floor = models.CharField(max_length=100)
    Town = models.CharField(max_length=100)
    Postaladdress = models.CharField(max_length=100,null=True)
    Postalcode = models.IntegerField(null=True)
    Telephone = models.IntegerField(null=True)
    Phone = models.IntegerField(null=True)
    Email = models.EmailField(max_length=70,blank=True)
    Institutioncategory = models.CharField(max_length=50)
    InstitutionType = models.CharField(max_length=50)

class studentIntake(models.Model):
    Institution = models.CharField(max_length=100, null=True)

    Course = models.CharField(max_length=100)
    Courselevel = models.CharField(max_length=100)
    Cost = models.IntegerField(null=True)
    Intakeyear = models.IntegerField(null=True)
    Gender = models.CharField(max_length=50)


class outrunsGraduates(models.Model):
    Institution = models.CharField(max_length=100, null=True)

    Course =models.CharField(max_length=200)
    CourseLevel = models.CharField(max_length=200)
    CourseDuration = models.CharField(max_length=100)
    ExaminingBody = models.CharField(max_length=200)
    Year = models.IntegerField(null=True)
    Gender = models.CharField(max_length=50)

class staffTotal(models.Model):
    Institution = models.CharField(max_length=100, null=True)

    NumberOfStaff = models.IntegerField(null=True)
    NumberOfStaffWithDissability = models.IntegerField(null=True)
    SkillArea = models.CharField(max_length=100)
    SkillLevel = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)


class skillShortage(models.Model):
    Institution = models.CharField(max_length=100, null=True)

    SkillArea = models.CharField(max_length=100)
    SkilllevelRequired = models.CharField(max_length=100)
    Optimal = models.CharField(max_length=100)
    InPostGender = models.CharField(max_length=100)
    ShortFall = models.CharField(max_length=200)
    ReasonsForShortFall = models.CharField(max_length=1000)


class challenges(models.Model):
    Institution = models.CharField(max_length=100, null=True)

    CovidEffects = models.CharField(max_length=100)
    OtherChallenges = models.CharField(max_length=100)
    OtherChallengesSelected = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    ContactNumber = models.IntegerField(null=True)
    EmailAddress = models.EmailField(max_length=70,blank=True)
    date =models.DateField(blank=True)
    Officer = models.CharField(max_length=50)