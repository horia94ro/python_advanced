def my_decorator(function): #funcția pe care  va decora este primită ca și argument
    def wrapper_function(*args, **kwargs): #parametrizarea în acest fel este necesară pentru a permite decorarea oricărei funcții
        #Set de instrucțiuni executat înainte de funcția inițială/decorată
        rez_function = function(*args, **kwargs)
        #Set de instrucțiuni executat dupa funcția inițială/decorată
        return rez_function
    return wrapper_function


def div_decorator(func):
    def wrapper_function(*args, **kwargs):
        return "<div>{}</div>".format(func(*args, **kwargs))
    return wrapper_function

@div_decorator
def web_page_content(user):
    return "Hello world, {}".format(user)

print(web_page_content("Student"))