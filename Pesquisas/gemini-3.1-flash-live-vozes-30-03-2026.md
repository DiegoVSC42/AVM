# Suporte a vozes no gemini-3.1-flash-live-preview

## Resumo

O modelo `gemini-3.1-flash-live-preview` suporta as mesmas 30 vozes prebuilt disponibilizadas pelo Google para modelos de audio nativo (native audio). A configuracao via `speechConfig > voiceConfig > prebuiltVoiceConfig > voiceName` continua sendo o metodo correto e documentado. Nao ha evidencias de bugs especificos de "voz ignorada" neste modelo, mas ha relatos historicos de problemas com o SDK Python em versoes anteriores (corrigidos na v0.4+). A voz padrao, quando nenhuma e especificada, e **Puck**.

---

## 1. Lista completa das 30 vozes prebuilt

As 30 vozes sao compartilhadas entre os modelos TTS e Live API do Gemini. Todas estao disponiveis para modelos de audio nativo:

### Femininas (14)
| Voz | Personalidade |
|---|---|
| Achernar | Macia (Soft) |
| Aoede | Leve (Breezy) |
| Autonoe | Brilhante (Bright) |
| Callirrhoe | Descontraida (Easygoing) |
| Despina | Suave (Smooth) |
| Erinome | Clara (Clear) |
| Gacrux | Madura (Mature) |
| Kore | Firme (Firm) |
| Laomedeia | Animada (Upbeat) |
| Leda | Jovem (Youthful) |
| Pulcherrima | Projetada (Forward) |
| Sulafat | Calorosa (Warm) |
| Vindemiatrix | Gentil (Gentle) |
| Zephyr | Brilhante (Bright) |

### Masculinas (16)
| Voz | Personalidade |
|---|---|
| Achird | Amigavel (Friendly) |
| Algenib | Rouca (Gravelly) |
| Algieba | Suave (Smooth) |
| Alnilam | Firme (Firm) |
| Charon | Informativa (Informative) |
| Enceladus | Ressonante (Breathy) |
| Fenrir | Excitavel (Excitable) |
| Iapetus | Clara (Clear) |
| Orus | Firme (Firm) |
| Puck | Animada (Upbeat) |
| Rasalgethi | Informativa (Informative) |
| Sadachbia | Vivaz (Lively) |
| Sadaltager | Experiente (Knowledgeable) |
| Schedar | Deliberada (Deliberate) |
| Umbriel | Relaxada (Easygoing) |
| Zubenelgenubi | Casual (Casual) |

---

## 2. Suporte a voiceConfig / prebuiltVoiceConfig

**Sim, o modelo suporta.** A estrutura de configuracao documentada pelo Google e:

```javascript
// JavaScript (SDK @google/genai)
speechConfig: {
  voiceConfig: {
    prebuiltVoiceConfig: {
      voiceName: "Kore"  // qualquer uma das 30 vozes
    }
  }
}
```

```python
# Python (SDK google-genai)
speech_config=SpeechConfig(
    voice_config=VoiceConfig(
        prebuilt_voice_config=PrebuiltVoiceConfig(
            voice_name="Kore"
        )
    )
)
```

A documentacao do Vertex AI (Google Cloud) confirma que "Voice is configured in the voice_name field for all models" — ou seja, todos os modelos da Live API usam a mesma estrutura.

---

## 3. Problemas conhecidos com selecao de voz

### Issue #378 — google-gemini/cookbook (dez/2024)
- **Problema:** Desenvolvedores nao conseguiam trocar a voz padrao (Puck) para outra (ex: Charon) usando o SDK Python.
- **Causa:** O SDK rejeitava dicionarios no campo `speech_config` com o erro `"Unsupported speechConfig type: <class 'dict'>"`.
- **Resolucao:** Corrigido na versao 0.4 do SDK Python. Um workaround era passar a voz como string simples: `"speech_config": "Charon"`.
- **Modelo afetado:** `gemini-2.0-flash-exp` (nao especificamente o 3.1).

