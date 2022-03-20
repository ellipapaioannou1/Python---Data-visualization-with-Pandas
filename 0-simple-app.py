import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = " Analysis of Course reviews", classes="text-h1")
    p1 = jp.QDiv(a=wp, text = "These graphs represent course review analysis", classes ="text-subtitle1")
    
    return wp

jp.justpy(app)