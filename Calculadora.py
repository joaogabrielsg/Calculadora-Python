from tkinter import*
import math

class Mercado():
    def __init__(self, raiz):
        
#        frame = Frame(raiz)
#        frame.pack()
        self. a = "0" 
        self.soma = Celula()
        
        caixa_texto = Texto(raiz, self.a)
    
        self.botao1 = Botao(raiz, "1", 3, 2, lambda : self.Numero(1))
        self.botao2 = Botao(raiz, "2", 3, 3, lambda : self.Numero(2))
        self.botao3 = Botao(raiz, "3", 3, 4, lambda : self.Numero(3))
        self.botao4 = Botao(raiz, "4", 4, 2, lambda : self.Numero(4))
        self.botao5 = Botao(raiz, "5", 4, 3, lambda : self.Numero(5))
        self.botao6 = Botao(raiz, "6", 4, 4, lambda : self.Numero(6))
        self.botao7 = Botao(raiz, "7", 5, 2, lambda : self.Numero(7))
        self.botao8 = Botao(raiz, "8", 5, 3, lambda : self.Numero(8))
        self.botao8 = Botao(raiz, "9", 5, 4, lambda : self.Numero(9))
        self.botao8 = Botao(raiz, "0", 5, 5, lambda : self.Numero(0))

        self.botao_soma = Botao(raiz, "+", 3, 5, self.Soma )
        self.botao_subtracao = Botao(raiz, "-", 4, 5, self.Subtracao)
        self.botao_subtracao = Botao(raiz, "*", 3, 6, self.Multiplicacao)
        self.botao_subtracao = Botao(raiz, "/", 4, 6, self.Divisao)
        self.botao_igual = Botao(raiz, "=", 5, 6, self.Igual)
        
        self.botao_raiz_quadrada = Botao(raiz, "raiz()", 2, 5, self.Raiz_Quadrada)
        self.botao_raiz_quadrada = Botao(raiz, "c", 2, 6, self.C)
        self.botao_raiz_quadrada = Botao(raiz, "sen()", 3, 1, self.Seno)
        self.botao_raiz_quadrada = Botao(raiz, "cos()", 4, 1, self.Cosseno)
        self.botao_raiz_quadrada = Botao(raiz, "tg()", 5, 1, self.Tangente)
        self.botao_raiz_quadrada = Botao(raiz, "pi()", 2, 1, self.Pi)
        self.botao_raiz_quadrada = Botao(raiz, "x²", 2, 2, self.Pow)
        self.botao_raiz_quadrada = Botao(raiz, "log10()", 2, 3, self.Log10)
        self.botao_raiz_quadrada = Botao(raiz, "%", 2, 4, self.Percentual)
        

    def C(self):
        self.a = "0"
        caixa_texto = Texto(raiz, self.a)        

    def Raiz_Quadrada(self):
        temporario = math.sqrt(float(self.a))
        self.a = str(temporario)
        caixa_texto = Texto(raiz, self.a)

    def Seno(self):
        temporario = ((int(self.a))*2*math.pi)/(360)
        self.a = math.sin(temporario)
        caixa_texto = Texto(raiz, self.a)
        
    def Cosseno(self):
        temporario = ((int(self.a))*2*math.pi)/(360)
        self.a = math.cos(temporario)
        caixa_texto = Texto(raiz, self.a)

    def Tangente(self):
        temporario = ((int(self.a))*2*math.pi)/(360)
        self.a = math.tan(temporario)
        caixa_texto = Texto(raiz, self.a)

    def Log10(self):
        temporario = math.log10(int(self.a))
        self.a = temporario
        caixa_texto = Texto(raiz, self.a)

    def Pi(self):
        self.a = math.pi
        caixa_texto = Texto(raiz, self.a)
        
    def Pow(self):
        self.a = math.pow(float(self.a), 2)
        caixa_texto = Texto(raiz, self.a)

    def Percentual(self):
        self.a = (float(self.a)/100)
        caixa_texto = Texto(raiz, self.a)

    def Igual(self):
        self.soma._numero_B = self.a
        if (self.soma._sinal == "soma"):
            v = self.soma.soma()
        elif (self.soma._sinal == "subtracao"):
            v = self.soma.subtracao()
        elif (self.soma._sinal == "multiplicacao"):
            v = self.soma.multiplicacao()
        elif (self.soma._sinal == "divisao"):
            v = self.soma.divisao()
        caixa_texto = Texto(raiz, v)
        self.a = v

    def Soma(self):
        self.soma._numero_A = self.a
        self.soma._sinal = "soma"
        self.a = "0"

    def Multiplicacao(self):
        self.soma._numero_A = self.a
        self.soma._sinal = "multiplicacao"
        self.a = "0"

    def Divisao(self):
        self.soma._numero_A = self.a
        self.soma._sinal = "divisao"
        self.a = "0"
        print(self.soma._numero_A )

    def Subtracao(self):
        self.soma._numero_A = self.a
        self.soma._sinal = "subtracao"
        self.a = "0"

    def Numero(self, numero):
        self.a += str(numero)
        caixa_texto = Texto(raiz, self.a)

 

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
m = Mercado(raiz)
raiz.mainloop()
