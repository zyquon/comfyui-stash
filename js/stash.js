import { app } from "../../scripts/app.js";

const NAMESPACE = "zyquon.ComfyUI-Stash";

// Unfortunately, these are shared with the Python code not DRY, because it seems
// that default values do not get written to the settings.json file, so Python needs to know them too.
const DEFAULT = {
  'api_url': `http://localhost:9999/graphql`,
}

debugger

app.registerExtension({
  name: `${NAMESPACE}`,

  async setup() {
    function messageHandler(event) { alert(event.detail.message); }
    app.api.addEventListener(`${NAMESPACE}.textmessage`, messageHandler);
  },

  settings: [
    {
      id: `${NAMESPACE}.api_url`,
      name: `API URL`,
      type: `text`,
      category: [`Stash`, `Stash API`, `api_url`],
      defaultValue: DEFAULT['api_url'],
      tooltip: `Enter your Stash API URL, which you can find in your Stash settings.`,
    },
    {
      id: `${NAMESPACE}.api_key`,
      name: `API Key`,
      type: `text`,
      category: [`Stash`, `Stash API`, `api_key`],
      tooltip: `Paste your Stash API key here. You MUST set this before you can use Stash.`,
    },
  ],
})
