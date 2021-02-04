def remove_last_element(my_list):
    def get_last_elem(my_list):
        return my_list[len(my_list) - 1]
    #în acest caz, folosim o funcție inner pentru a returna ultimul element din cadrul unei liste
    my_list.remove(get_last_elem(my_list))
    #mai departe, în funcția outter vom returna rezultatul întors de funcția inner
    #în această situație, funcția inner are relevanță strict locală
    return my_list

print(remove_last_element([1, 2, "Text", "Python"]))

def outter_function(val):
    def inner_function():
        print(val)
    return inner_function #returnarea sub formă de obiect a funcției; nu vom pune paranteze

inst = outter_function(10) #apelăm funcția outter și salvăm obiectul returnat într-o zonă de memorie
inst() #putem apela funcția returnată anterior ori de câte ori avem nevoie

var_globala = "text global"
def outter(param_local):
    var_locala = "text local"
    def inner():
        print(var_globala, param_local, var_locala)
    inner()

outter("text parametru")