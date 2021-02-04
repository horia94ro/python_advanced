def scrie_in_pagina(nume_pagina):
    def decorator_html(func):
        def wrapper_func(*args, **kwargs):
            with open(file = nume_pagina, mode = "wt") as file:
                file.write(f"<html>{func(*args, **kwargs)}</html>")
        return wrapper_func
    return decorator_html

@scrie_in_pagina("index.html")
def continut_pagina(continut):
    return continut


continut_pagina("HELLO WORLD")