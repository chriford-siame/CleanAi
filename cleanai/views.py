from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
)
from django.views.generic import ListView
from cleanai.models import Image

from uuid import uuid4

# import os
# import keras_ocr
# from utils import inpaint_text

def index(request, *args, **kwargs):
    """Add documentation"""
    
    context = {
        "itle": "Index Page"
    }
    return render(request, 'index.html', context)

def image_background_proccessor(request):
    """Add documentation"""
    
    if request.method == "POST":

        # TODO: Export the file handling logic below as a module  
        media_file = request.FILES['media_file']
        # TODO: Process an incomming image's background
        image = Image(
            file=media_file
        )
        image.save()
        
        pipeline = keras_ocr.pipeline.Pipeline()
        if image.file:
            img_text_removed = inpaint_text(image.file.url, pipeline)
            plt.imshow(img_text_removed) # type: ignore
            cv2.imwrite(f'{uuid4()}/text_removed_image.jpg', cv2.cvtColor(img_text_removed, cv2.COLOR_BGR2RGB)) # type: ignore
        
        return redirect('main:image_background_processor')

    processed_media_files = Image.objects.order_by('created_at').order_by('updated_at').order_by('file')
    context = {
        'title': 'Background Image Remover',
        'processed_files': processed_media_files
    }
    return render(request, 'bg_remover.html', context)

def subscription_plans(request):
    return HttpResponse("")