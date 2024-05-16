import { app } from "../../../scripts/app.js";
import { playSound, appQueueIsEmpty } from "./util.js";

app.registerExtension({
    name: "Notifications.PlaySound",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "Notif-PlaySound") {
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = async function () {
                onExecuted?.apply(this, arguments);
                if (this.widgets[0].value === "on empty queue") {
                    if (!await appQueueIsEmpty(app)) return;
                }
                let file = this.widgets[2].value;
                playSound(file, this.widgets[1].value)
            };
        }
    },
});
