from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_block_tag(end_name = 'endtoast')
def toast(content):
    res = f"""
    <div class="position-fixed bottom-0 end-0 p-3">
        <div class="toast show align-items-center text-white bg-success border-0" role="alert" aria-live="assertive" aria-atomic="true" data-bs-autohide="true" data-bs-delay="3000">
            <div class="d-flex">
                <div class="toast-body">
                {content}   
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    </div>
    """
    return format_html(res)