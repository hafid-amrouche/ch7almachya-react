///////////////////////////////////
// FIREBASE INITIATION
//////////////////////////////////
importScripts('https://www.gstatic.com/firebasejs/9.6.6/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.6/firebase-messaging-compat.js');

const firebaseConfig = {
    apiKey: "AIzaSyB0FyjOo6-j0XK8pLcH1_NWzZqq2DDT-LM",
    authDomain: "ch7al-machya.firebaseapp.com",
    projectId: "ch7al-machya",
    storageBucket: "ch7al-machya.appspot.com",
    messagingSenderId: "1006750492863",
    appId: "1:1006750492863:web:14de76ca115914a6c1fe0a",
    measurementId: "G-074VKY03K5"
};

firebase.initializeApp(firebaseConfig);

////////////////////////////////////
// HANDLE NOTIFICATIONS CLICK
///////////////////////////////////

self.addEventListener('notificationclick', function(event) {
    event.notification.close();
    let link = event.notification.data.link
    event.waitUntil(clients.matchAll({
        type: "window"
    }).then(()=>{return clients.openWindow(link);}));
});

///////////////////////////////////
// USE FIREBASE MESSAGES
///////////////////////////////////
self.addEventListener('push', (event) => {
    let payload=event.data.json()
    if (event.data && event.data.action === 'showNotification') {
        // Check if there are any active clients
        event.waitUntil(
          clients.matchAll({ type: 'window', includeUncontrolled: true }).then(clients => {
            console.log(clients)
            // If no active clients found, display the notification
            if (!clients || clients.length === 0) {
              return showNotification(payload)
            }
          })
        );
      }
});

/////////////////////////////////
// FUNCTIONS
////////////////////////////////
const showNotification = (payload)=>{
    self.registration.showNotification(payload.notification.title, {
        body: payload.notification.body,
        icon: payload.notification.icon,
        data : payload.data,
        tag : payload.data.type
    });
}