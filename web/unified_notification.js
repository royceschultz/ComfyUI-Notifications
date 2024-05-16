import { app } from '../../../scripts/app.js'
import {
    notificationSetup, sendNotification, getNotificationTextFromArguments,
    playSound,
    appQueueIsEmpty,
} from './util.js'


app.registerExtension({
    name: 'Notifications.UnifiedNotification',
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === 'Notif-UnifiedNotification') {
            const onExecuted = nodeType.prototype.onExecuted
            nodeType.prototype.onExecuted = async function () {
                onExecuted?.apply(this, arguments)
                const args = arguments[0] ?? {}
                if (args.mode[0] === 'on empty queue') {
                    if(!await appQueueIsEmpty(app)) return
                }
                if (args.system_notification[0]) {
                    const notif_text = getNotificationTextFromArguments(arguments)
                    sendNotification('ComfyUI', notif_text)
                }
                if (args.play_sound[0]) {
                    playSound(args.file[0], args.volume[0] ?? 0.5)
                }
            }

            const onNodeCreated = nodeType.prototype.onNodeCreated
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated?.apply(this, arguments)
                notificationSetup()
            }
        }
    },
})
