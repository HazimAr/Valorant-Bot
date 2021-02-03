import consola, { Consola } from 'consola';
import { Client, MessageEmbedOptions, Message, Intents, Collection } from 'discord.js';
import glob from 'glob';
import { Command } from '../interfaces/Command';
import { Event } from '../interfaces/Event';
import { Config } from '../interfaces/Config';
import { promisify } from 'util';

const globPromise = promisify(glob);

class Bot extends Client {
    public logger: Consola = consola;
    public events: Collection<string, Event> = new Collection();
    public commands: Collection<string, Command> = new Collection();
    public config: Config;
    public constructor() {
        super({ ws: { intents: Intents.ALL }, messageCacheLifetime: 180, messageCacheMaxSize: 200, messageEditHistoryMaxSize: 200, messageSweepInterval: 180})
    };

    public aysnc start(config: Config): Promise<void> {
        this.config = config;
        this.login(config.token);
        const commandFiles: string[] = await globPromise(`${__dirname}/../this.commands/**/*{.ts,.js}}`)
    }
};

export { Bot };

