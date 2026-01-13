# 🎙️ Assistente de Voz em Python (STT + LLM + TTS)

Assistente de voz local que realiza Speech-to-Text (STT), processa a entrada
com um modelo de linguagem remoto (LLM) e gera a resposta em áudio
via Text-to-Speech (TTS).

O foco do projeto é:

- Uso e consumo de APIs de Inteligência Artificial, com atenção a custo, latência e retorno em bytes
- Integração entre STT, LLM e TTS em um único fluxo funcional
- Compreensão prática de como modelos diferentes se conectam em produção

---

## Fluxo de funcionamento

1. Entrada de voz pelo microfone
2. Captura de áudio em tempo real (sounddevice)
3. Persistência do áudio em "audio.wav"
4. Transcrição de fala para texto (Whisper)
5. Processamento de linguagem natural (LLM remoto)
6. Conversão de texto em fala (TTS – ElevenLabs)
7. Reprodução local do áudio gerado ("tts.mp3")

---

## Tecnologias

### Linguagem

- Python 3.11+

### Captura e reprodução de áudio

- sounddevice — captura de áudio via microfone
- scipy — salvamento de áudio em WAV
- numpy — manipulação de buffers de áudio
- playsound — reprodução local de áudio

### Speech-to-Text (STT)

- Whisper
  - Modelo: small

### LLM

- Hugging Face Router — acesso remoto a modelos de linguagem
  - Modelo LLM: openai/gpt-oss-120b:fastest

### Text-to-Speech (TTS)

- ElevenLabs
  - Modelo TTS: eleven_multilingual_v2

### Gerenciamento de configuração

- python-dotenv — gerenciamento de variáveis de ambiente (.env)

---

## Configuração (.env)

Crie o arquivo `.env` na raiz do projeto:

```bash
TOKEN_LLM=seu_token_llm   # Token do provedor do modelo LLM (Hugging Face Router)
TOKEN_TTS=seu_token_tts   # Token do ElevenLabs (Text-to-Speech)

```

---

## Como usar

### Preparação do ambiente virtual

```bash
# Criação do ambiente
python -m venv venv

# Execução Windows
.venv\Scripts\activate

# Execução Linux / macOS
source .venv/bin/activate

# Instalação das libs
pip install -r requirements.txt
```

###

### Execução

```bash
python main.py
```

### Exemplo pós execução:

```bash
🎙️ Pressione ENTER para iniciar a gravação

⏺️ Gravando... pressione ENTER para parar


📝 Você disse:
 O que é desenvolvimento back-end?

🤖 Resposta:

Desenvolvimento back‑end é a parte da programação que cuida da lógica,
do processamento de dados e da comunicação com bancos de dados e servidores.
Ele garante que as funcionalidades do site ou aplicativo funcionem corretamente,
gerenciando requisições, autenticação, segurança e integração com outros serviços.

🔊 Falando...

(Aqui será a resposta em audio do modelo TTS do texto acima)
```
