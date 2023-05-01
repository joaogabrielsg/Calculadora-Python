from tkinter import*
import itertools
import math

class Calculadora():
    def __init__(self, raiz):
        
        self.input_ = "0" 
        self.soma = Celula()
        caixa_texto = Texto(raiz, self.input_) 

        def novo_botao(text, row, column, function):
            return Botao(raiz, text, row, column, function)

        def input_numero(numero):
            return lambda : self.Numero(numero)
        
        buttons = {}

        numbers_positions = list(itertools.product([3, 4, 5], [2, 3, 4]))
        for numero in range(1, 10):
            buttons.update({str(numero) : (*numbers_positions[numero-1], input_numero(numero))})
        
        buttons.update({"0": (5, 5, input_numero(0))})

        buttons.update({
            "pi()": (2, 1, self.Pi),
            "x²": (2, 2, self.Pow),
            "log10()": (2, 3, self.Log10),
            "%": (2, 4, self.Percentual),
            "raiz()": (2, 5, self.Raiz_Quadrada),
            "clear": (2, 6, self.clear_),
            "sen()": (3, 1, self.Seno),
            "cos()": (4, 1, self.Cosseno),
            "tg()": (5, 1, self.Tangente)
        })
        
        for button in buttons.keys():
            novo_botao(button, *buttons[button])
        

    def clear_(self):
        self.input_ = "0"
        caixa_texto = Texto(raiz, self.input_)        

    def Raiz_Quadrada(self):
        temporario = math.sqrt(float(self.input_))
        self.input_ = str(temporario)
        caixa_texto = Texto(raiz, self.input_)

    def Seno(self):
        temporario = ((int(self.input_))*2*math.pi)/(360)
        self.input_ = math.sin(temporario)
        caixa_texto = Texto(raiz, self.input_)
        
    def Cosseno(self):
        temporario = ((int(self.input_))*2*math.pi)/(360)
        self.input_ = math.cos(temporario)
        caixa_texto = Texto(raiz, self.input_)

    def Tangente(self):
        temporario = ((int(self.input_))*2*math.pi)/(360)
        self.input_ = math.tan(temporario)
        caixa_texto = Texto(raiz, self.input_)

    def Log10(self):
        temporario = math.log10(int(self.input_))
        self.input_ = temporario
        caixa_texto = Texto(raiz, self.input_)

    def Pi(self):
        self.input_ = math.pi
        caixa_texto = Texto(raiz, self.input_)
        
    def Pow(self):
        self.input_ = math.pow(float(self.input_), 2)
        caixa_texto = Texto(raiz, self.input_)

    def Percentual(self):
        self.input_ = (float(self.input_)/100)
        caixa_texto = Texto(raiz, self.input_)

    def Igual(self):
        self.soma._numero_B = self.input_
        soma = self.soma
        operacao = {"soma": soma.soma,
                    "subtracao": soma.subtracao,
                    "multiplicacao": soma.multiplicacao,
                    "divisao": soma.divisao}
        v = operacao()
        caixa_texto = Texto(raiz, v)
        self.input_ = v

    def Soma(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "soma"
        self.input_ = "0"

    def Multiplicacao(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "multiplicacao"
        self.input_ = "0"

    def Divisao(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "divisao"
        self.input_ = "0"
        print(self.soma._numero_A )

    def Subtracao(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "subtracao"
        self.input_ = "0"

    def Numero(self, numero):
        self.input_ += str(numero)
        caixa_texto = Texto(raiz, self.input_)

 

class Botao():
    def __init__(self, frame, text_botao, linha, coluna, comando):
        self.button = Button(frame, text = text_botao, fg="black", bg="grey", command = comando, font = ("Arial", "20", "bold"))
        self.button["width"] = 5
        self.button["height"] = 1
        self.button.grid(row = linha, column = coluna)

class Celula():
    def __init__(self):
        self._numero_A = None
        self._numero_B = None
        self._sinal = None

    def soma(self):
        return float(self._numero_A) + float(self._numero_B)

    def subtracao(self):
        return float(self._numero_A) - float(self._numero_B)

    def multiplicacao(self):
        return float(self._numero_A) * float(self._numero_B)
    
    def divisao(self):
        return float(self._numero_A) / float(self._numero_B)

class Texto():
    def __init__(self, raiz, texto):
        self.texto = Label(raiz, text =round (float(texto), 5), font = ("Arial", "72", "bold"))
        self.texto["height"] = 2 
        self.texto["width"] = 2
        self.texto.grid(row=1, column=1, columnspan=6,sticky=W+E+N+S)

        

raiz = Tk()
raiz.title("Calculadora")
raiz.geometry("570x452")
m = Calculadora(raiz)
raiz.mainloop()
