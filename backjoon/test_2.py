tstring = "this is {template} {template} is {state}"
variables = [["template", "{state}"], ["state", "{template}"]]

#tstring = "{a} {b} {c} {d} {i}"
#variables = [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]



def fun(tstring,variables):
    copy_tstring = tstring
    for i in variables:
        temp = i[0]
        var_temp = '{' + temp + '}'
        if temp in tstring:
            tstring = tstring.replace(var_temp,i[1])

    #print(tstring)

        if '{' in tstring:
            fun(tstring,variables)
        else:
            return tstring


print(fun(tstring,variables))

