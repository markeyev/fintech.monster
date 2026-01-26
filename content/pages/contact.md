Title: Contact
Date: 2025-12-27
Status: published

<!-- # Contact Us -->

Have a tip, a question, or a corporate leak? Get in touch with the Fintech Monster editorial team.

<div class="mt-12 bg-gray-50 p-8 border border-gray-200">
    <form action="https://api.web3forms.com/submit" method="POST" class="space-y-6">
        <input type="hidden" name="access_key" value="f8eb8656-772e-4d92-9778-5ddbbeff1bf0">
        
        <div>
            <label for="name" class="block text-sm font-bold uppercase tracking-widest text-black mb-2">Name</label>
            <input type="text" name="name" id="name" required class="w-full px-4 py-3 border border-gray-300 focus:border-black outline-none transition-colors bg-white">
        </div>

        <div>
            <label for="email" class="block text-sm font-bold uppercase tracking-widest text-black mb-2">Email Address</label>
            <input type="email" name="email" id="email" required class="w-full px-4 py-3 border border-gray-300 focus:border-black outline-none transition-colors bg-white">
        </div>

        <div>
            <label for="message" class="block text-sm font-bold uppercase tracking-widest text-black mb-2">Message</label>
            <textarea name="message" id="message" rows="5" required class="w-full px-4 py-3 border border-gray-300 focus:border-black outline-none transition-colors bg-white"></textarea>
        </div>

        <input type="hidden" name="redirect" value="https://fintech.monster/pages/contact.html?status=success">

        <button type="submit" class="w-full bg-black text-white px-8 py-4 font-bold uppercase tracking-widest hover:bg-gray-800 transition-colors">
            Send Message
        </button>
    </form>
</div>

<script>
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('status') === 'success') {
        const form = document.querySelector('form');
        form.innerHTML = '<div class="bg-green-50 text-green-800 p-4 border border-green-200 font-bold uppercase tracking-widest">Message sent successfully! We will get back to you soon.</div>';
    }
</script>
