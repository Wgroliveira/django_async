import asyncio
import random
from django.http import JsonResponse
from datetime import datetime

# View assíncrona que simula uma chamada de API
async def async_random_api_view(request):
    start_time = datetime.now()  # Marca o início do tempo
    
    # Simulando uma espera aleatória entre 2 e 10 segundos
    wait_time = random.randint(2, 10)
    await asyncio.sleep(wait_time)
    
    end_time = datetime.now()  # Marca o fim do tempo
    elapsed_time = (end_time - start_time).total_seconds()  # Calcula o tempo decorrido
    
    return JsonResponse({
        'message': 'Requisição simulada concluída!',
        'wait_time': f'{wait_time} segundos',
        'elapsed_time': f'{elapsed_time} segundos'
    })
