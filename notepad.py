import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
import os
import sys

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad - Sem título")
        self.root.geometry("900x600")
        self.root.config(bg="#ffffff")
        
        self.arquivo_atual = None
        self.texto_modificado = False
        
        self.criar_menu()
        self.criar_area_texto()
        
        self.root.bind('<Control-s>', lambda e: self.salvar_txt())
        self.root.bind('<Control-Shift-S>', lambda e: self.salvar_como())
        self.root.bind('<Control-o>', lambda e: self.escolher_documento())
        self.root.bind('<Control-n>', lambda e: self.abrir_menu_formatar())
        
        self.area_texto.bind('<<Modified>>', self.texto_foi_modificado)
        
    def criar_menu(self):
        menu_frame = tk.Frame(self.root, bg="#f0f0f0", height=40)
        menu_frame.pack(fill="x", side="top")
        menu_frame.pack_propagate(False)
        
        estilo_botao = {
            "font": ("Segoe UI", 10),
            "bg": "#f0f0f0",
            "fg": "#000000",
            "bd": 0,
            "padx": 15,
            "pady": 8,
            "cursor": "hand2",
            "activebackground": "#e0e0e0",
            "activeforeground": "#000000"
        }
        
        btn_salvar_como = tk.Button(menu_frame, text="Salvar Como...", command=self.salvar_como, **estilo_botao)
        btn_salvar_como.pack(side="left", padx=2)
        
        btn_salvar_txt = tk.Button(menu_frame, text="Salvar .txt", command=self.salvar_txt, **estilo_botao)
        btn_salvar_txt.pack(side="left", padx=2)
        
        btn_abrir = tk.Button(menu_frame, text="Escolher Documento de Texto", command=self.escolher_documento, **estilo_botao)
        btn_abrir.pack(side="left", padx=2)
        
        btn_formatar = tk.Button(menu_frame, text="Formatar", command=self.abrir_menu_formatar, **estilo_botao)
        btn_formatar.pack(side="left", padx=2)
        
        btn_ajuda = tk.Button(menu_frame, text="Ajuda", command=self.mostrar_ajuda, **estilo_botao)
        btn_ajuda.pack(side="left", padx=2)
        
        # Variáveis de formatação
        self.quebra_automatica = True  # Começa com quebra automática
        self.estilo_fonte = "Regular"
        self.tamanho_fonte = 11

    def criar_area_texto(self):
        texto_frame = tk.Frame(self.root, bg="#ffffff")
        texto_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        scroll_vertical = tk.Scrollbar(texto_frame)
        scroll_vertical.pack(side="right", fill="y")
        
        scroll_horizontal = tk.Scrollbar(texto_frame, orient="horizontal")
        scroll_horizontal.pack(side="bottom", fill="x")
        
        self.area_texto = tk.Text(
            texto_frame,
            font=("Consolas", 11),
            bg="#ffffff",
            fg="#000000",
            insertbackground="#000000",
            wrap="none",
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set,
            undo=True,
            maxundo=-1
        )
        self.area_texto.pack(fill="both", expand=True)
        
        scroll_vertical.config(command=self.area_texto.yview)
        scroll_horizontal.config(command=self.area_texto.xview)
        
        self.area_texto.bind('<KeyPress>', self.limitar_largura_linha)
        
    def limitar_largura_linha(self, event):
        linha_atual = self.area_texto.index("insert").split('.')[0]
        texto_linha = self.area_texto.get(f"{linha_atual}.0", f"{linha_atual}.end")
        
        # Se chegou em 1024 caracteres e não é tecla especial
        if len(texto_linha) >= 1024 and event.keysym not in ['BackSpace', 'Delete', 'Return', 'Left', 'Right', 'Up', 'Down']:
            if self.quebra_automatica:
                # Quebra automática ativada - insere nova linha
                self.area_texto.insert("insert", "\n")
                return None  # Permite o caractere ser digitado na nova linha
            else:
                # Quebra manual - trava (precisa apertar ENTER)
                return "break"
    
    def texto_foi_modificado(self, event=None):
        if self.area_texto.edit_modified():
            self.texto_modificado = True
            self.area_texto.edit_modified(False)
    
    def salvar_como(self):
        conteudo = self.area_texto.get("1.0", "end-1c")
        
        arquivo = filedialog.asksaveasfilename(
            title="Salvar Como",
            defaultextension=".*",
            filetypes=[
                ("Todos os arquivos", "*.*"),
                ("Arquivo de Texto", "*.txt"),
                ("HTML", "*.html"),
                ("Python", "*.py"),
                ("JavaScript", "*.js"),
                ("CSS", "*.css"),
                ("JSON", "*.json"),
                ("XML", "*.xml"),
                ("Markdown", "*.md"),
                ("C++", "*.cpp"),
                ("Java", "*.java"),
                ("C#", "*.cs"),
                ("Batch", "*.bat"),
            ]
        )
        
        if arquivo:
            try:
                with open(arquivo, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                
                self.arquivo_atual = arquivo
                self.texto_modificado = False
                self.root.title(f"Notepad - {os.path.basename(arquivo)}")
                messagebox.showinfo("Sucesso", f"Arquivo salvo com sucesso!")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar o arquivo!")

    def salvar_txt(self):
        conteudo = self.area_texto.get("1.0", "end-1c")
        
        arquivo = filedialog.asksaveasfilename(
            title="Salvar .txt",
            defaultextension=".txt",
            filetypes=[("Arquivo de Texto", "*.txt")]
        )
        
        if arquivo:
            try:
                if not arquivo.endswith('.txt'):
                    arquivo += '.txt'
                
                with open(arquivo, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                
                self.arquivo_atual = arquivo
                self.texto_modificado = False
                self.root.title(f"Notepad - {os.path.basename(arquivo)}")
                messagebox.showinfo("Sucesso", f"Arquivo .txt salvo com sucesso!")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar o arquivo!")
    
    def escolher_documento(self):
        if self.texto_modificado:
            resposta = messagebox.askyesnocancel("Alterações não salvas", "Você tem alterações não salvas. Deseja salvar antes de abrir outro arquivo?")
            if resposta is True:
                self.salvar_txt()
            elif resposta is None:
                return
        
        arquivo = filedialog.askopenfilename(
            title="Escolher Documento de Texto",
            filetypes=[
                ("Todos os arquivos", "*.*"),
                ("Arquivo de Texto", "*.txt"),
                ("HTML", "*.html"),
                ("Python", "*.py"),
                ("JavaScript", "*.js"),
                ("CSS", "*.css"),
                ("JSON", "*.json"),
                ("XML", "*.xml"),
                ("Markdown", "*.md"),
                ("C++", "*.cpp"),
                ("Java", "*.java"),
                ("C#", "*.cs"),
                ("Batch", "*.bat"),
            ]
        )
        
        if arquivo:
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                
                self.area_texto.delete("1.0", "end")
                self.area_texto.insert("1.0", conteudo)
                
                self.arquivo_atual = arquivo
                self.texto_modificado = False
                self.root.title(f"Notepad - {os.path.basename(arquivo)}")
                
                # Resetar formatação ao abrir arquivo
                self.resetar_formatacao()
                
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo!")
    
    def abrir_menu_formatar(self):
        """Abre menu de formatação"""
        janela_formatar = Toplevel(self.root)
        janela_formatar.title("Formatar")
        janela_formatar.geometry("400x200")
        janela_formatar.config(bg="#ffffff")
        janela_formatar.resizable(False, False)
        janela_formatar.transient(self.root)
        janela_formatar.grab_set()
        
        # Título
        tk.Label(
            janela_formatar,
            text="⚙️ Opções de Formatação",
            font=("Segoe UI", 14, "bold"),
            bg="#ffffff",
            fg="#000000"
        ).pack(pady=20)
        
        # Frame dos botões
        frame_botoes = tk.Frame(janela_formatar, bg="#ffffff")
        frame_botoes.pack(pady=10)
        
        estilo_btn = {
            "font": ("Segoe UI", 11),
            "bg": "#0078d4",
            "fg": "#ffffff",
            "bd": 0,
            "padx": 20,
            "pady": 10,
            "cursor": "hand2",
            "activebackground": "#005a9e",
            "width": 25
        }
        
        # Botão de quebra de linha (muda o texto conforme estado)
        texto_quebra = "Quebra de Linha Manual (Enter)" if self.quebra_automatica else "Quebra de Linha Automática"
        btn_quebra = tk.Button(
            frame_botoes,
            text=texto_quebra,
            command=lambda: self.toggle_quebra_linha(janela_formatar),
            **estilo_btn
        )
        btn_quebra.pack(pady=5)
        
        # Botão de fontes
        btn_fontes = tk.Button(
            frame_botoes,
            text="Fontes",
            command=lambda: self.abrir_menu_fontes(janela_formatar),
            **estilo_btn
        )
        btn_fontes.pack(pady=5)
        
    def toggle_quebra_linha(self, janela_formatar):
        """Alterna entre quebra automática e manual"""
        self.quebra_automatica = not self.quebra_automatica
        
        if self.quebra_automatica:
            messagebox.showinfo("Quebra de Linha", "✅ Quebra de linha AUTOMÁTICA ativada!\n\nAo atingir 1024 caracteres, uma nova linha será criada automaticamente.")
        else:
            messagebox.showinfo("Quebra de Linha", "⚠️ Quebra de linha MANUAL ativada!\n\nAo atingir 1024 caracteres, será necessário pressionar ENTER para criar nova linha.")
        
        # Fechar e reabrir menu para atualizar o texto do botão
        janela_formatar.destroy()
        self.abrir_menu_formatar()
    
    def abrir_menu_fontes(self, janela_anterior):
        """Abre menu de seleção de fontes"""
        if janela_anterior:
            janela_anterior.destroy()
        
        janela_fontes = Toplevel(self.root)
        janela_fontes.title("Fontes")
        janela_fontes.geometry("450x450")
        janela_fontes.config(bg="#ffffff")
        janela_fontes.resizable(False, False)
        janela_fontes.transient(self.root)
        janela_fontes.grab_set()
        
        # Título
        tk.Label(
            janela_fontes,
            text="🔤 Configurações de Fonte",
            font=("Segoe UI", 14, "bold"),
            bg="#ffffff",
            fg="#000000"
        ).pack(pady=15)
        
        # ESTILO DA FONTE
        tk.Label(
            janela_fontes,
            text="Estilo da Fonte:",
            font=("Segoe UI", 11, "bold"),
            bg="#ffffff",
            fg="#000000"
        ).pack(pady=(10, 5))
        
        self.frame_estilos = tk.Frame(janela_fontes, bg="#ffffff")
        self.frame_estilos.pack(pady=5)
        
        self.criar_botoes_estilos(self.frame_estilos)
        
        # TAMANHO DA FONTE
        tk.Label(
            janela_fontes,
            text="Tamanho da Fonte:",
            font=("Segoe UI", 11, "bold"),
            bg="#ffffff",
            fg="#000000"
        ).pack(pady=(20, 5))
        
        self.frame_tamanhos = tk.Frame(janela_fontes, bg="#ffffff")
        self.frame_tamanhos.pack(pady=5)
        
        self.criar_botoes_tamanhos(self.frame_tamanhos)
        
        # Frame de botões inferiores
        frame_botoes_inferiores = tk.Frame(janela_fontes, bg="#ffffff")
        frame_botoes_inferiores.pack(pady=20)
        
        # Botão Voltar
        tk.Button(
            frame_botoes_inferiores,
            text="← Voltar",
            font=("Segoe UI", 10),
            bg="#6c757d",
            fg="#ffffff",
            bd=0,
            padx=20,
            pady=8,
            cursor="hand2",
            command=lambda: self.voltar_menu_formatar(janela_fontes)
        ).pack(side="left", padx=5)
        
        # Botão OK
        tk.Button(
            frame_botoes_inferiores,
            text="OK",
            font=("Segoe UI", 10),
            bg="#28a745",
            fg="#ffffff",
            bd=0,
            padx=20,
            pady=8,
            cursor="hand2",
            command=lambda: janela_fontes.destroy()
        ).pack(side="left", padx=5)
    
    def criar_botoes_estilos(self, frame):
        """Cria botões de estilo"""
        # Limpar frame
        for widget in frame.winfo_children():
            widget.destroy()
        
        estilos = ["Regular", "Itálico", "Negrito", "Itálico em Negrito"]
        
        for estilo in estilos:
            cor = "#0078d4" if estilo == self.estilo_fonte else "#e0e0e0"
            fg = "#ffffff" if estilo == self.estilo_fonte else "#000000"
            
            btn = tk.Button(
                frame,
                text=estilo,
                font=("Segoe UI", 10),
                bg=cor,
                fg=fg,
                bd=0,
                padx=10,
                pady=5,
                cursor="hand2",
                command=lambda e=estilo: self.aplicar_estilo_fonte(e)
            )
            btn.pack(side="left", padx=3)
    
    def criar_botoes_tamanhos(self, frame):
        """Cria botões de tamanho"""
        # Limpar frame
        for widget in frame.winfo_children():
            widget.destroy()
        
        tamanhos = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22]
        
        for i, tamanho in enumerate(tamanhos):
            cor = "#0078d4" if tamanho == self.tamanho_fonte else "#e0e0e0"
            fg = "#ffffff" if tamanho == self.tamanho_fonte else "#000000"
            
            btn = tk.Button(
                frame,
                text=str(tamanho),
                font=("Segoe UI", 9),
                bg=cor,
                fg=fg,
                bd=0,
                width=4,
                pady=5,
                cursor="hand2",
                command=lambda t=tamanho: self.aplicar_tamanho_fonte(t)
            )
            
            # 5 botões por linha
            row = i // 5
            col = i % 5
            btn.grid(row=row, column=col, padx=2, pady=2)
    
    def aplicar_estilo_fonte(self, estilo):
        """Aplica estilo de fonte SEM fechar janela"""
        self.estilo_fonte = estilo
        self.atualizar_fonte()
        # Atualizar cores dos botões
        self.criar_botoes_estilos(self.frame_estilos)
        
    def aplicar_tamanho_fonte(self, tamanho):
        """Aplica tamanho de fonte SEM fechar janela"""
        self.tamanho_fonte = tamanho
        self.atualizar_fonte()
        # Atualizar cores dos botões
        self.criar_botoes_tamanhos(self.frame_tamanhos)
    
    def atualizar_fonte(self):
        """Atualiza a fonte da área de texto"""
        # Mapear estilos para configurações tkinter
        estilos_map = {
            "Regular": ("Consolas", self.tamanho_fonte),
            "Itálico": ("Consolas", self.tamanho_fonte, "italic"),
            "Negrito": ("Consolas", self.tamanho_fonte, "bold"),
            "Itálico em Negrito": ("Consolas", self.tamanho_fonte, "bold", "italic")
        }
        
        fonte = estilos_map.get(self.estilo_fonte, ("Consolas", self.tamanho_fonte))
        self.area_texto.config(font=fonte)
    
    def voltar_menu_formatar(self, janela_fontes):
        """Volta para menu de formatação"""
        janela_fontes.destroy()
        self.abrir_menu_formatar()
    
    def resetar_formatacao(self):
        """Reseta formatação para padrão ao abrir/criar arquivo"""
        self.estilo_fonte = "Regular"
        self.tamanho_fonte = 11
        self.atualizar_fonte()
    
    def abrir_arquivo_externo(self, caminho_arquivo):
        """Abre arquivo vindo do explorador ou drag&drop"""
        if not os.path.exists(caminho_arquivo):
            messagebox.showerror("Erro", f"Arquivo não encontrado:\n{caminho_arquivo}")
            return
        
        # Verificar se já tem alterações não salvas
        if self.texto_modificado:
            resposta = messagebox.askyesnocancel(
                "Alterações não salvas",
                "Você tem alterações não salvas. Deseja salvar antes de abrir outro arquivo?"
            )
            if resposta is True:
                self.salvar_txt()
            elif resposta is None:
                return
        
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            self.area_texto.delete("1.0", "end")
            self.area_texto.insert("1.0", conteudo)
            
            self.arquivo_atual = caminho_arquivo
            self.texto_modificado = False
            self.root.title(f"Notepad - {os.path.basename(caminho_arquivo)}")
            
            # Resetar formatação ao abrir arquivo
            self.resetar_formatacao()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo!\n{str(e)}")

    def mostrar_ajuda(self):
        janela_ajuda = Toplevel(self.root)
        janela_ajuda.title("Ajuda - Notepad")
        janela_ajuda.geometry("700x500")
        janela_ajuda.config(bg="#ffffff")
        janela_ajuda.resizable(False, False)
        janela_ajuda.transient(self.root)
        janela_ajuda.grab_set()
        frame_scroll = tk.Frame(janela_ajuda, bg="#ffffff")
        frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        scrollbar = tk.Scrollbar(frame_scroll)
        scrollbar.pack(side="right", fill="y")
        texto_ajuda = tk.Text(frame_scroll, font=("Segoe UI", 10), bg="#ffffff", fg="#000000", wrap="word", yscrollcommand=scrollbar.set, bd=0, padx=10, pady=10)
        texto_ajuda.pack(fill="both", expand=True)
        scrollbar.config(command=texto_ajuda.yview)
        ajuda = """AJUDA DO NOTEPAD

SALVAR COMO: Salva com qualquer extensão (.txt, .html, .py, etc)

SALVAR .TXT: Salva rapidamente como .txt

ESCOLHER DOCUMENTO: Abre arquivos de qualquer lugar do PC

FORMATAR: Abre menu com opções de formatação
  • Quebra de Linha Manual/Automática
  • Configurações de Fontes (estilo e tamanho)

QUEBRA DE LINHA:
- Automática (padrão): Cria nova linha automaticamente aos 1024 chars
- Manual: Trava aos 1024 chars, precisa apertar ENTER

FONTES:
- Estilos: Regular (padrão), Itálico, Negrito, Itálico em Negrito
- Tamanhos: 8, 9, 10, 11 (padrão), 12, 14, 16, 18, 20, 22
- Padrão ao abrir/criar: Regular, tamanho 11

ATALHOS: 
- CTRL+S (Salvar .txt)
- CTRL+SHIFT+S (Salvar Como)
- CTRL+O (Abrir arquivo)
- CTRL+N (Abrir menu Formatar)
- CTRL+Z (Desfazer)
- CTRL+Y (Refazer)"""
        texto_ajuda.insert("1.0", ajuda)
        texto_ajuda.config(state="disabled")
        btn_entendi = tk.Button(janela_ajuda, text="Entendi", font=("Segoe UI", 12, "bold"), bg="#0078d4", fg="#ffffff", bd=0, padx=40, pady=10, cursor="hand2", command=janela_ajuda.destroy)
        btn_entendi.pack(pady=10)

def main():
    root = tk.Tk()
    app = Notepad(root)
    
    # Verificar se foi passado arquivo como argumento (abrir com...)
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
        if os.path.exists(arquivo):
            app.abrir_arquivo_externo(arquivo)
    
    root.mainloop()

if __name__ == "__main__":
    main()
