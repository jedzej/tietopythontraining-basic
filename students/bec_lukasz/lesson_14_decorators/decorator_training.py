def get_text(name):
   return "lorem ipsum, " + name + " dolor sit amet"


def p_decorate(func):
   def func_wrapper(name):
       return "<p>" + func(name) + "</p>"
   return func_wrapper


my_get_text = p_decorate(get_text)

print(my_get_text("John"))