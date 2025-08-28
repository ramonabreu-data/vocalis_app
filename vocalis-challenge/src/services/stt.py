import abc
import asyncio

# Interface abstrata que define o contrato para qualquer serviço de STT
class STTService(abc.ABC):
    @abc.abstractmethod
    async def transcribe(self, audio_chunks: list[bytes]) -> str:
        """Converte uma lista de chunks de áudio em uma string de texto."""
        pass

# Implementação Mock para testes e desenvolvimento
class MockSTTService(STTService):
    async def transcribe(self, audio_chunks: list[bytes]) -> str:
        """
        Simula a transcrição. Em vez de processar o áudio,
        apenas aguarda um pouco e retorna um texto fixo para testar o agente.
        """
        print(f"MockSTTService: Recebido {len(audio_chunks)} chunks de áudio.")
        await asyncio.sleep(0.5)  # Simula a latência da rede e do processamento

        # Retornamos um texto que sabemos que nossa ferramenta do agente consegue processar
        transcribed_text = "Adicione duas caixas de café ao carrinho"
        print(f"MockSTTService: Texto transcrito (simulado): '{transcribed_text}'")
        return transcribed_text