(
    function () {
        let appLink = document.querySelectorAll('[app-link]')
        if (appLink) {
            appLink.forEach(link => {
                const [url, target] = link.getAttribute('app-link').split(' ')
                const location = window.location.pathname
                link.addEventListener('click', () => {
                    window.open(url, target ?? '_self')
                })
                if (location === url) link.style = 'background-color: var(--color-dark); color: white;'
            })
        }
    }
)()