import consola, { Consola } from 'consola';
import { Client, MessageEmbedOptions, Message, Intents, Collection } from 'discord.js';
import glob from 'glob';
import { promisify } from 'util';

const globPromise = promisify(glob);

class Bot extends Client {
    public constructor() {
        super({ ws: { intents: Intents.All }, messageCacheLifetime: 180, messageCacheMaxSize: 200, messageEditHistoryMaxSize: 200, messageSweepInterval: 180})
    
    }
}