from djchoices import ChoiceItem, DjangoChoices


class TaskStatusChoices(DjangoChoices):
    TODO = ChoiceItem("To Do")
    WIP = ChoiceItem("Work in Progress")
    ONHOLD = ChoiceItem("On Hold")
    DONE = ChoiceItem("Done")
