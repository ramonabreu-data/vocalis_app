import abc
import asyncio

# Interface abstrata que define o contrato para qualquer serviço de TTS
class TTSService(abc.ABC):
    @abc.abstractmethod
    async def synthesize(self, text: str) -> bytes:
        """Converte uma string de texto em bytes de áudio."""
        pass

# Implementação Mock para testes e desenvolvimento
class MockTTSService(TTSService):
    async def synthesize(self, text: str) -> bytes:
        """
        Simula a síntese de voz. Em vez de gerar áudio,
        lê um arquivo de áudio local e o retorna.
        """
        print(f"MockTTSService: Recebido texto para sintetizar: '{text}'")
        await asyncio.sleep(0.5)  # Simula a latência da rede e do processamento

        try:
            # Vamos ler um arquivo de áudio placeholder.
            # Você precisará criar este arquivo.
            with open("src/services/placeholder_response.wav", "rb") as f:
                audio_bytes = f.read()
            print("MockTTSService: Retornando áudio placeholder.")
            return audio_bytes
        except FileNotFoundError:
            print("MockTTSService: Arquivo de áudio placeholder não encontrado!")
            return b"" # Retorna bytes vazios se o arquivo não existir