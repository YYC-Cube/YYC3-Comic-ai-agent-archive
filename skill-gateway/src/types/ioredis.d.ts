/**
 * ioredis 类型声明 — 可选依赖
 *
 * 仅声明 RedisStore 使用到的最小 API 面；包未安装时
 * 由 createRateLimitStore 工厂降级至 MemoryStore。
 */
declare module 'ioredis' {
  export interface RedisOptions {
    lazyConnect?: boolean;
    maxRetriesPerRequest?: number;
    connectTimeout?: number;
    enableOfflineQueue?: boolean;
    retryStrategy?: (times: number) => number | null;
  }
  export default class Redis {
    constructor(url: string, options?: RedisOptions);
    ping(): Promise<string>;
    on(event: string, listener: (...args: unknown[]) => void): this;
    call(command: string, ...args: unknown[]): Promise<unknown>;
    disconnect(): void;
  }
}
