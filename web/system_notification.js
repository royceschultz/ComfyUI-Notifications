import { app } from "../../../scripts/app.js";
import {
    notificationSetup, sendNotification, getNotificationTextFromArguments,
    appQueueIsEmpty,
} from "./util.js";

app.registerExtension({
    name: "Notifications.SystemNotification",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "Notif-SystemNotification") {
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = async function () {
                onExecuted?.apply(this, arguments);
                if (this.widgets[0].value === "on empty queue") {
                    if (!await appQueueIsEmpty(app)) return;
                }
                if (!notificationSetup()) return;
                const notification_text = getNotificationTextFromArguments(arguments)
                sendNotification("ComfyUI", notification_text)
            };

            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated?.apply(this, arguments);
                notificationSetup();
            }
        }
    },
});
