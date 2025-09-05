welcome_prompt = "Welcome doctor, what would you ike to do today?\n - To list all patients, press 1\n - To run a new diagnostic, press 2\n - To exit, press q\n"

name_prompt = "What is the patient's name?\n"

appearance_prompt = "How is the patient's appearance?\n - 1: Normal appearance\n - 2:Irritable or lethargic\n"
eyes_prompt = "How is the patient's eyes?\n - 1: Eyes Normal or slightly sunken \n - 2: Eyes very sunken\n"

severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"


def list_patients():
  print("Listing patient and diagnoses")


def assess_skin():
  print("Assessing skin")


def assess_eyes():
  eyes = input(eyes_prompt)
  if eyes == "1":
    return no_dehydration
  elif eyes == "2":
    return severe_dehydration


def assess_appearance():
  appearance = input(appearance_prompt)
  if appearance == "1":
    diagnosis = assess_eyes()
  elif appearance == "2":
    assess_skin()


def start_new_disgnosis():
  name = input(name_prompt)
  assess_appearance()


def main():
  while (True):
    selection = input(welcome_prompt)
    if selection == "1":
      list_patients()
    elif selection == "2":
      start_new_disgnosis()
    elif selection == "q":
      return


main()
