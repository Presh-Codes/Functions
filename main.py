def compo(**things):
    x = lambda a: a + 10
    print("Hello there, my name is", things["name"])
    print("I am", x(3), "years old.")
    print("I school at", things["school"])
    print("I am from", things["state"], "state.")
    print("My favourite meals are", meals[0], "and", meals[1])


meals = ["beans and dodo", "fried rice"]
compo(name="Precious", school="Shalom Science and Technology Academy", state="Ebonyi")


