# 📝 NOTEPAD - Editor de Texto Profissional

Um editor de texto completo com suporte a múltiplas extensões!

---

## 🎯 CARACTERÍSTICAS

✅ Salvar com QUALQUER extensão (.txt, .html, .py, .js, .css, etc)
✅ Abrir arquivos de qualquer lugar do PC
✅ **QUEBRA DE LINHA AUTOMÁTICA** aos 1024 caracteres (NOVO!)
✅ Scroll vertical INFINITO
✅ Scroll horizontal e vertical
✅ Aviso de alterações não salvas
✅ Interface limpa e profissional
✅ Atalhos de teclado
✅ Suporte a CTRL+Z (desfazer) e CTRL+Y (refazer)

---

## 🆕 NOVIDADE v1.1 - QUEBRA AUTOMÁTICA

**ANTES (v1.0):**
- Ao atingir 1024 caracteres → ❌ TRAVAVA
- Tinha que apertar ENTER manualmente
- Interrompia a digitação

**AGORA (v1.1):**
- Ao atingir 1024 caracteres → ✅ **QUEBRA AUTOMÁTICA**
- Cria nova linha sozinho
- Continue digitando sem parar!

**Exemplo:**
```
Você digita: "Este é um texto muito longo que vai passar de 1024..."
[Chegou em 1024]
→ AUTOMÁTICO: Cria nova linha
→ Você continua: "...caracteres sem problemas!"
```

**Resultado:** Fluxo natural, sem interrupções! 🎉

---

## 🚀 COMO USAR

### Opção 1: Rodar direto do Python

```
python notepad.py
```

### Opção 2: Criar arquivo .EXE

```
compilar_notepad.bat
```

O .exe estará em: `dist\Notepad.exe`

---

## 📋 FUNCIONALIDADES

### 1. SALVAR COMO...
- Salva com qualquer extensão
- Exemplos: .txt, .html, .py, .js, .css, .json, .md
- Escolha o nome e a extensão

### 2. SALVAR .TXT
- Salva rapidamente como .txt
- Não precisa digitar a extensão

### 3. ESCOLHER DOCUMENTO DE TEXTO
- Abre arquivos de qualquer lugar
- Suporta múltiplas extensões
- Detecta alterações não salvas antes de abrir

### 4. FORMATAR
- Limpa todo o texto
- Pede confirmação antes de apagar
- Mensagem: "Tem certeza em apagar esse texto?"

### 5. AJUDA
- Mostra guia completo
- Botão "Entendi" para fechar

---

## ⌨️ ATALHOS DE TECLADO

| Atalho | Função |
|--------|--------|
| CTRL + S | Salvar .txt |
| CTRL + SHIFT + S | Salvar Como... |
| CTRL + O | Abrir arquivo |
| CTRL + N | Formatar (limpar) |
| CTRL + Z | Desfazer |
| CTRL + Y | Refazer |

---

## 📐 LIMITAÇÕES

- **Horizontal:** 1024 caracteres por linha
- **Vertical:** INFINITO (sem limite!)

Se tentar digitar mais de 1024 caracteres em uma linha, o editor bloqueia.
Para continuar escrevendo, pressione ENTER para ir para a próxima linha.

---

## 💡 EXEMPLOS DE USO

### Criando um arquivo HTML:
1. Escreva seu código HTML
2. Clique em "Salvar Como..."
3. Digite: `index.html`
4. Salve
5. Abra no navegador!

### Criando um script Python:
1. Escreva seu código Python
2. Clique em "Salvar Como..."
3. Digite: `script.py`
4. Salve
5. Execute: `python script.py`

### Criando um arquivo CSS:
1. Escreva suas regras CSS
2. Clique em "Salvar Como..."
3. Digite: `estilos.css`
4. Salve

---

## 📂 EXTENSÕES SUPORTADAS

✓ .txt - Texto simples
✓ .html - Páginas web
✓ .py - Python
✓ .js - JavaScript
✓ .css - Estilos CSS
✓ .json - Dados JSON
✓ .xml - XML
✓ .md - Markdown
✓ .cpp - C++
✓ .java - Java
✓ .cs - C#
✓ .bat - Scripts Batch
✓ E QUALQUER OUTRA!

---

## 🔧 COMPILAÇÃO

### Passo a passo:

1. Coloque os arquivos na mesma pasta
2. Execute `compilar_notepad.bat`
3. Aguarde a compilação
4. O .exe estará em `dist\Notepad.exe`

### Arquivos gerados:
```
📁 SuaPasta/
├── notepad.py
├── compilar_notepad.bat
│
├── 📁 build/
├── 📁 dist/
│   └── Notepad.exe ⭐
│
└── Notepad.spec
```

---

## ⚠️ AVISOS IMPORTANTES

### Alterações não salvas:
- O programa detecta se você tem alterações não salvas
- Antes de abrir outro arquivo, pergunta se quer salvar
- Opções: Sim / Não / Cancelar

### Formatar (limpar texto):
- Sempre pede confirmação
- Mensagem: "Tem certeza em apagar esse texto?"
- Botões: Sim / Não

---

## 🎨 INTERFACE

### Menu superior (barra cinza):
- Salvar Como...
- Salvar .txt
- Escolher Documento de Texto
- Formatar
- Ajuda

### Área de texto:
- Fundo branco
- Fonte monoespaçada (Consolas)
- Scroll horizontal e vertical
- Tamanho: 900x600 pixels

---

## 💻 REQUISITOS

- Python 3.6+ (tkinter já incluído)
- PyInstaller 5.13.2 (para compilar)
- Windows 7+ (para o .exe)

---

## 🔍 DETALHES TÉCNICOS

### Fonte:
- Consolas, tamanho 11
- Monoespaçada (ideal para código)

### Codificação:
- UTF-8 (suporta acentos, emojis, etc)

### Scroll:
- Vertical: Ilimitado
- Horizontal: Até 1024 caracteres

### Desfazer/Refazer:
- Ilimitado (CTRL+Z / CTRL+Y)

---

## 📝 DICAS

1. **Salve frequentemente!**
   - Use CTRL+S sempre que fizer alterações

2. **Use "Salvar Como" para extensões diferentes**
   - Permite escolher qualquer extensão

3. **Aproveite os atalhos de teclado**
   - São mais rápidos que clicar nos botões

4. **O limite de 1024 caracteres é por LINHA**
   - Para baixo você pode escrever infinitamente!

---

## 🐛 PROBLEMAS COMUNS

### "Python não é reconhecido"
**Solução:** Instale Python e marque "Add to PATH"

### O .exe não abre
**Solução:** Execute pelo prompt para ver erros

### Perdi meu texto
**Solução:** Sempre salve com CTRL+S!

---

## ✨ SOBRE

Editor de texto criado como projeto de aprendizado.
Feito com ❤️ usando Python e Tkinter.

**Bons textos! 📝**
