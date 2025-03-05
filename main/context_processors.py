# main/context_processors.py
def site_settings(request):
    """Context processor to add site settings to all templates."""
    return {
        'site_name': 'My Website',
        'site_description': 'Professional web design, business automation, and server maintenance services.',
    }