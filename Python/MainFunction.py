import manjil
manjil.greet()

print(__name__)  # it indicate that it is run from this module or run from another module.
# if __name__ equal to __main__ then only the down function will run.

# Suppose we have this code in another slide
def greet():
    print("Hellow!! , It's me manjil bajgain.")
    print(__name__)
if __name__=="__main__":
    greet()

