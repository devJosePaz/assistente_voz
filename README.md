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

## Estrutura do projeto

.
├── main.py # Orquestrador
├── stt.py # Gravação de áudio (sounddevice)
├── transcription.py # Whisper (STT)
├── llm.py # LLM remoto
├── tts.py # Text-to-Speech
├── audio_player.py # Reprodução do áudio
├── client.py # Tokens (.env)
├── audio.wav
├── tts.mp3

---

## Tecnologias

- Python — linguagem principal
- sounddevice + scipy — captura de áudio e salvamento em WAV
- Whisper (modelo: small) — Speech-to-Text
- Hugging Face Router — acesso remoto a LLMs
  - Modelo LLM: openai/gpt-oss-120b:fastest
- ElevenLabs (Text-to-Speech) — geração de áudio em MP3
  - Modelo TTS: eleven_multilingual_v2
- playsound / sounddevice — reprodução local do áudio
- python-dotenv — gerenciamento de variáveis de ambiente

---

## Configuração

Crie um arquivo ".env":

TOKEN_LLM=seu_token_llm
TOKEN_TTS=seu_token_tts

---

## Execução

python main.py

ENTER inicia a gravação
ENTER para parar

O sistema transcreve, gera a resposta e fala automaticamente.
