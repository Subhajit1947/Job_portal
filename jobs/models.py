from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
User = get_user_model()

class JobCategory(models.TextChoices):
    SOFTWARE_ENGINEERING = 'SOFTWARE_ENGINEERING', _('Software Engineering')
    DATA_SCIENCE = 'DATA_SCIENCE', _('Data Science')
    CYBERSECURITY = 'CYBERSECURITY', _('Cybersecurity')
    CLOUD_ENGINEERING = 'CLOUD_ENGINEERING', _('Cloud Engineering')
    DEVOPS = 'DEVOPS', _('DevOps')
    AI_ML = 'AI_ML', _('AI & ML')
    UI_UX_DESIGN = 'UI_UX_DESIGN', _('UI/UX Design')
    IT_SUPPORT = 'IT_SUPPORT', _('IT Support')
    NETWORK_ENGINEERING = 'NETWORK_ENGINEERING', _('Network Engineering')
    DATABASE_ADMIN = 'DATABASE_ADMIN', _('Database Administration')

class JobType(models.TextChoices):
    FULL_TIME = 'FULL_TIME', _('Full-Time')
    PART_TIME = 'PART_TIME', _('Part-Time')
    CONTRACT = 'CONTRACT', _('Contract')
    FREELANCE = 'FREELANCE', _('Freelance')
    INTERN = 'INTERN', _('Internship')

class Location(models.TextChoices):
    MUMBAI = 'MUMBAI', _('Mumbai')
    DELHI = 'DELHI', _('Delhi')
    BENGALURU = 'BENGALURU', _('Bengaluru')
    HYDERABAD = 'HYDERABAD', _('Hyderabad')
    CHENNAI = 'CHENNAI', _('Chennai')
    KOLKATA = 'KOLKATA', _('Kolkata')
    PUNE = 'PUNE', _('Pune')
    AHMEDABAD = 'AHMEDABAD', _('Ahmedabad')
    JAIPUR = 'JAIPUR', _('Jaipur')
    CHANDIGARH = 'CHANDIGARH', _('Chandigarh')
    KOCHI = 'KOCHI', _('Kochi')
    BHUBANESWAR = 'BHUBANESWAR', _('Bhubaneswar')
    INDORE = 'INDORE', _('Indore')
    LUCKNOW = 'LUCKNOW', _('Lucknow')
    VISAKHAPATNAM = 'VISAKHAPATNAM', _('Visakhapatnam')
    

class Job(models.Model):
    class ExperienceLevel(models.TextChoices):
        ENTRY = 'ENTRY', _('Entry Level')
        MID = 'MID', _('Mid Level')
        SENIOR = 'SENIOR', _('Senior Level')
        LEAD = 'LEAD', _('Lead')
        EXECUTIVE = 'EXEC', _('Executive')

    class Mode(models.TextChoices):
        REMOTE = 'REMOTE', _('Remote')
        HIBRID = 'HIBRID', _('Hibrid')
        WORK_FROM_OFFICE = 'WORK FROM OFFICE', _('Work From Office')
        
    company_name=models.CharField(max_length=150,default='MicroSoft')
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    title = models.CharField(max_length=200)
    slug=AutoSlugField(populate_from="title",unique=True)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100,choices=Location.choices,default=Location.BENGALURU)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_currency = models.CharField(max_length=3, default='INR')
    category = models.CharField(max_length=100,choices=JobCategory.choices,default=JobCategory.SOFTWARE_ENGINEERING)
    job_type = models.CharField(max_length=100,choices=JobType.choices,default=JobType.FULL_TIME)
    experience_level = models.CharField(
        max_length=30,
        choices=ExperienceLevel.choices,
        default=ExperienceLevel.MID
    )
    mode=models.CharField(max_length=100,choices=Mode.choices,default=Mode.WORK_FROM_OFFICE)
    application_deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"{self.title} in {self.company_name}"

# class JobApplication(models.Model):
#     class ApplicationStatus(models.TextChoices):
#         PENDING = 'PENDING', _('Pending')
#         REVIEWED = 'REVIEWED', _('Reviewed')
#         INTERVIEW = 'INTERVIEW', _('Interview')
#         REJECTED = 'REJECTED', _('Rejected')
#         ACCEPTED = 'ACCEPTED', _('Accepted')

#     job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
#     applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
#     cover_letter = models.TextField()
#     resume = models.FileField(upload_to='resumes/')
#     status = models.CharField(
#         max_length=10,
#         choices=ApplicationStatus.choices,
#         default=ApplicationStatus.PENDING
#     )
#     applied_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         unique_together = ['job', 'applicant']
#         ordering = ['-applied_at']

#     def __str__(self):
#         return f"{self.applicant.username}'s application for {self.job.title}"