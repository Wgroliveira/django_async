import asyncio
from django.http import JsonResponse
from datetime import datetime

# View assíncrona
async def async_counter_view(request):
    start_time = datetime.now()  # Marca o início do tempo
    await asyncio.sleep(5)  # Aguarda 5 segundos
    end_time = datetime.now()  # Marca o fim do tempo
    elapsed_time = (end_time - start_time).total_seconds()  # Calcula o tempo decorrido
    return JsonResponse({
        'message': 'Contagem concluída!',
        'elapsed_time': f'{elapsed_time} segundos'
    })
