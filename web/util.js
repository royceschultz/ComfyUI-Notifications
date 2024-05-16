export const notificationSetup = () => {
    if (!('Notification' in window)) {
        console.log('This browser does not support notifications.')
        alert('This browser does not support notifications.')
        return
    }
    if (Notification.permission === 'denied') {
        console.log('Notifications are blocked. Please enable them in your browser settings.')
        alert('Notifications are blocked. Please enable them in your browser settings.')
        return
    }
    if (Notification.permission !== 'granted') {
        Notification.requestPermission()
    }
    return true
}

export const sendNotification = (title, body) => {
    if (!notificationSetup()) return
    const notification = new Notification(title, { body })
    return notification
}

export const getNotificationTextFromArguments = (args) => {
    return args[0]?.notification_text[0] ?? 'Your notification has triggered.'
}

export const playSound = (file, volume) => {
    if (!file) {
        file = 'notify.mp3'
    }
    if (!file.startsWith('http')) {
        if (!file.includes('/')) {
            file = 'assets/' + file
        }
        file = new URL(file, import.meta.url)
    }
    const url = new URL(file)
    const audio = new Audio(url)
    audio.volume = volume
    audio.play()
}

export const appQueueIsEmpty = async (app) => {
    if (app.ui.lastQueueSize !== 0) {
        await new Promise((r) => setTimeout(r, 500))
    }
    if (app.ui.lastQueueSize !== 0) {
        return false
    }
    return true
}
