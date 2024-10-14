"""
## Challenge - 👟 Fitness App

- Imagine you are developing a program for a ***fitness*** app.
- The user is asked to input the duration of the workout in minutes,
  the type of exercise they did (e.g., *running*, *cycling*, *weightlifting*)
  and their location.
- The program then calculates the calories burned based on the workout type
  and duration.
- The program checks the current weather in the user's location.
- Additionally, it provides feedback on whether the user needs to hydrate
  more based on the workout intensity and weather.
- Finally, it displays the **total calories burned and the hydration recommendation**.
"""
def get_current_user_from_db():
    """
    Check currently logged in user, obtain instance from database
    :return: user
    """
    pass # TODO database team implement

def ask_workout_duration(current_user):
    """
    Given the current user, ask him/her what the workout duration was,
    make sure it is a valid amount of minutes.
    :param current_user:
    :return: minutes
    """
    pass # TODO workout design team implement

def get_exercise_options():
    """
    Return valid exercise options as list
    :return: minutes
    """
    pass # TODO workout design team implement

def ask_performed_exercises(current_user, exercise_options):
    """
    Given a list of exercise options, ask the user which ones they did.
    :param current_user:
    :param exercise_options:
    :return: List of picked exercises
    """
    pass # TODO workout design team implement

def ask_location(current_user):
    """
    Ask current user where the exercise was performed
    :param current_user:
    :return: Location
    """
    pass # TODO geo location team

def main():
    # Fetch user from db
    current_user = get_current_user_from_db()

    # Ask user about workout details
    workout_duration_in_minutes = ask_workout_duration(current_user)

    # Fetch current exercise list
    exercise_options = get_exercise_options()
    performed_exercises = ask_performed_exercises(current_user, exercise_options)
    workout_location = ask_location(current_user)


if __name__ == "__main__":
    print("Running 👟 Fitness App")
    exit(main())