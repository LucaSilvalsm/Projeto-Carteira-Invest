from flask import  flash, redirect, url_for, request,session

class MessageHandler:
    def __init__(self, url):
        self.url = url

    def set_message(self, msg, msg_type, redirect_url="index"):
        # Vou inserir uma mensagem na tela 
        session["msg"] = msg
        session["type"] = msg_type

        if redirect_url != "back":
            return redirect(self.url + url_for(redirect_url))
        else:
            return redirect(request.referrer)

    def get_message(self):
        # vou pegar uma mesagem do sistema
        if "msg" in session and session["msg"]:
            return {
                "msg": session["msg"],
                "type": session["type"]
            }
        return None

    def clear_message(self):
        # vai limpar a mensagem do sistema
        session.pop("msg", None)
        session.pop("type", None)
