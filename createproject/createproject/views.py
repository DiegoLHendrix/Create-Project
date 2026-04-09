from pyexpat import features
from urllib import request

from django.shortcuts import render


def home(request):
    # Create a list of dictionaries instead of just strings
    features = [
        {
            'image': 'Image1.png',
            'title': 'Electric Vehicle Team',
            'description': 'Member of the firmware team at RIT EVT.',
            'link': '/'
        },
        {
            'image': 'Image2.jpg',
            'title': 'Embedded Systems Design',
            'description': 'Working with custom PCBs and sensors integration for projects.',
            'link': '/'
        },
        {
            'image': 'Image3.png',
            'title': 'Digital Signal Processing',
            'description': 'Exploring DSP techniques in audio and communication systems.',
            'link': '/'
        },
    ]
    
    projects = [
        {
            'title': 'Low Voltage SubSystem',
            'description': 'Designing firmware for a low voltage system for an electric motorcycle, ensuring safety and efficiency.',
            'image': 'lvss.png',
            'tag': 'Embedded Systems Engineering'
        },
        {
            'title': 'DIY Guitar Pedal',
            'description': 'Building a custom guitar pedal with unique sound effects.',
            'image': 'pedal.jpg',
            'tag': 'Digital Signal Processing'
        },
        {
            'title': 'CAN Flashing',
            'description': 'Working on a build system for flashing firmware over CAN bus for automotive applications.',
            'image': 'project3.jpg',
            'tag': 'Embedded Systems Engineering'
        },
    ]
    
    return render(request, 'createproject/home.html', {
        'features': features,
        'projects': projects
    })
