class Programa:  # Criei a classe mae 
    def __init__(self, nome , ano ):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes (self):
        return self._likes


    def Dar_Like(self):  
        self._likes += 1 

    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title()


    def __str__ (self):
        return f"Nome: {self._nome} - Ano :{self.ano}  - Likes: {self._likes} "


class Filme (Programa) : # Criei classe especifica que contem informações unicas
    def __init__(self, nome , ano , duração):
        super().__init__(nome,ano)
        self.duração = duração
        
    def __str__ (self):
        return f"Nome: {self._nome} - Ano: {self.ano} - {self.duração} Minutos - {self._likes} Likes "       


class Serie(Programa) : # Criei classe especifica que contem informações unicas
    def __init__(self,nome, ano,  temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} -  {self.temporadas} Temporadas - {self._likes} Likes "   


class Playlist: 
    def __init__(self, nome , programas):
        self.nome = nome
        self._programas = programas


    def __getitem__ (self, item):   # Transforma em iteravel 
        return self._programas[item]

    @property
    def listagem (self):
         return self._programas

    
    def __len__(self): # poder acessar tamanho
        return len(self._programas)        



#PROGRAMA PRINCIPAL    

Vingadores = Filme('Vingadores guerra de ultron', 2015, 160) # criei  um  filme
Game_Of_Thrones = Serie('game of thrones', 2020, 10) # Criei uma série 
Todo_Mundo_odeia_O_Cris = Serie('todo mundo odeia o cris', 2005, 8)
Avatar = Filme('avatar' , 2011 , 190)


Game_Of_Thrones.Dar_Like() # função para dar like
Vingadores.Dar_Like()
Vingadores.Dar_Like()
Avatar.Dar_Like()
Avatar.Dar_Like()
Avatar.Dar_Like()
Todo_Mundo_odeia_O_Cris.Dar_Like()

Filmes_E_Series = [Vingadores, Game_Of_Thrones, Avatar, Todo_Mundo_odeia_O_Cris] # minha lista contendo minahs series e filmes
Playlist_Domingao = Playlist('Playlist_Domingao', Filmes_E_Series)

print(f'Tamanho da minha Playlist {len(Playlist_Domingao)}') # Para usar o len primeiro fiz meu objeto herdar atribuutos de list
for programa in Playlist_Domingao: #Polimorfismo 
    print(programa)

#print(f'Avatar esta na minha Playlist ? {Avatar in Playlist_Domingao}') # Verificar sem tem algo especifico na minha lista