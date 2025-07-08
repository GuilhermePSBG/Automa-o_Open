# 🛠️ Automação de Cadastro - Open Ferramentaria

Este projeto realiza a automação do processo de cadastro de ferramentas na plataforma [Open Ferramentaria](https://app.openferramentaria.com.br/) utilizando **Selenium WebDriver**, **Pandas** e **Python**.

## 📌 Objetivo

Automatizar o preenchimento de formulários e cadastro de itens com base em dados de um arquivo Excel, reduzindo erros manuais e acelerando o processo.

---

## 🚀 Funcionalidades

- Login automático na plataforma.
- Navegação até o menu de cadastro de ferramentas.
- Leitura de dados a partir de um arquivo `.xlsx`.
- Preenchimento automático dos campos do formulário.
- Validação de códigos já existentes e salvamento em arquivos `.txt`.
- Registro de códigos novos também em arquivo `.txt`.

---

## 📁 Estrutura Esperada

```bash
Automação_Open/
├── test.xlsx                # Arquivo com os dados para cadastro
├── codigo_novos.txt         # Gerado com os códigos cadastrados com sucesso
├── codigo_repetidos.txt     # Gerado com os códigos já existentes
├── Cadastro_Itens.py        # Script principal da automação
└── README.md                # Este arquivo

⚙️ Tecnologias Utilizadas
Python 3.x

Selenium

Pandas

WebDriver Chrome

PyAutoGUI (opcional)

🧪 Requisitos
Google Chrome instalado.

Chromedriver compatível com a versão do Chrome.

Instalação das dependências:

bash
Copiar
Editar
pip install selenium pandas openpyxl
📄 Como usar
Abra o arquivo test.xlsx e insira os dados com as seguintes colunas (sem espaços sobrando):

Código Interno

Descrição Simples

Descrição Completa

Catégoria

Unidade

Configure os dados de login diretamente no script:

python
Copiar
Editar
email = "seu.email@empresa.com"
senha = "suasenha"
Execute o script:

bash
Copiar
Editar
python Cadastro_Itens.py

✍️ Autor
Guilherme Pimentel Santos Barbosa Gomes
Jovem Aprendiz na Hydrostec • Estudante de Licenciatura em Computação - UFBA
Email: guilhermepsbg@gmail.com

📌 Observações
Este projeto tem fins didáticos e operacionais internos. É recomendável não compartilhar credenciais públicas ou sensíveis.
