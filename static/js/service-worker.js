///////////////////////////////////
// FIREBASE INITIATION
//////////////////////////////////
importScripts('https://www.gstatic.com/firebasejs/9.6.6/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.6/firebase-messaging-compat.js');

const firebaseConfig = {   
    apiKey: "AIzaSyCvQPhgNrO3VqmOLTNG-K3IIdu_n00q9u4", 
    authDomain: "ch7al-machya-web-fcm.firebaseapp.com",   
    projectId: "ch7al-machya-web-fcm",   
    storageBucket: "ch7al-machya-web-fcm.appspot.com",   
    messagingSenderId: "920203073524",   
    appId: "1:920203073524:web:f863eb5ca537c90ea38ba1",   
    measurementId: "G-QBKVL6V01W"
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
    showNotification(payload)
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