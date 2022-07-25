from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import fileDownloader

import os
from pytube import YouTube
import glob
# Create your views here.


def index(request):
    if request.method == "POST":
        form = fileDownloader(request.POST)
        if form.is_valid():
            link = form.cleaned_data["link"]
            path = os.path.join(os.path.expanduser('~'), 'downloads')
            yt = YouTube(link)
            video = yt.streams.filter(only_audio=True).first()

            if glob.glob(f"{path}//{video.title}.*"):
                messages.warning(request, "File already exists")
                
            else:     
                out_file = video.download(output_path=os.path.join(os.path.expanduser('~'), 'downloads'))
                file_name = os.path.splitext(out_file)[0]+".mp3"
                os.rename(out_file, file_name)
                messages.success(request, "File downloaded.")            
            return redirect("index")

            


    form = fileDownloader()

    return render(request, 'index.html', {"form": form})