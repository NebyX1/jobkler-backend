from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import cloudinary
from cloudinary.uploader import destroy
from cloudinary.api import NotFound
import json
import logging
from django.db import models
from apps.user_profile.models import UserProfile

# Cargar las variables de entorno
load_dotenv()

# Importar y ejecutar la configuración de Cloudinary directamente
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

logger = logging.getLogger(__name__)


def get_public_id_from_url(url):
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path  # Ejemplo: /image/upload/v1600000000/uploads/user_4/image_name.webp
        parts = path.split('/')
        upload_index = parts.index('upload')
        # public_id es todo lo que viene después de 'upload/', excluyendo la versión si está presente
        public_id_parts = parts[upload_index + 1:]
        if public_id_parts and public_id_parts[0].startswith('v'):
            public_id_parts = public_id_parts[1:]
        # Eliminar la extensión del archivo
        public_id_with_extension = "/".join(public_id_parts)
        public_id, _ = os.path.splitext(public_id_with_extension)
        logger.info(f"public_id extraído: {public_id}")
        return public_id
    except (ValueError, IndexError) as e:
        logger.error(f"Error al extraer public_id de la URL: {url} - {e}")
        return None


@csrf_exempt
def delete_image(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            public_ids = data.get('publicIds')

            logger.info(f"Datos recibidos en delete_image: {public_ids}")

            if not public_ids or not isinstance(public_ids, list):
                logger.error("Solicitud sin 'publicIds' válidos o 'publicIds' no es una lista.")
                return JsonResponse({'success': False, 'message': 'No se proporcionaron public_ids válidos'}, status=400)

            results = []
            for public_id in public_ids:
                logger.info(f"Intentando eliminar public_id: {public_id}")
                try:
                    result = destroy(public_id)
                    logger.info(f"Resultado de Cloudinary para {public_id}: {result}")

                    # Considerar 'ok' y 'not found' como eliminaciones exitosas
                    if result.get('result') in ['ok', 'not found']:
                        results.append({'public_id': public_id, 'deleted': True})
                        # Actualizar el UserProfile para eliminar la URL de la imagen
                        user_profiles = UserProfile.objects.filter(
                            models.Q(header__icontains=public_id) |
                            models.Q(certificate__icontains=public_id) |
                            models.Q(portfolio1__icontains=public_id) |
                            models.Q(portfolio2__icontains=public_id) |
                            models.Q(portfolio3__icontains=public_id)
                        )
                        for profile in user_profiles:
                            updated = False
                            if profile.header and public_id in profile.header:
                                profile.header = ""
                                updated = True
                            if profile.certificate and public_id in profile.certificate:
                                profile.certificate = ""
                                updated = True
                            if profile.portfolio1 and public_id in profile.portfolio1:
                                profile.portfolio1 = ""
                                updated = True
                            if profile.portfolio2 and public_id in profile.portfolio2:
                                profile.portfolio2 = ""
                                updated = True
                            if profile.portfolio3 and public_id in profile.portfolio3:
                                profile.portfolio3 = ""
                                updated = True
                            if updated:
                                profile.save()
                                logger.info(f"Actualizado UserProfile {profile.user.id} para eliminar la imagen {public_id}")
                    else:
                        error_message = result.get('error', {}).get('message', 'Error desconocido')
                        results.append({'public_id': public_id, 'deleted': False, 'error': error_message})
                        logger.error(f"Error al eliminar imagen {public_id}: {error_message}")
                except Exception as cloudinary_error:
                    logger.error(f"Excepción al intentar eliminar {public_id}: {cloudinary_error}")
                    results.append({'public_id': public_id, 'deleted': False, 'error': str(cloudinary_error)})

            all_deleted = all(r['deleted'] for r in results)
            if all_deleted:
                logger.info("Todas las imágenes eliminadas correctamente.")
                return JsonResponse({'success': True, 'message': 'Todas las imágenes eliminadas', 'results': results})
            else:
                logger.error("Algunas imágenes no se pudieron eliminar.")
                return JsonResponse({'success': False, 'message': 'Algunas imágenes no se pudieron eliminar', 'results': results}, status=500)

        except json.JSONDecodeError as e:
            logger.error(f"Error de JSON en la solicitud: {e}")
            return JsonResponse({'success': False, 'message': f'Error en el formato de JSON: {str(e)}'}, status=400)

        except Exception as e:
            logger.exception(f"Error general al eliminar imágenes: {e}")
            return JsonResponse({'success': False, 'message': f'Error al eliminar las imágenes: {str(e)}'}, status=500)
    else:
        logger.warning("Método HTTP no permitido en la solicitud.")
        return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)


@csrf_exempt
def check_image_exists(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            public_id = data.get('publicId')

            if not public_id:
                return JsonResponse({'exists': False, 'message': 'No se proporcionó public_id'}, status=400)

            # Utilizamos la API de Cloudinary para verificar la existencia
            cloudinary.api.resource(public_id)

            return JsonResponse({'exists': True})
        except NotFound:
            # Si la imagen no existe, se lanza una excepción NotFound
            return JsonResponse({'exists': False})
        except Exception as e:
            logger.error(f"Error al verificar la existencia de la imagen: {e}")
            return JsonResponse({'exists': False, 'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)

