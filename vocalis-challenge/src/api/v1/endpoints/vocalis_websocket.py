from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import logging

from src.agent.vocalis_agent import vocalis_agent_executor
from src.services.stt import MockSTTService
from src.services.tts import MockTTSService

router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    logging.info(f"WebSocket connection established for user: {user_id}")

    stt_service = MockSTTService()
    tts_service = MockTTSService()

    try:
        while True:
            # 1. Recebe o áudio do cliente.
            # Para este MVP, vamos assumir que o cliente envia um único bloco de bytes por vez.
            # Em um sistema real, aqui teríamos um buffer e detecção de fim de fala (VAD).
            audio_bytes = await websocket.receive_bytes()
            logging.info("Audio received from client.")

            # 2. Transcreve o áudio para texto
            transcribed_text = await stt_service.transcribe([audio_bytes])
            await websocket.send_text(f"OUVI: {transcribed_text}") # Feedback para o cliente

            # 3. Executa o agente com o texto transcrito
            logging.info("Invoking agent...")
            agent_response = await vocalis_agent_executor.ainvoke({
                "input": transcribed_text,
                # Adicionar memória de chat seria o próximo passo aqui
            })
            response_text = agent_response.get("output", "Não entendi, pode repetir?")
            logging.info(f"Agent response: {response_text}")
            await websocket.send_text(f"RESPONDENDO: {response_text}") # Feedback

            # 4. Sintetiza a resposta do agente em áudio
            response_audio = await tts_service.synthesize(response_text)

            # 5. Envia o áudio de volta para o cliente
            if response_audio:
                logging.info("Sending audio response to client.")
                await websocket.send_bytes(response_audio)
            else:
                logging.warning("TTS returned empty audio. Nothing to send.")

    except WebSocketDisconnect:
        logging.info(f"WebSocket connection closed for user: {user_id}")
    except Exception as e:
        logging.error(f"An error occurred in the WebSocket connection: {e}")
    finally:
        logging.info("Closing connection.")