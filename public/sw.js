self.addEventListener('install', (e) => {
  self.skipWaiting()
})

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches
      .keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames.map((cacheName) => {
            return caches.delete(cacheName)
          }),
        )
      })
      .then(() => {
        return self.registration.unregister()
      })
      .then(() => {
        return self.clients.matchAll()
      })
      .then((clients) => {
        clients.forEach((client) => {
          if (client.url && 'navigate' in client) {
            // Circuit breaker: prevent infinite refresh loop
            // Check if URL already contains the refresh marker, skip refresh if it exists
            const url = new URL(client.url)
            if (!url.searchParams.has('pwa-cleanup')) {
              url.searchParams.append('pwa-cleanup', 'true')
              client.navigate(url.toString())
            }
          }
        })
      }),
  )
})
