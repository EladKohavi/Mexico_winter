import { CacheClient } from '../cache/cacheClient';
import { CACHE_TABLES } from '../cache/consts';
import { STORE_OPTIONS } from '../cache/types';
import { createRedisClient } from './redis';

const client = createRedisClient();

const setupClient = async () => {
  if (!client.isReady) {
    await client.connect();
  }
};

const closeClient = async () => {
  if (client.isReady) {
    await client.quit();
  }
};

// Decorator function to connect to redis
const withRedisConnection = wrappedFunction => {
  return async function (...args: any[]) {
    await setupClient(); // Establish database connection before executing the original function
    const result = await wrappedFunction.apply(this, args);
    await closeClient(); // Close database connection after executing the original function

    return result;
  };
};

const storeItem = async (
  tableName: CACHE_TABLES,
  redisKey: string,
  redisValue: any,
  options: STORE_OPTIONS = {
    expirationInSeconds: 30 * 24 * 60 * 60,
    insertIfNotExist: false
  }
) => {
  const key = `${tableName}:${redisKey}`;
  const stringValue = JSON.stringify(redisValue);
  await client.set(key, stringValue, {
    EX: options.expirationInSeconds,
    ...(options.insertIfNotExist && { NX: true })
  });
};

const getItem = async (tableName: CACHE_TABLES, redisKey: string) => {
  const key = `${tableName}:${redisKey}`;
  const result = await client.get(key);
  if (!result) {
    return null;
  }
  return JSON.parse(result);
};

const patchItem = async (tableName: CACHE_TABLES, redisKey: string, redisValue: any) => {
  const oldItem = await getItem(tableName, redisKey);
  await storeItem(tableName, redisKey, { ...oldItem, ...redisValue });
};

export class RedisClient implements CacheClient {
  storeItem = withRedisConnection(storeItem);
  getItem = withRedisConnection(getItem);
  patchItem = withRedisConnection(patchItem);
}
