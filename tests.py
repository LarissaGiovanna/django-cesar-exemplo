class Teste_04_Votacao_Resposta(BaseTestCase):
    """Testa a funcionalidade de adicionar votos em uma resposta de uma pergunta"""
    def test_07_a_resposta_deve_iniciar_com_zero_votos(self):
        print("Teste 07")
        
        #criação da pergunta e da resposta
        pergunta = self.criar_pergunta_via_model(titulo="como fazer um hello world em python?")
        self.criar_resposta_via_model(pergunta, "print('Hello World')")

        #abre a pagina de detalhes da pergunta
        self.abrir_pagina(f"/forum/{pergunta.id}")

        #procura se o body existe
        body = self.driver.find_element(By.TAG_NAME, "body").text

        time.sleep(3)

         # verifica se a contagem de votos inicial é 0
        self.assertIn("0 votos", body, "Contagem inicial de votos deveria ser 0.")

    def test_08_adiciona_um_voto(self):
        #criar pergunta de novo
        pergunta = self.criar_pergunta_via_model(titulo="Pergunta pra testar o voto unico")
        self.criar_resposta_via_model(pergunta, "Resposta da pergunta")

        self.abrir_pagina(f"/forum/{pergunta.id}/")
        #verificar se tem um titulo
        title = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))

        botao_votar = self.driver.find_element(By.ID, "votar")
        botao_votar.click()

        body = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        time.sleep(3)

         # verifica se a contagem de votos inicial é 0
        self.assertIn("1 votos", body.text, "Contagem deveria ser 1.")
