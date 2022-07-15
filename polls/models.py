from django.db import models

# Create your models here.
class Question(models.Model):
    #number
    #name
    #pub.date
    #no need for this line of code cos django does the auto for us.
    question_text = models.CharField(max_length=255)
    question_description = models.CharField(max_length=255, default= "Basic Description")
    pub_date = models.DateTimeField(auto_now_add=True)

# 4)                   "Are you happy about Djagno"                                     "June 16, 09:50 WAT"
# 5)                   "ARE YOU .."                                                    "JUNE 17, 10:00 WAT"


    def __str__(self):
        return self.question_text


class Choices(models.Model):
    #number of choice
    # link to a question
    # choice_of_answer           [yes/no]
    # votes

   #django has done the auto id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    vote = models.IntegerField(default=0)


# 1)                  "Are you happy about Djagno"                yes/no              3/0


def __str__(self):
        return self.choice_answer