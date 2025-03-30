# 📼 Youtube Downloader

> Um programa que baixa vídeos através de um biblioteca chamada pytubefix, que tem esse nome por conta da versão anterior ter um erro com base em novas políticas do YouTube. A ideia veio com uma necessidade minha de ter que baixar uma mídia e não ter uma ferramenta pronta para isso.

## 🚀 Tecnologias Utilizadas
- O projeto foi escrito em **Python** e utiliza as seguintes bibliotecas:
  
  - **pytubefix**: Principal biblioteca do projeto, serve para baixar os videos fornecendo ferramentas para escolher qualidade, diretório, codec, etc.
    
  - **customtkinter**: Biblioteca para criar a interface do projeto, utilizei ela ao invés do tkinter porque ela fornece uma UI mais bonita.
    
  - **requests**: Utiliza para pegar o conteúdo da url da thumbnail dos vídeos e fazer uma conversão para mostrar na tela.
    
  - **pillow**: Para adicionar imagens a elementos dentro do customtkinter, se faz necessário um formato específico desse arquivo, essa biblioteca me ajudou no processo.
    
  - **moviepy**: Dependendo da resolução do video, o pytubefix acaba baixando somente o video sem o áudio, então preciso baixar os dois separados e fazer a fusão entre os dois arquivos.

## 📦 Instalação e Uso

### Passos para rodar o projeto

1. Clone este repositório:
   ```sh
   git clone https://github.com/andre-fe-santana/YoutubeDownloader
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd YoutubeDownloader
   ```  
3. Instale as bibliotecas usadas no projeto
  ```sh
  pip install pytubefix
  ```
  ```sh
  pip install customtkinter
  ```
  ```sh
  pip install requests
  ```
  ```sh
  pip install moviepy
  ```
  ```sh
  pip install pillow
  ```
3. Rode o programa através do seu editor de código
   

## 🛠 Funcionalidades

- ✅ Mostra thumbnail do vídeo junto com o título
- ✅ Usuário pode escolher a resolução pra baixar o vídeo
- ✅ Usuário pode escolher o diretório onde vai baixar o vídeo (embora já tenha um padrão caso ele não escolha nada)
- 🚧 Planejo adicionar outras conforme o projeto for evoluindo

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto.
2. Crie uma branch com sua feature: `git checkout -b minha-feature`
3. Commit suas alterações: `git commit -m 'Adicionando minha feature'`
4. Faça um push da branch: `git push origin minha-feature`
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

