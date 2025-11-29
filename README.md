# SmartFlow - Plataforma de Automação Inteligente de Workflows com IA

## Setup Local
1. `pip install -r requirements.txt`
2. Crie `.env` com: `OPENAI_API_KEY=sk-...` (ou GROK_API_KEY)
3. `flask db init` (se usar migrate)
4. `python run.py` → API em http://localhost:5000
5. `celery -A app.celery worker --loglevel=info`
6. Teste via Postman: POST /workflows com JWT.

## Docker
docker-compose up --build

 Ideia da Solução: "SmartFlow" – Plataforma de Automação Inteligente de Workflows com IA
Cenário principal:
Uma empresa precisa automatizar processos complexos que envolvem aprovações humanas, integração com múltiplos sistemas externos (ERP, CRM, e-mail, Slack, WhatsApp, Google Drive), enriquecimento de dados com IA (análise de sentimento, extração de entidades, geração de relatórios) e monitoramento em tempo real.
Exemplo de fluxo real:
Um vendedor cria uma proposta comercial → o sistema envia automaticamente para aprovação do gerente → a IA analisa o texto da proposta (sentimento, riscos jurídicos) → após aprovação, gera PDF, salva no Google Drive, envia por WhatsApp ao cliente, cria tarefa no CRM, notifica no Slack e gera dashboard em tempo real.
Mais no diagrama draw.io 