### Issue #487 — google/adk-docs (2025-2026)
- Feature request pedindo mais controle sobre vozes na Live API e suporte a vozes customizadas (custom voices).
- Nao e um bug, mas indica que a comunidade considera o suporte atual limitado.

### Issue #5018 — google/adk-python (marco/2026)
- O ADK (Agent Development Kit) Python nao suporta o modelo `gemini-3.1-flash-live-preview` corretamente.
- O envio de conteudo via `send_client_content` causa erro `APIError: 1007 None` ("Request contains an invalid argument").
- **Causa:** O Gemini 3.1 Flash Live mudou o comportamento: `send_client_content` agora so funciona para "seed" de contexto inicial; texto em tempo real deve ser enviado via `send_realtime_input`.

### Nenhum relato especifico de "voz nao corresponde a selecionada" no 3.1
- Nao encontrei relatos nos foruns do Google, GitHub Issues ou Stack Overflow de que a voz selecionada via `prebuiltVoiceConfig` seja ignorada especificamente no `gemini-3.1-flash-live-preview`.

---

## 4. Diferencas de configuracao no modelo 3.1

O guia de migracao do Google lista as seguintes **breaking changes** ao migrar de `gemini-2.5-flash-native-audio` para `gemini-3.1-flash-live-preview`:

| Aspecto | 2.5 Flash Audio | 3.1 Flash Live |
|---|---|---|
| Model string | `gemini-2.5-flash-native-audio-preview-12-2025` | `gemini-3.1-flash-live-preview` |
| Thinking config | `thinkingBudget` (numerico) | `thinkingLevel` (`minimal`, `low`, `medium`, `high`) |
| Envio de texto | `send_client_content` | `send_realtime_input` (texto em tempo real); `send_client_content` so para historico inicial |
| Eventos do servidor | Um evento = uma parte | Um evento pode conter multiplas partes (audio + transcricao simultaneos) |
| Turn coverage padrao | `TURN_INCLUDES_ONLY_ACTIVITY` | `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO` |
| Proactive audio | Suportado | **Nao suportado** ainda |
| Affective dialogue | Suportado | **Nao suportado** ainda |

**Sobre vozes:** O guia de migracao **nao menciona nenhuma mudanca** na configuracao de voz. A estrutura `speechConfig > voiceConfig > prebuiltVoiceConfig` permanece identica.

---

## 5. Half-cascade vs. Native Audio

Historicamente, os modelos da Live API tinham duas arquiteturas:

- **Half-cascade:** Usa um modelo de linguagem (LLM) para gerar texto e depois um TTS separado para sintetizar audio. Suportava apenas 8 vozes: Puck, Charon, Kore, Fenrir, Aoede, Leda, Orus, Zephyr.
- **Native audio:** Gera audio diretamente do modelo, sem TTS intermediario. Suporta todas as 30 vozes.

O `gemini-3.1-flash-live-preview` e um modelo **native audio** — portanto, suporta todas as 30 vozes.

---

## Fontes

- [Gemini 3.1 Flash Live Preview — Documentacao oficial](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)
- [Live API capabilities guide](https://ai.google.dev/gemini-api/docs/live-api/capabilities)
- [Configure language and voice — Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api/configure-language-voice)
- [Text-to-speech generation (TTS) — Gemini API](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Issue #378 — Changing default voice (google-gemini/cookbook)](https://github.com/google-gemini/cookbook/issues/378)
- [Issue #487 — Enhanced voice control (google/adk-docs)](https://github.com/google/adk-docs/issues/487)
- [Issue #5018 — ADK nao suporta 3.1-flash-live (google/adk-python)](https://github.com/google/adk-python/issues/5018)
- [Gemini 3.1 Flash Live — Blog Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/)
- [Build with Gemini 3.1 Flash Live — Blog Google Developers](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-3-1-flash-live/)
- [Gemini 3.1 Flash Live — 9to5Google](https://9to5google.com/2026/03/26/gemini-3-1-flash-live/)
- [Configuration options — Firebase AI Logic](https://firebase.google.com/docs/ai-logic/live-api/configuration)
