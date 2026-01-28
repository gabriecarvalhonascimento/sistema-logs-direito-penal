# 🚀 Guia Rápido de Deploy - Sistema de Gerenciamento de Logs

## Opção 1: Deploy no Streamlit Cloud (RECOMENDADO)

### Passo a Passo:

1. **Criar Repositório no GitHub**
   - Acesse [github.com](https://github.com) e faça login
   - Clique em "New repository"
   - Nome sugerido: `sistema-logs-internos`
   - Deixe como **Public** ou **Private**
   - NÃO marque "Initialize with README"
   - Clique em "Create repository"

2. **Upload dos Arquivos**
   - Na página do repositório criado, clique em "uploading an existing file"
   - Arraste e solte os seguintes arquivos:
     - `app.py`
     - `requirements.txt`
     - `README.md`
   - Clique em "Commit changes"

3. **Criar pasta .streamlit (Opcional)**
   - Clique em "Add file" > "Create new file"
   - Digite: `.streamlit/config.toml`
   - Cole o conteúdo do arquivo `config.toml`
   - Clique em "Commit changes"

4. **Deploy no Streamlit Cloud**
   - Acesse [share.streamlit.io](https://share.streamlit.io)
   - Clique em "New app"
   - Conecte sua conta GitHub (se ainda não conectou)
   - Selecione:
     - Repository: `seu-usuario/sistema-logs-internos`
     - Branch: `main`
     - Main file path: `app.py`
   - Clique em "Deploy!"
   - Aguarde 2-3 minutos

5. **Pronto!**
   - Sua aplicação estará disponível em: `https://seu-usuario-sistema-logs-internos.streamlit.app`
   - Você pode compartilhar este link ou acessar de qualquer dispositivo

---

## Opção 2: Executar Localmente

### Requisitos:
- Python 3.8 ou superior
- pip instalado

### Comandos:

```bash
# 1. Instalar dependências
pip install streamlit

# 2. Navegar até a pasta do projeto
cd /caminho/para/pasta/do/projeto

# 3. Executar a aplicação
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`

---

## Opção 3: Deploy em Outros Serviços

### Heroku
```bash
# Criar Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy
heroku create nome-do-app
git push heroku main
```

### Render
1. Conecte seu repositório GitHub
2. Selecione "Web Service"
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

---

## 📱 Acesso Discreto

### Dicas para uso em ambiente corporativo:

1. **Aba do Navegador**: O título aparecerá como "Sistema de Gerenciamento de Logs e Relatórios Internos"

2. **URL Personalizada** (Streamlit Cloud):
   - Vá em Settings > General
   - Altere o "App URL" para algo discreto como:
     - `relatorios-internos-2025`
     - `sistema-logs-ti`
     - `gestao-registros-admin`

3. **Modo Tela Cheia**:
   - Pressione F11 no navegador para esconder a barra de endereços

4. **Atalho de Teclado**:
   - Adicione aos favoritos com nome discreto
   - Use Ctrl+D para acesso rápido

---

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'streamlit'"
**Solução**: Execute `pip install streamlit`

### Erro: "Port 8501 is already in use"
**Solução**: 
```bash
# Windows
netstat -ano | findstr :8501
taskkill /PID [número_do_processo] /F

# Linux/Mac
lsof -ti:8501 | xargs kill -9
```

### Aplicação não carrega no Streamlit Cloud
**Solução**: 
- Verifique se o arquivo `requirements.txt` está no repositório
- Confirme que o arquivo `app.py` está na raiz do repositório
- Aguarde 5 minutos após o deploy inicial

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique o arquivo README.md
2. Consulte a documentação oficial: [docs.streamlit.io](https://docs.streamlit.io)
3. Revise os logs de erro no Streamlit Cloud (se aplicável)

---

**Boa sorte nos estudos! 📚**
