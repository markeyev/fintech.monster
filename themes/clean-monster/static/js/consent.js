function initCookieConsent() {
    const consent = localStorage.getItem('cookie-consent');
    const banner = document.getElementById('cookie-banner');

    if (!consent) {
        banner.classList.remove('hidden');
    }

    document.getElementById('accept-cookies').addEventListener('click', () => {
        localStorage.setItem('cookie-consent', 'accepted');
        banner.classList.add('hidden');
        window.location.reload();
    });

    document.getElementById('decline-cookies').addEventListener('click', () => {
        localStorage.setItem('cookie-consent', 'declined');
        banner.classList.add('hidden');
    });
}

window.addEventListener('DOMContentLoaded', initCookieConsent);
