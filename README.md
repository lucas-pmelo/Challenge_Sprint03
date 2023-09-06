# Global Solution - **O2Future**

-   Computational Thinking Using Python

## Integrantes do Grupo

-   Ana Júlia Almeida Silva Neves – RM: 98974
-   Felipe Rodrigues Franco de Oliveira – RM: 552101
-   Lucas Pinheiro de Melo – RM: 97707
-   Murilo Ribeiro Valério da Silva – RM: 550858
-   Sarah Santos Teixeira – RM: 550635

## Detalhes

Esse projeto tem como objetivo, mostrar em detalhes, parte da nossa solução para o Challenge 2023 da empresa Porto.

Criamos um sistema de Banco de Dados simples, para simular um banco real que utilizaremos no projeto final, uma IA para reconhecimento de imagens
tanto para identificação de bicicletas quanto, para a identificação de texto em uma imagem (para poder verificar o número de série da Bike).

A pasta `db`, contém o arquivo `clientes.json`, que é responsável por armazenar os dados dos clientes cadastrados no sistema e suas bicicletas.

Os arquivos `yolov3.cfg`, `yolov3.weights` e `yolov3.txt` são necessários para o funcionamento da IA de reconhecimento de bicicletas.

O arquivo `requirements.txt`, contém as dependências necessárias, e suas respectivas versões para o funcionamento do programa. Logo abaixo, temos as instruções para instalar as dependências.

Para o número de série, utilize a chave `WSBC60`, pois é a chave que está sendo utilizada para o reconhecimento na imagem de teste.

## ⚠️ Sobre as Imagens

As imagens para teste, estão na pasta `reconhecimento_IA`, pois estão sendo utilizadas para o aprimoramento do programa. Por favor, utilize-as para testar o sistema.

-   Para fazer o teste de reconhecimento de texto, utilize a imagem `numero_serie.jpg` e o número de série `WSBC60` para obter sucesso.
-   Para testar a falha no teconhecimento de texto, utilize outro número de série, ou uma imagem diferente.
-   Para fazer o teste de reconhecimento de Bike, utilize as imagens `bicicleta.jpg` ou `dog.jpg`, para obter sucesso.
-   Para testar a falha no reconhecimento de Bike, utilize os arquivos `theoffice.jpg` ou `theoffice.pdf`.

O caminho para cada imagem é:

```
reconhecimento_IA/NOME_DA_IMAGEM
```

## Instruções para Instalação

### 1. Clone o repositório do projeto ou baixe os arquivos do zip:

```
git clone https://github.com/lucas-pmelo/gs_python.git
```

### 2. Instale a OCR para identificar texto em imagens:

#### **Linux**

```
sudo apt-get install tesseract-ocr
```

#### **Windows**

```
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe
```

⚠️ **É necessário adicionar o Tesseract-OCR ao PATH do sistema**

#### **MacOS**

```
brew install tesseract
```

### 3. Instale as dependências do projeto

```
pip install -r requirements.txt
```

### 4. Execute o arquivo principal em Python na sua IDE de preferência:

```
main.py
```

## Requisitos

-   Python 3.10

## Dependências

-   **numpy**
    -   É uma biblioteca de código aberto que fornece uma alta velocidade de computação de matrizes e arrays.
-   **opencv-python**
    -   É um wrapper para o pacote de código aberto de visão computacional e processamento de imagens OpenCV.
-   **packaging**
    -   É uma biblioteca para criar, gerenciar e distribuir pacotes Python. Ela fornece uma estrutura para criar, instalar, atualizar e remover pacotes Python.
-   **pillow**
    -   É uma biblioteca de imagem Python que fornece uma ampla gama de recursos para trabalhar com imagens. Ela pode ser usada para carregar, salvar, manipular, converter e exibir imagens.
-   **pytesseract**
    -   É um wrapper para o mecanismo de reconhecimento óptico de caracteres (OCR) Tesseract. Ele fornece uma API Python para acessar as funcionalidades do Tesseract.
-   **tesseract-ocr**
    -   é um mecanismo de OCR de código aberto que pode ser usado para reconhecer texto de imagens.

## Funcionalidade

O sistema possui 4 funcionalidades principais exibidas no menu:

### 1. Vistoria completa

Realiza o cadastro do cliente, caso o CPF ainda não esteja registrado em nosso sistema, dando a opção, ao final, se deseja cadastrar uma bicicleta agora, ou posteriormente. Caso já esteja cadastrado, o cliente será idenficado e pode cadastrar uma bicicleta.

### 2. Cadastrar Bike

Caso o cliente ainda não cadastrou uma Bike, ou quer cadastrar outra, essa opção permite o cadastro de uma nova Bike, para um cliente já cadastrado, por meio de uma identificação por CPF.

### 3. Mostrar clientes

Exibe todos os clientes cadastrados no sistema, com suas respectivas bicicletas.

### 4. Sair

Encerra o programa.

## Estrutura

O sistema está organizado da seguinte forma:

-   `crud.py`: Contém as funções para **cadastro de cliente**, **cadastro de bicicleta** e **exibição dos clientes já existentes**.
-   `db.py`: **Inicializa nosso sistema de Banco de Dados** e fornece funcionalidades para **ler e escrever em arquivos JSON** que **armazenam as informações dos clientes e suas bicicletas**.
-   `functions.py`: Contém funções auxiliares, como **obter valores inteiros** e **decimais** a partir da resposta do usuário, **exibir os menus**, **limpar a tela**, **printar mensagens com tempo de espera**, **sair do programa**, executar o **processo de reconhecimento das imagens pela IA** e gerenciar **tentativas falhas ao enviar as imagens**.
-   `main.py`: Arquivo principal do programa, **inicia o sistema** e gerencia o **fluxo de execução** com base nas opções selecionadas pelo usuário.
-   `models.py`: Define os modelos das classes utilizadas no sistema, como **Cliente** e **Bike**.
-   `reconhecimento_IA/ia_bike.py`: Realiza o **reconhecimento de bicicletas** em imagens utilizando a **IA**.
-   `reconhecimento_IA/ia_numero_serie.py`: Realiza o **reconhecimento de texto** em imagens utilizando a **IA**.
